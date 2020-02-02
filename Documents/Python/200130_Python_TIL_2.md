# Python 문법에 관한 내용 일부 정리 3(Python Nested function, Closure, Decorator)

## 1. Nested function(중첩함수)

python에서 함수 또한 반복문이나 조건문과 마찬가지로 중첩하여 사용할 수 있다. 

```python
def outer_function():
  def inner_function():
    print("this is inner function")
  inner_function()

outer_function()
```

내부에 있는 ```inner_function()```은 ```outer_function()```에서만 호출이 가능하며 ```outer_function()```밖에선 호출이 될 수 없다.

그렇다면 왜 nested function을 사용하는 것일까 ? 첫번째로 우리가 함수를 사용하는 주된 이유중 하나인 반복의 방지 및 가독성이다.



```python
def outer():
  # logic A
  # logic B
  # logic A
  # logic C
  # logic A
  
outer()
```

위의 예제와 같이 어떤 함수 내에서 **logic A**가 반복되는 것을 확인할 수 있다. **logic A**를 자주 사용해야 하고 또한 추가할 상황이 있다면 ```outer()```내부에서 함수를 별도로 정의하여 유지 보수 및 관리를 쉽게 하는게 좋을 것이다.



```python
def outer():
  def logic_A():
    #logiclogiclogic
  logic_A()
  # logic B
  logic_A()
  # logic C
  logic_A()

outer()
```

위와 같이 구현하게 되면 ```outer()```함수의 가독성도 높일 수 있고 추후 ```logic_A()```를 수정할 일이 있을 때 내부 함수 하나만 수정하면 되기 때문에 유지보수가 쉬워지게 된다.



## 2. Closure(클로저)

중첩함수를 사용하는 이유 중에 또 다른 이유는 이 **closure(클로져)** 때문이다. Closure는 사전적의미로 무언가를 막다(폐쇄하다)는 의미인데 여기선 **enclosing function(외부함수)**의 변수나 로직에 대한 제한으로 보면 된다. 

외부함수의 변수나 로직에 대한 접근은 오로지 **nested function(내부함수)**에 의해서만 이뤄 진다고 보면 된다. 그래서 어떤 함수의 중요한 변수나 로직에 대한 접근과 임의의 수정을 제한하면서 해당 기능을 이용하고 싶을때 closure를 사용하게 된다.



```python
def multiply_of_n(number, n):
  return number * n

multiply_of_n(5, 7) # 35
```

위의 예제는 간단히 ```number```와 ```n```을 곱하는 함수의 예제인데 여기서 특정 숫자를 고정하고 ```n```을 곱한 값을 리턴하는 함수를 만든다고 했을 때를 가정해보자



```python
def multiply_of_three_n(n):
  return 3 * n

multiply_of_three_n(7) # 21
```

이런 식으로 3 * n을 구하는 함수를 만들 수 있는데 만약 3이 아니라 다른 숫자를 n에 곱하는 함수를 만들고 싶다면 ? 첫번째 예제와 같은 함수를 정의해서 양쪽 변수에 매번 넣던가 두번째 예제의 함수를 복붙해서 함수의 정의가 늘리는 방식으로 해나갈지도 모르겠다. 

하지만 closure개념을 사용하면 argument를 여러번 대입한다던지(parameter가 3개 이상이라 생각해보자) 조금씩 다른 기능의 비슷한 함수를 여러 개를 만든다던지 하는 불편함을 줄일 수 있다. 이를 다시 바꿔 말하면 factory 패턴의 로직을 구현할 때 closure를 쓴다고 말한다. 마치 공장처럼 특정 로직의 비슷한 함수를 효율적으로 많이 구현할 때 쓴다고 이해하면 될 것 같다.



```python
def multiply_of_number_n(base_number):
  def n_multiply(n):
    return base_number * n
  
  return n_multiply

# 미리 외부함수의 parameter값을 고정
# 외부함수의 parameter가 많아질 때도 같이 고려한다면 이렇게 함수를 정의하는게 경제적인 측면도 있음
calculate_two_mul_n = multiply_of_number_n(2)
calculate_two_mul_n(5) # 2 * 5
calculate_two_mul_n(7) # 2 * 7
calculate_two_mul_n(9) # 2 * 9
calculate_two_mul_n(11) # 2 * 11

# 함수를 또 만들 필요없이 기존에 정의한 함수를 재활용하여 3을 곱하는 함수로 생산
# 비슷한 기능의 함수를 들어가는 변수가 바뀐다고 새로 만들거나 재정의할 필요가 없다
calculate_three_mul_n = multiply_of_number_n(3)
calculate_three_mul_n(5) # 3 * 5
calculate_three_mul_n(9) # 3 * 9
calculate_three_mul_n(11) # 3 * 11
calculate_three_mul_n(13) # 3 * 13
calculate_three_mul_n(25) # 3 * 25
```



## 3. Decorator

closure의 효율적인 측면을 응용한 개념이 이 **decorator** 이다. decorator 역시 중첩함수이며 함수를 리턴한다. 이를 이용하여 decorator가 적용된 함수는 그 함수가 실행되기 전에 decorator를 통하고 나서 실행된다.

아래와 같은 상황을 가정해보자



```python
# 사람이라면 회사에 가야한다는 로직이 있다
# 어떤 함수를 구현하거나 로직을 구현할 때 사람임을 판단하고 판단되면 회사에 보내야 한다고 해보자
if is_human():
  think()

def think():
  return "생각을 할 수 있습니다."
```

위 코드와 같은 로직을 프로젝트 상에서 여러군데에 구현하고자 할 때(꽤 많은) 만에 하나 실수로 빠뜨렸다고 해보자 그렇다면 사람이 아닌 다른 무언가가 생각을 할 수 있다와 같이 무언가 판타지 스럽고 비현실적인 로직에 빠질 위험이 있다. 따라서 어떤 함수가 실행되기 이전에 무조건 특정한 함수나 로직을 거쳐야 할 때 이 decorator를 활용해 준다

```python
@is_human()
def think():
  return "생각을 할 수 있습니다."
```



위와 같은 상황에 적용되는 decorator는 아래와 같다.

```python
def is_human(func):
  is_human = True # 간결화 시킨 진위판단 로직, 이 부분은 충분히 복잡해 질 수 있다.
  def wrapper(*argc, **kwargc):
    if is_human:
      return "사람은" + func()
    else:
      return
  return wrapper
```

``wrapper()``를 리턴하므로 closure의 형태로 구현된다. 이 함수의 과정을 거쳐야 하는 여러 함수에 복수 적용가능하다.(효율성)



따라서 이 부분은 실제로 이렇게 작동하게 되는 것이다.

```python
decorated_function = is_human(think)
decorated_function()
```



### 3-1. (참고) parameter가 들어가 있는 decorator의 선언 및 적용방법

```python
def name_decorator(name):
  def wrapper(func):
    def decorator():
      return func() + name
    return decorator
  return wrapper
  

@name_decorator("정우성")
def greeting():
  return "Hello, "
```

```python
"Hello, 정우성"
```

위와 같이 parameter를 담는 함수를 하나 덧 씌워서 decorator를 만들게 되면  argument를 받는 decorator도 만들 수 있다.



## *Reference

1. <https://softwareengineering.stackexchange.com/questions/232766/when-to-use-python-function-nesting>
2. <https://www.geeksforgeeks.org/python-closures/>
3. 파이썬의 중첩함수 : <https://yes90.tistory.com/50>

4. 파이썬 decorator 써본 이야기 : <http://abh0518.net/tok/?p=604>