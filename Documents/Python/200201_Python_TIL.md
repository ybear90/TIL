# Python 문법에 관한 내용 일부 정리 (sys module, path 정리)



## 1. Sys module

Python은 여러 모듈이 합쳐져서 프로젝트를 이루게 된다 ```pip```를 이용하여 모듈 패키지를 추가할 수 있고 용도에 따라 웹개발이나, AI/ML개발, 게임 개발 등이 가능하다. 개발자 개인이 만든 **local package module** 을 이용하여 더 다양한 프로젝트를 만들 수 있다. 그렇다면 ``import`` 를 써서 어떻게 모듈과 패키지를 찾는 것일까 ?



### 1-1. import search order



Python은 크게 세가지 구역에서 아래와 같은 순서로 module/package들을 찾게 된다

>  **sys.modules** => **built-in modules** => **sys.path** 



#### ``sys.modules``

Python이 module이나 package를 찾기 위해 우선적으로 살피는 영역으로 dictionary형태로 되어 있다

```python
>>> import sys
>>> print(sys.modlues)
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, 'encodings': <module 'encodings' from  .... '/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/rlcompleter.py'>, 'mod1': <module 'mod1' from '/Users/YB/Google 드라이브/TIL/Documents/Python/mod1.py'>}
```

python을 실행하고 한 번 이상 import가 되었다면 다시 모듈을 찾지 않고 곧바로 sys.modules를 확인하여 module이나 package를 사용하게 된다. 한 번 이상 사용되었거나 이미 내장 되어 있는 module이나 패키지만 존재하므로 새롭게 import되는 것들은 없다고 보면 된다.



#### ``built-in modules``

파이썬에서 공식으로 제공하는 라이브러리. 당연히 설치하자 마자 깔리는 것들이고 쉽게 찾을 수 있게 된다. 위에 sys.modules ``print()`` 출력 결과를 확인하게 되면 어떤 것이 built-in modules인지 쉽게 확인 할 수 있다.



#### ``sys.path``

파이썬이 module이나 package를 찾을 때 가장 마지막으로 확인하는 부분입니다. ``pip`` 로 새롭게 설치한 패키지도 이 곳을 통해 찾게 되며 새롭게 작성한 패키지나 모듈을 사용하고자 할 때 이 곳에 **path를 등록** 해서 찾게끔 설정해 준다.(설정하는 방법은 해당 시스템의 OS에 따라 다소 차이가 있다) 해당 변수는 **list** 의 형태로 구성되어 있다(쉽게 할당 삭제가 가능하다)

```python
>>> import sys
>>> print(sys.path)
['', '/Users/YB/Google 드라이브/TIL/Documents/Python', '/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/YB/Library/Python/3.7/lib/python/site-packages', '/usr/local/lib/python3.7/site-packages']
```

(해당 리스트의 1번째 인덱스 문자열을 보면 임의로 등록한 path임이 확인 된다)



위 3개의 구역에서 module이나 package를 찾지 못하게 되면 ``ModuleNotFoundError``를 발생시킨다.



### 1-2. How to search sys module ?



그렇다면 module/package 검색에 근원이 되는 ``sys`` 모듈은 어떻게 찾게 되는 것일까 ? 이미 위에 답이 나와있다

> 'sys': <module 'sys' (built-in)>

``sys``모듈은 이미 built-in 되어 있기 때문에 built-in module들이 있는 부분에서 찾게 된다.



## 2. Absolute path and Relative path(절대경로와 상대경로)

Python을 사용하다 보면 **built-in 모듈**과 **pip** 모듈을 사용하는데 있어 사용법만 잘 숙지 한다면 크게 경로 관련 문제가 생기지 않는다.(경로가 명확하게 정의되어 있기 때문에, built-in은 설치되면서 내장되어 있고 pip는 각각 python설치 경로 중에 site-package라는 곳에 모두 저장되어 있다. 해당 경로는 ``sys-path``에 저장되어 있다) 문제는 직접 만든 모듈이나 패키지를 사용할 때이다.



```shell
my_app
├── main.py
├── pkg1
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── pkg2
│   ├── __init__.py
│   ├── module3.py
│   ├── module4.py
│   ├── module5.py
│   └── pkg4
│       ├── __init__.py
│       └── module6.py
└── pkg3
    ├── __init__.py
    └── module7.py
```

위와 같은 프로젝트가 있다고 가정해보자



### 2-1. Absolute path

absolute path는 모듈 및 패키지의 시작부터 끝까지 생략이나 축약되지 않고 명확히 명시된 경로를 뜻한다. 어디에서 쓰든 항상 같아서 사용하는데 헷갈리지 않다는 장점이 있다.



```python
# main.py
from pkg1 import module1
from pkg1.module2 import func3
from pkg2 import module3
from pkg2.pkg4.module6 import func10
```

경로의 시작점은 해당 module및 패키지 있는 current directory(이 부분은 sys.path에 자동 등록 되어 있다)으로 하기 때문에 main.py가 아닌 어디에서 사용하던 항상 같은 방법으로 쓰면 된다.



### 2-2. Relative path



```python
# pkg2/module5.py
# relative path를 적용하기 전
from pkg1.module2 import func3
from pkg2 import module3
from pkg2.pkg4.module6 import func10
```



relative path는 최상위 경로가 아닌 현재 자기가 속한 경로를 기준으로 정의한다. 주로 local package안에서 다른 local package를 참조할 때 쓰인다.



```python
# pkg2/module5.py
# relative path를 적용한 후
from ..module2 import func3
from . import module3
from .pkg4.module6 import func10
```

```python
# pkg4/module6.py
from ..module5 import func_12
```



위의 두 예제 모두 현재경로 (pkg2, pkg4)를 기준으로 새롭게 ``from .. import``를 적용한 코드이다. absolute path에 비해 간결해 지는 장점이 있지만 프로젝트가 커지고 복잡도가 높아질 수록 혼동이 될 수 있으며 만일 파일의 위치가 바뀌게 되면 그에 맞춰서 path도 재설정 해주어야 한다. 따라서 아무리 복잡한 프로젝트라 하더라도 코드의 일관성 및 실수를 막고자 absolute path의 사용이 권장되는 편이다.







