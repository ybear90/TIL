# Python 문법에 관한 내용 일부 정리 2(python while-else, kwargs)



## 1. Python while-else 구문

파이썬에선 특이하게도 ```while```반복문과 연결해서 ```else```가 따라올 수 있게 되어있다. 있는 그대로 직역하게 되면 **while이 아니면 실행해라**는 식으로 해석 될 수 있지만 그런 의미가 아니다.



> while loop를 break없이(예외없이) 끝까지 다 돌고 나서 else이하의 구문들을 실행해라 즉 while의 조건문이 **아니게 되면** 실행해라.



는 의미를 가지고 있다. 예를 들면,

```python
num = 0
while num < 5:
  print(num, end=' ')
  num += 1
else: # indent 주의할 것 while-else문이기 때문에 if-else 연결하듯이 코딩
  print("loop가 무사히 끝났습니다")
```

```python
0 1 2 3 4 loop가 무사히 끝났습니다
```

```while```문에서 ```num```을 증가시키며 출력하고 ```num = 5```가 되어 빠져나갔을 때 바로 ```print```문이 실행 되는 것을 확인할 수 있었다.



### 1-1. while-else에서 else를 실행시키기 못하는 경우

while-else문에서 else가 실행되지 않고 빠져나갈 때가 있는데 아래와 같은 경우에 else문을 실행하지 않게 된다.

```python
num = 0
while num < 5:
  print(num, end=' ')
  if num == 3:
    break
else:
  print("loop가 무사히 끝났습니다")
```

```python
0 1 2
```

```while```문 내에서 임의로 ```break``` 조건을 주거나 반복문이 다 실행되지 않고 종료될 경우엔 ```while``` 조건문이 완벽하게 ```False```가 되지 않았으므로 ```else``` 문을 거치지 않는다.



### 1-2. (참고) for-else 구문에 대해서

while-else문과 마찬가지로  for loop에도 else구문이 붙을 수 있는데 ```while```문과 같이 ```for``` 문의 수행이 무사히 돌게 되면 ```else``` 를 실행하게 되고 그렇지 않고 ```break``` 등으로 종료되게 되면 ```else``` 구문이 실행되지 않는다.

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

위의 예제는 소수를 판별하는 예제인데, 안쪽 ```for``` loop를 실행하는 동안 특정 조건에 의해서 break되지 않으면 즉 소인수 들로 나눠지지 않으면 ```else```문을 거쳐서 ```print()```를 실행하게 되고 그렇지 않으면 실행하지 않게 된다. 

이렇게 하게되면 특정 조건에서 loop가 깨지는 유무를 쉽게 알 수 있어 특정 반복 실행 여부에 대한 테스트를 하기 좋다.



## 2. Python *args, **kwargs 정리

### 2-1. *args(**Non-keyworded variable length of arguments**)

python에서 특정 기능을 하는 함수를 구성할 때, 내가 얼만큼 arguments들을 받아야 하는지 결정하기 애매할 때가 있다. 간단하게 더하는 함수만 구성하려고 해도 몇개의 수를 더할 지 명확하게 정할 수 없을 때 ```*args```, ```**kwargs``` 와 같은 parameter로 정의한다. 



우선 ```*args```는 여러 개의 인자를 **tuple**의 형태로 받는다.

```python
def extendable_sum(*args):
  return sum(args)
```

```python
print(extendable_sum(1, 2)) # 3
print(extendable_sum(1, 2, 3)) # 6
print(extendable_sum(1, 2, 3, 4)) # 10
print(extendable_sum(1, 2, 3, 4, 5)) # 15
```

```python
def args_test(*args):
  return args
```

```python
>>> print(type(args_test()))
<class 'tuple'>
```

위 예제 처럼 ```*args```를 활용하면 특정하지 않은 여러개의 변수에 대한 연산을 간단한 함수를 통해 쉽게 구현할 수 있다. 



### 2-2. **kwargs(Keyworded variable length of arguments)

```**kwargs```는 ```*args```와는 다르게 일반 변수들(positional argument)이 아닌 keyword arguments들 즉 **dictionary 형태**의 변수들을 넣고 싶은데 그 수가 정해지지 않을 때 사용된다.

```python
# full_name을 return 해주는 함수
# first_name이나 last_name이라는 keyword arguments들 중 하나만 있으면 이름이 출력되고
# full_name을 모두 갖추게 되면 kwargs['last_name'] + ' ' + kwargs['first_name']로 출력
def what_is_my_full_name(**kwargs):
  if 'first_name' not in kwargs.keys() and 'last_name' not in kwargs.keys():
    return "Nobody"
  elif 'first_name' in kwargs.keys() and 'last_name' not in kwargs.keys():
    return kwargs['first_name']
  elif 'first_name' not in kwargs.keys() and 'last_name' in kwargs.keys():
    return kwargs['last_name']
  else:
    return kwargs['last_name'] + ' ' +kwargs['first_name']

print(what_is_my_full_name(first_name="CG", last_name="Y")) # Y CG
print(what_is_my_full_name(first_name="CG")) # CG
print(what_is_my_full_name(last_name="Y")) # Y
print(what_is_my_full_name()) # Nobody
```

위 예제 처럼 keyword arguments의 갯수나 keyword등이 미리 정해지지 않았지만 활용하고 싶을 때 ```**kwargs```을 사용한다. ```**kwargs```는 그 형태가 **dictionary**처럼 사용된다.



### 2-3. (참고) 함수의 parameter 사용 순위

이전 parameter, argument와 관련된 포스트에서 parameter나 argument가 선언되고 호출 될 때 순서가 중요하다고 언급했다. 아래 이미지는 그와 관련되어 사진 한장으로 정리 된 것이니 참고할 것

![python function parameter order](http://getkt.com/wp-content/uploads/2019/02/python-function-definition-arguments-kind-and-order.jpg)

(***이미지 출처***: <https://getkt.com/blog/types-of-function-arguments-in-python/>) 



## *Reference

1.  python official docs : <https://docs.python.org/3/reference/compound_stmts.html#while>