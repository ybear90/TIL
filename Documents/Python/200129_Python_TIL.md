# Python 문법에 관한 내용 일부 정리(python function keyword arguments, Parameter Default Value)

## 1. Python keyword arguments

Python 함수에서 정의된 parameter의 순서와는 다르게  parameter의 이름을 명시해 준다면 순서가 반대로 되어도 값을 전달 해 주는 것이 가능하다

```python
def test_function(my_parameter, your_parameter):
  print(f"{my_parameter} 그리고 {your_parameter}".format(my_parameter, your_parameter))

# 실행 결과 : 내꺼 and 니꺼 <- 이렇게 정상적으로 나온다
# parameter1 = value <- 이런 식으로 parameter 이름으로 맞춰서 값을 전해주는 것을 keyword arguments라고 한다. 
test_function(your_parameter = "니꺼", my_parameter = "니꺼")
```

keyword arguments를 명시하면서 함수를 실행하게 되면 가독성도 높아질 수 있고 만일 실수로 값이 바뀌었다 하더라도 어떤 parameter인지 명시적으로 알 수 있기 때문에 관련 오류가 발생했다 하더라도 바로 조치가 가능하다는 장점이 있다.

### 1-1. positional arguments와 같이 쓸 때 유의할 점

keyword arguments는 그 parameter가 확실히 명시되어 있기 때문에 순서가 바뀌어도 상관이 없지만 일반 arguments들(positional arguments)은 어떤 값인지 명시되어 있지 않기 때문에 그 순서가 중요하다. 당연하게도 엉뚱한 곳에 해당 값이 들어가게 되면 원치 않는 결과를 출력하게 되기 때문이다.

이 둘을 같이 사용할 때는 순서를 지켜줘야 하며 그렇게 하지 않으면 에러를 발생시키게 된다.

```python
test_function(your_parameter = "니꺼", "내꺼")
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

에러가 나는 이유는 positional argument의 순서가 틀렸기 때문이다(첫번째에 와야 하는데 두번째에 왔다) 실제로 그렇게 되었다고 에러 메세지가 친절히 설명해 준다.

## 2. Parameter Default Value

함수에 parameter 그 자체에 default값을 정의해 줄 수도 있는데 이럴땐 default값이 정의되지 않은 parameter 보다 먼저 위치해서는 안된다. 실제로 syntax error가 발생한다.

```python
def test_func(my_param = "hello", your_param):
...     print(f"{my_param} hello world {your_param}")
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

### 2-1. 그렇다면 왜 에러가 나는 것일까 ?

아래와 같은 경우를 생각해보자.

```python
test_func("world") # my_param에 들어갈지 your_param에 들어갈지 모호해진다
test_func("world", "hello") 
```

만약 ```test_func```가 에러 없이 선언 되었다면 위의 함수들이 실행 되어야 한다. 그러나 해당 argument가 어떤 parameter에 해당 하는지 모호해져 버린다. 따라서 의도치 않는 함수 로직의 실행을 막고자 python interpreter에서 에러로 처리를 하게 되는 것이다. 이런 모호한 점을 방지하기 위해 아래와 같이 ```non-default value```는 앞에서 정의 되어야 하며 ```parameter default value```들은 ```non-default value``` 뒷 부분에 정의 되어야 한다.



## * Reference

1. 점프 투 파이썬 e-book : <https://wikidocs.net/24#_9>
2. Stackoverflow link : <https://stackoverflow.com/questions/16932825/why-cant-non-default-arguments-follow-default-arguments>





