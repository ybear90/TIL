# Python 문법에 관한 내용 일부 정리 4(Python scope)

## 1. Scope

scope는 어떤 변수나 객체 등이 적용될 수 있는 말 그대로 범위라고 보면 된다. python에선 해당 변수나 객체가 생성된 지점에서 상위 객체까지, 아래로는 모든 하위 객체와 그 내부 까지에 해당된다.



Scope개념은 크게 4종류로 나눠 볼 수 있다.

* Local Scope
* Enclosed Scope
* Global Scope
* Built-in Scope

![kinds_of_scope](https://wellsr.com/python/assets/images/2018-09-07-scopes-diagram.png)

(이미지 출처 : https://wellsr.com/python/assets/images/2018-09-07-scopes-diagram.png)



### 1-1. Local Scope

```python
def local_scope():
  local_var = 1
  print(local_var)

print(local_var) # local_Var는 함수 내에서만 호출 가능하므로 호출이 불가하다
```

위의 예제처럼 local scope는 해당 변수, 함수 객체가 선언된 그 특정 범위 내에서만 유효 한 것을 뜻한다. 함수 내부에 선언된 변수나 함수가 이에 해당된다.



### 1-2. Enclosing Scope

```python
def enclosing_scope():
  enclosing_var = 2
  def inner_func():
    inner_var = 3
    print(enclosing_var * inner_var) # 6이 나온다
 	
  inner_func()
  print(inner_var)
```

위의 예제에서  ```enclosing_var``` 를 주목해 보면 외부함수에서 정의가 되었지만 내부함수에서 까지 사용됨을 알 수 있다. 주로 중첩함수가 정의 되어 있을 때 사용되는 scope의 개념이라고 생각하면 된다. 다시 말해 외부 함수에서 선언된 변수나 함수는 그 내부함수에 까지 영향을 미치게 되는 것이다.



### 1-3. Global Scope

말 그대로 함수나 클래스, 객체 내부에 선언 된 변수나 함수가 아닌 그 밖에 선언된 변수나 객체 scope를 뜻한다. 

```python
global_Var = 10

def outer_func():
  outer_var = global_var + 3
  print(outer_var) # 13이 출력된다
  def inner_func():
    inner_var = global_var * 10
    print(inner_var) # 100이 출력된다

print(global_var) # 10이 출력된다
```

선언된 지점에 대한 동일 지역 및 그 하위 까지 모두 접근이 가능함을 확인할 수 있다.



### 1-4. Built-in Scope

python 설치 파일 안에 바로 내장 되어 있는 어떤 python 파일을 작성하든지 간에 항상 포함되는 가장 광범위한 scope라고 보면 된다. 별다른 선언없이 실행되는 ```len()```, ```input()```, ```print()``` 와 같은 python 내장 함수등이 해당 범위에 해당된다.



### 1-5. Shadowing

> Local scope -> Enclosing scope -> Global Scope -> Built-in Scope

python은 선언된 변수나 함수의 정의를 찾을 때 선언된 지점을 기준으로 가장 가까운 범위서 부터 찾게 되고 가장 가까운 범위에 있는 정의를 가장 우선시한다. 



```python
test_var = 10

def func1():
  test_var = 12
  print(test_var)
  def func2():
    test_var = 100
    print(test_var)
  
print(test_var)
```

```python
10
func1 test:  12
func2 test:  100
```



위와 같이 출력되는 것을 확인할 수 있다.