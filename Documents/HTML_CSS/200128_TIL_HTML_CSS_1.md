# 200128 TIL(Today I Learned) - 1

## 1. HTML 내용 정리

### 1-0. 정의

> **H**yper**T**ext **M**arkup **L**anguage의 약자로 웹페이지를 만들기 위한 언어로 웹브라우저 위에서 동작한다.(***위키피디아*** 출처)

### 1-1. 주요 구조

```html
<tagname class="class-name">contents...blahblah...</tagname>
```

* tagname : 태그의 이름에 해당 ex) html, head, body, a, h1~h6, header, section, aside div 와 같은 열린 태그와 img, hr, br과 같이 끝 태그가 존재하지 않고 시작과 동시에 종료(태그와 태그 사이에 내용이 없다)되는 닫힌 태그 등이 있다.
* class에 해당하는 부분 : 속성(attribute)로 불리며 태그에 종류에 따라 하나 이상의 여러 속성을 줄 수 있다.
* contents… 에 해당하는 부분 : 태그의 내용영역에 해당한다.

### 1-2.  HTML 태그들의 몇가지 종류(예시)

```html
<!-- 주요 구조는 다음과 같다 -->
<!DOCTYPE html> <!-- html5 버전임을 선언 -->
<html>
  <head>
    <meta charset="utf-8"> <!-- 문자 인코딩 선언 -->
    <meta name="viewpoint" content="width=device-width"> <!-- 디바이스의 가로 크기가 곧 웹 페이지의 가로와 같다 -->
    <title>title이다</title> <!-- 웹페이지의 제목 -->
  </head>
  <body>
    <div class="container"> <!-- 주로 섹션을 나눌 때 쓰는 태그 그 자체로는 의미가 있지 않다 -->
      <h1></h1> <!-- 제목태그 -->
      <span>testsetsetsetes</span> <!-- 주로 텍스트의 내용이 들어감 개행이 이루어 지지 않고 한줄로 이어서 나온다(inline-element)-->
      <p>
        paragraph test examples.paragraph test examples.paragraph test examples.paragraph test examples.paragraph test examples.paragraph test examples.paragraph test examples.
      </p> <!-- 주로 문단을 담을 때 쓰는 태그 -->
      <a href="https://www.w3schools.com/tags/tag_div.asp" target="_blank">div 태그?</a> <!-- 링크 태그 : 다른 웹페이지로 이동 할 때 쓰는 태그 -->
    </div>
  </body>
</html>
```

그 밖에 무분별한 div의 사용을 막고 코드의 가독성과 유지보수 효율을 높이기 위해 HTML5버전에서는 html영역과 기능에 따른 고유의 태그를 지원한다 [참고링크](<https://www.w3schools.com/html/html5_semantic_elements.asp>)

### 1-3. 몇가지 Attribute(속성)에 대한 내용 정리

* **id**:  각 태그에 이름(id 값)을 주는 속성, 오직 유일하게 정의 되어야 한다. 동시에 여러 태그에 정의할 수 없다(중복된 id 값은 존재하지 않는다.)
* **class**: id와 비슷한 역할을 하지만 여러 tag에 공통적으로 적용할 수 있는 속성으로 중복하여 이름을 부여할 수 있다.

```id```와 ```class```는 **CSS**를 이용하여 html에 여러가지 속성값을 줄 수 있는 **선택자(selector)**로서 많이 활용된다.

 

## 2. CSS 배운 내용 정리

### 2-0. 정의

> CSS(**C**ascading **S**tyle **S**heet)의 약어로 HTML이 실제 표시되는 방법을 기술하는 언어(***위키피디아*** 출처)

### 2-1. CSS의 구조 및 적용방식

![CSS Syntax](https://www.w3schools.com/css/selector.gif)
(이미지 출처 : https://www.w3schools.com/css)

* Selector : 선택자에 해당하고 여러 종류가 올 수 있다. 주로 **태그 이름**이나 **class 이름** 그리고 **id 이름**이 오기도 한다.
* 실제 속성값(Property)에 대한 정의는 중괄호 안에서 이뤄진다.

* 적용방식 : 

  ```html
  <h1 style="color: red;">Inline test</h1> <!-- 인라인 스타일 안에 들어가는 스타일이 길어지면 난감. 하지만 즉각적으로 style 테스트 하기는 용이하다. -->
  
  <style>
    h1 {
      color: #ffffff;
    } /* style태그를 이용한 방식 기능적으로 html과 분리되어 있지 않기 때문에 유지보수에 적합하지 않다. */ 
  </style>
  <link rel="stylesheet" type="text/css" href="index.css"/> <!-- 별도의 파일에 따로 작성하는 방법 유지보수에 용이하다 -->
  ```

### 2-2. color에 관한 몇가지 정리

* hex 색상코드 : #eb1234
* rgb값 : rgb(125, 123, 70)함수를 이용(수치의 범위는 0~255)
* hsl값 : 색상, 채도, 명도(hue, saturation, lightness)로 표현 (%값으로 정의)
* rgba값 : 기존 rgb에 a(투명도)를 더한 값



### 2-3. CSS position 정리

position 프로퍼티를 사용하면 html 코드와 상관없이 내가 원하는 위치에 요소를 나타낼 수 있다. position에는 크게 4가지(static, relative, absolute, fixed)가 있고 ```static```은 직접적으로 실제로 많이 쓰이지 않는다.(기본값, 다른 태그와의 관계에 의해 자동적으로 배치)

#### 2-3-1 relative 속성 

해당 속성은 그 자체로 눈에 띄는 변화를 주지 않는다. 다만 실제 위치를 이동(```top```, ```bottom```, ```left```, ```right```)시켜 주는 property를 사용하면 해당 요소를 이동 시킬 수 있다. 이 부분에서 처음에 헷갈릴 수 있는 부분은 다음과 같다. 

> 해당 이동 속성에 일정 pixel 값 만큼을 지정해 주면 (ex) top: 30px -> 30px만큼 '위로' 이동하겠다) 해당 속성 방향대로 일정 픽셀 값 만큼 이동하겠지 ?

하지만 실제로 해당 값을 적용해 보면 그렇지 않다는 것을 알 수 있다. ***해당 요소가 ```static```이 였던 상태를 기준으로 해당 방향 만큼(```top```, ```bottom```, ```left```, ```right```) 공백을 만든다*** 라고 생각 하면 헷갈리지 않고 이해하기가 쉬웠다. 그래서 음수 픽셀 값에 대한 부분도(ex ) top: 20px 등) 쉽게 이해가 되었던 것 같다.

한 가지 신기했던 점은 top, bottom 을 동시에 또는 left, right을 동시에 줄 경우 속성이 과도하게 지정되어 두 값이 동시에 지정이 되지 않았고 우선하는 속성이 있었다. 이에 관해서 MDN에서 이렇게 말하고 있다. (한줄 요약하면 해당 컨테이너가 left-to-right로 시작하는가 right-to-left로 시작하는가에 따라 다르다는것이 요지 아직은 잘 이해가 되지 않는다)

> When both the right CSS property and the left CSS property are defined, the position of the element is overspecified. In that case, the left value has precedence when the container is left-to-right (that is that the right computed value is set to -left), and the right value has precedence when the container is right-to-left (that is that the left computed value is set to -right). (출처 : <https://developer.mozilla.org/en-US/docs/Web/CSS/left>)



#### 2-3-2. absolute 속성

해당 요소들을 속성 그대로 절대적인 위치에 둘 수 있다. ```position: static``` 속성을 가지고 있지 않는 특정 부모를 기준으로 절대적 위치로 움직이게 된다. 만약 부모들 중 position 값이 relative, absolute, fixed값이 아닌 경우 가장위의 태그인 **body**를 기준으로 한다.

#### 2-3-3. fixed 속성

해당 요소를 특정 위치에 **고정 시킬 때** 사용한다. 눈에 보이는 브라우저 화면 기준으로 화면 내에서만 움직이는 식이여서 마치 웹페이지에서 해당 요소를 고정된 것 처럼 보이게 하고 싶을 때 사용한다.



위 내용과 관련한 실제 사용 코드 예제

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Position examples</title>
    <style>
        .relative {
            width: 200px;
            height: 100px;
            border: 3px solid green;
            position: relative;
        }
        .top-left {
            /* top: -20px; */
            right: 50px;
            left: 30px;
            bottom: 20px;
        }
        p {
            margin: 0;
            background-color: yellow;
        }
        .absolute {
            position: absolute;
        }

        .right-0 {
            right: 0;
            bottom: 0;
        }
        .fixed {
            position: fixed;
            left: 0;
            top: 0;
            background-color: yellow;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <div class="relative">div.relative</div>
    <div class="relative top-left">div.relative.top-left(-20, 30)</div>
    <div class="relative">
        <p class="absolute right-0">child</div>
    </div>
    <div class="relative">스크롤 처리용</div>
    <div class="relative top-left">스크롤 처리용</div>
    <div class="relative">스크롤 처리용</div>
    <div class="relative top-left">스크롤 처리용</div>
    <div class="relative">스크롤 처리용</div>
    <div class="relative top-left">스크롤 처리용</div>
    <div class="relative">스크롤 처리용</div>
    <div class="relative top-left">스크롤 처리용</div>
    <div class="fixed">hihihello</div>
</body>
</html>
```



##  * 참고한 자료 및 블로그 출처 :

1. mozilla MDN : <https://developer.mozilla.org/en-US/docs/Web/CSS/position>
2. zerocho blog : <https://www.zerocho.com/category/CSS/post/5864f3b59f1dc000182d3ea1>