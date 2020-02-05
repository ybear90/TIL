# Django Official Tutorial part1 정리



(Django framework official tutorial : https://docs.djangoproject.com/ko/3.0/intro/tutorial01/#creating-a-project)

Python을 이용하여 본격적인 Back-end 개발을 하기 앞서 공식 튜토리얼을 통해 간단한 설문조사 앱을 작성하며 **django framework**에 대한 기초를 잡았고 튜토리얼을 따라가면서 중요하거나 새롭게 알게된 사실을 정리



## 시작하기 전에

### Python 가상환경 설정(miniconda3 기준)

django 프로젝트를 진행하기 앞서 가상환경을 설정해 준다. 가상환경을 설정해 주는 이유는 일반환경(로컬환경)에서 작업을 하게 되면 하나의 프로젝트만 작업하지 않는 이상 각각 project 마다 사용되는 패키지들이 버전이 충분히 다를 수 있기 때문에 여러 종류의 프로젝트를 하나의 환경에서 작업하게 되면 pip 패키지 버전차이나 기능 차이 등 여러가지 이유들로 인해 파이썬 패키지들 사이의 충돌이나 기타 다른 문제를 발생시킬 수 있다.

따라서 프로젝트 별로 로컬과는 다른 환경을 구성하여 프로젝트끼리 충돌이 없는 안정된 상태에서 작업하는 것이 좋다.

아나콘다를 사용해도 크게 문제가 없지만 해당 프로그램이 무거워서 최소한의 장점을 담고 있는 miniconda를 설치해서 사용한다
([미니콘다 설치 링크](https://docs.conda.io/en/latest/miniconda.html))

해당 os와 python에 맞는 가상환경 설치 sh를 받아서 설치를 진행해 준다.(wget이 없으면 wget을 설치)

```shell
# Mac 버전
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

# Ubuntu 버전
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 파일의 실행 권한을 수정하지 않으면 permission denied가 뜨므로 수정 하고 실행
$ chmod -R 755 Miniconda3-latest-Linux-x86_64.sh

$ ./Miniconda3-latest-Linux-x86_64.sh
```

가상환경을 로컬 환경과 **충돌없이** 구성하기 위해 zsh(.zshrc), bash(.bash_profile)등에서 PATH설정과 python과 관련된 alias 설정을 확인해준다.(둘 중 하나라도 겹치거나 충돌이 나면 가상환경을 만들더라도 python이나 pip등의 경로가 어긋나서 제대로 구성이 안될때도 있다.)

아래는 실제 가상환경을 구성할 때 자주 쓰이는 명령어를 정리해 두었다.
```shell
# conda 가상환경 목록 확인
$ conda env list

# python3.7 기반의 가상환경 만들기
$ conda create -n [virtualenv name] python=3.7

# conda 가상환경 활성화
# 아래의 명령어는 쉘 설정 파일의 PATH나 alias설정에 따라
# 유효한 명령어가 다소 차이가 있을 수 있다
$ conda activate [virtualenv name] # conda 기본
$ source activate [virtualen name] # 필자 사용 명령어

# conda 가상환경 비활성화
$ conda deactivate

# conda 가상환경 삭제
$ conda env remove -n [virtualenv name]

# conda 가상환경 export(배포용 yaml제작)
$ conda env export> "가상환경이름.yaml"

# conda expor한 가상환경 import
$ conda env create -f "가상환경이름.yaml"
```

## Part 1

### Django project 생성

가상환경이 실행되어 있는 상태에서 django를 설치(pip install django)를 해준 다음 프로젝트를 시작해준다.

```shell
(django_tutorial) $ django-admin startproject [project_name]
```



해당 프로젝트를 만들고 나서 tree구조를 확인해 보면 다음과 같다

```shell
myproject
├── manage.py
└── myproject
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

* **manage.py** : django 프로젝트에 직접 명령어를 전달하게 해주는 모듈 [링크참조](https://docs.djangoproject.com/en/3.0/ref/django-admin/)

* **myproject/settings.py** : django 프로젝트의 환경설정을 저장하는 모듈

* **myproject/urls.py** : django 프로젝트의 url들을 저장, django app에 접근하는 index의 역할

* **myproject/asgi.py** : ASGI(Asynchronous Server Gateway Interface)를 줄인 말로 django에서 비동기 웹앱을 제작하기 위한 프로토콜을 지원해 주는 모듈

* **myproject/wsgi.py** : WSGI(Web Server Gateway Interface)를 줄인 말로 django app이 웹 서버와 통신하기 위한 프로토콜을 지원해 주는 모듈(기본 프로토콜 모듈)


만든 django 프로젝트가 제대로 동작하는지 실행해 보는 쉘 명령어는 다음과 같다.

```shell
# python manage.py runserver [option : dns:port]
$ python manage.py runserver
$ python manage.py runserver 8080
$ python manage.py runserver 0:8080
```

### Django app 생성

프로젝트 안에 앱을 만드는 명령어는 다음과 같다

```shell
$ python manage.py startapp polls
```

```shell
polls
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
├── urls.py
└── views.py
```

위와 같은 구조의 app을 만들 수 있습니다 app이 제대로 작동하는지 테스트를 해보기 위해 viws.py에 내용을 작성하고 url을 각각 연결하여 테스트 해봅니다.

```python
# polls/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
```python
# polls/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
```python
# myproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

``include``함수를 사용하여 다른 URLConf(여기서 polls/urls.py)를 참조하게끔 합니다. ``path``함수에서 첫번째 argument 만큼의 문자열을 만나게 되면 남은 문자열은 두번째 argument에 include하거나 지정한 모듈에서 처리를 대신 한다.

위의 모든 과정을 무사히 마치고 다음 명령어를 실행하면 나면 "Hello, world. You're at the polls index."를 http://localhost:8000/polls/에서 확인할 수 있다.

```shell
$ python manage.py runserver
```

## Reference
https://docs.djangoproject.com/ko/3.0/intro/tutorial01/
