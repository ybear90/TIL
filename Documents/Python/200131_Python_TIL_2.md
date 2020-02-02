# Python 문법에 관한 내용 일부 정리 5(Python module, package 내용 정리)

## 1. python package관련

### 1-1. 모듈 관련 간략 정리

\__init__.py 는 package가 import될 때의 초기설정을 가능하게 해주는 py파일이다. 즉 해당 디렉터리가 패키지임을 알려주는 역할을 한다. (파이썬 3.3 버전 이후로 해당 파일을 직접 만들어 주지 않아도 패키지로 인식이 된다고 한다 ([링크참고(PEP 420)](https://www.python.org/dev/peps/pep-0420/)))



아래와 같은 파이썬 프로젝트가 있다고 가정해보자.

```python
app/
    __init__.py
    sound/
        __init__.py
        main_Sound.py
        click_sound.py
    graphic/
        __init__.py
        screen.py
        images.py
    logic/
        __init__.py
        business_logic1.py
        business_logic2.py
```

```python
# main_sound.py
def sound_test():
  print("sound on")
```

```python
# click_sound.py
def sound_test():
  print("click on")

def all_test():
  pass
```



```main_sound.py```라는 모듈을 실행 시키는 방법은 아래와 같다.



1. 단순히 **main_sound 모듈을 import**하는 방법

```python
>>> import app.sound.main_sound
>>> app.sound.main_sound.sound_test()
sound on
```



2. **main_sound 모듈이 있는 경로까지 from … import 구문**으로 선언

```python
>>> from app.sound import main_sound
>>> main_sound.sound_test()
sound on
```



3. **main_sound 모듈에 sound_test함수를 직접** import

```python
>>> from app.sound.main_sound import sound_test
>>> sound_test()
sound on
```



그러나 단순히 최상단을 import하는 것으로는 에러가 발생할 수 있다.

```python
>>> import app
>>> app.sound.main_sound.sound_test()
Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no atribute 'sound'
```

에러를 토대로 해석해보면 sound는 **python 모듈**이 아니기 때문에 module객체에 할당 받을 수 없다는 뜻이다.  ```app``` 디렉토리의 모듈 또는 ``__init__.py``에 정의가 되어 있는 부분만 참조 할 수 있다.



아래와 같은 방법으로 함수를 사용하는 것도 불가능하다.

```python
>>> import app.sound.main_sound.sound_test
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ImportError: No module named sound_test
```

```import a, b, c``` 라고 했을 때 가장 마지막 항목인 c는 **파이썬 모듈** 이나 **파이썬 패키지** 여야 하기 때문이다.

여기서 정확히 ``__init__.py`` 는 어떤 용도로 쓰이는 것일까 ?



### 1-2. \__init__.py의 역할

``__init.py__``는 다음과 같은 역할을 한다



- import 할 때 경로의 길이를 줄이기
- package에서 import 할 수 있는 변수/함수/클래스 제한
- package가 import 될 때 반드시 먼저 실행 되야 하는 코드 작성



경로를 줄이는 것은 아래와 같이 할 수 있다.

```python
# __init__.py
from app.sound.main_sound import sound_test
```

```python
# __init__.py가 있는 경로의 python
>>> sound_test()
```

위에서 처럼 여러번 사용할 필요없이 사전에 정의된 ``__init__.py`` 를 통해 함수를 좀 더 간결하게 부를 수 있게 되었다.



하지만 여러개의 패키지내의 모듈이 존재하고 각각의 함수나 객체들의 이름이 중복이 되거나 불필요하게 선언이 되선 안될 시에는 어떻게 할까 ? 그럴때는 ``__init__.py`` 에서 아래와 같이 처리해 주면 된다



```python
# __init__.py
# 패키지를 실행하려면 패키지를 적용할 경로에 대해 PYTHONPATH등록을 해주어야 한다
# 앞에 점이 없거나 sound 라는 부모 패키지 명을 명시해 주지 않으면 에러가 발생한다
# (외부에서 해당 파일을 실행할 때는 경로가 명시 되어야 한다고 추측 중)
from .main_sound import sound_test 
from .click_sound import sound_test as click_test # 이름 중복 처리

# __all__ 내부 변수를 통해 처리 가능 (default는 모든 함수/변수/클래스)
# * 기호를 사용하여 import를 할 경우 이곳에 정의된 것들만 실행된다
__all__ = ['sound_test', 'click_test'] # 문자열의 형태로 사용할 함수, 변수, 클래스를 담는다
```

```python
# main.py 위치는 app 패키지가 있는 그 위치에 있다
from app.sound import * # 
sound_test()
click_test()
```

```python
sound on
click on
```



위와 같이 중복된 이름의 함수들을 호출했고 꼭 필요한 함수만 호출 할 수 있었다.



### 1-3. ``__name__`` 과 ``if __name__ == "__main__"`` 의 의미

하나의 모듈 파일을 작성해보자

```python
# mod1.py
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

print(add(3, 5))
print(sub(4, 2))
```

```python
$ python mod1.py
8
2
```



이 모듈을 파이선 인터프리터에서 import를 해보면 아래와 같다.

```python
>>> import mod1
8
2
```

그저 import해서 모듈에 있는 함수를 쓰고 싶었지만 의도와는 다르게 되었다. 해당 모듈을 직접 호출하던, import를 통해 간접 호출을 하던 py파일 내에서 온전히 실행되게끔 코드가 짜져 있기 때문이다. 또한 python은 C나 Java와 같은 언어와는 다르게 스크립트 기반 인터프리터 언어로서 특별히 시작 지점이 명시가 되어 있지 않은 언어이다. 그래서 특별한 변수를 할당하여 **현재 스크립트의 시작점**이 어디인지 판단한다. 그 변수로서 이용하는 것이 ``__name__`` 이다. 



다시말해 하나의 py 파일이 만들져 실행 될 때마다 ``__name__`` 변수를 할당하여 "\_\_main\_\_" 을 저장하게 된다. 반면에 사용될 모듈로서 import등이 될 경우에는 ``__name__`` 에 '모듈명'이 들어가게 된다 (ex) hello.py일 경우 'hello'가 할당됨)  이와 같은 방식으로 python은 스크립트의 시작점을 명시한다.



따라서 위와 같이 모듈로서만 해당 모듈을 이용하기 위해서는 아래와 같이 구성해 주면 된다.

```python
# mod1.py
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

print(add(3, 5))
print(sub(4, 2))

if __name__ == "__main__":
  print(add(a, b))
  print(sub(a, b))
```

```python
>>> import mod1
>>>
```



## Reference

1. stackoverflow <What does if \_\_name\_\_ == "\_\_main\_\_": do?> : <https://stackoverflow.com/questions/419163/what-does-if-name-main-do>

2. 파이썬 코딩 도장 e-book : <https://dojang.io/mod/page/view.php?id=2448>

3. 점프 투 파이썬 e-book : <https://wikidocs.net/1418>

   





