# 200128 TIL(Today I Learned) - 2

### 2-4. CSS Display 관한 정리

![css display shortcut](https://i1.wp.com/www.tutorialbrain.com/wp-content/uploads/2019/06/CSS-Display.png?w=945&ssl=1)

(이미지 출처 : <https://www.tutorialbrain.com/css_tutorial/css_display/>)

* block 속성 : 대부분의 HTML elements들은 대부분 block 속성으로 되어 있다. ```<header>``` , ```<footer>```, ```<p>```, ```<li>```, ```<table>```, ```<div>``` 등이 대표적이다. 이 요소들은 웹브라우저 상에서 좌우를 100% 온전히 다 사용한다.(이미지 참조)

* inline 속성 : 해당 내용의 영역 만큼을 차지하는 속성으로 대표적으로 ```<span>```, ```<a>```, ```<img>```, ```<input>``` 등이 있다. width, height 등을 수정함으로 크기 지정도 가능하다.
* inline-block 속성 : inline요소와 block 요소의 장점을 하나로 합친 속성 ```css```에서 display 속성에 임의로 부여하는 식으로 주로 사용됨. 위 이미지 처럼 **grid layout** 등을 구성할 때 많이 쓰임. inline속성을 가지고 있기 때문에 역시 크기 조정도 가능하다.
* (추가) none 속성 : 이 속성은 해당 요소를 화면에서 보이지 않게 해준다. none 그 자체의 효과로서 단독으로 쓰이기 보단. **포탈 사이트 등에서 검색어 입력 창에 문자열이 들어있을 때** 연관검색어 등이 뜨는 것 처럼 웹을 동적으로 만들어 줄 때 많이 쓰인다. 

display 속성을 활용하여 block 속성으로 inline이나 inline-block 속성으로, inline속성을 block이나 inline-block 속성으로 변경하는 것도 가능하다.

기타 자세한 설명과 다른 속성(예를 들면 flex등)은 해당 URL을 참고할 것(https://developer.mozilla.org/en-US/docs/Web/CSS/display)



### 2-5. float 속성에 관한 정리

**float**은 주로 image나 기타 다른 컨텐츠들을 감싸면서 layout을 잡는 용도로 많이 쓰이는 속성이다. ```left```, ```right```, ```none``` 등의 속성 값이 있다.

float을 사용하게 되면 float이라는 말 그대로 떠있다보니 부모 요소가 높이를 인지하지 못하고 따라서 다른 요소들의 영역을 겹치고 침범하는 문제가 발생한다. 이를 해결하는 방법은 아래 몇 가지가 있다

1.  float이 적용된 태그(컨테이너) 다음에 아무 태그나 넣고 **clear** 속성을 넣어준다. html 코드를 추가로 입력해야 한다는 부담이 적용된다.

2. float이 적용된 태그에 ```overflow: hidden;``` css 속성을 추가해 준다.

3. float을 담고 있는 태그 또한 float옵션을 적용해준다 역시 뜨기 때문에 float 속성이 적용된 컨텐츠를 인식하게 된다.(block  성질을 잃어 버리는 문제가 있다) 

4. float을 담고있는 태그에 아래와 같은 css옵션을 적용해 준다

   ```css
   .clearfix {
     overflow: auto;
   }
   ```

5. 떠있는 요소의 영역의 너비만큼 margin을 적용하여 애초에 영역 침범이 일어나지 않게 한다(계산의 번거로움, 때때로 %너비를 활용 하기도 함)

하지만 float 속성을 잘 활용하면 원하는 컨텐츠들을 원하는 위치에 자유롭게 구성하여 더 나은 디자인의 웹페이지를 구현하는데 용이하다.

아래 예제를 통해 실제 float이 어떻게 쓰이는지 참고(실제 코드 테스트 적용 가능)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>float example</title>
    <style>
        .main-page, .home-page {
            height: 200px;
        }

        .main-page header {
            background-color: yellow;
        }

        .main-page aside {
            float: left;
            width: 200px;
            background-color: green;
        }

        .main-page section {
            background-color: blue;
        }

        .home-page header {
            background-color: yellow;
        }

        .home-page aside {
            float: right;
            width: 200px;
            background-color: green;
        }

        .home-page section {
        margin-right: 200px;
        background-color: blue;
        }
    </style>
</head>
<body>
    <h3>assignment 1</h3>
    <div class="main-page">
      <header>배너</header>
      <aside>사이드바</aside>
      <section>main contents</section>
    </div>
    
    <h3>assignment 2</h3>
    <div class="home-page">
      <header>배너</header>
      <aside>사이드바</aside>
      <section>main contents</section>
    </div>
</body>
</html>
```



### 2-6. border-box를 쓰는 이유 간략하게 정리

FE개발자가 매번 요소들을 추가할 때 padding, margin영역을 한꺼번에 고려하여 실제 컨텐츠의 크기를 계산해야 하는 번거로움을 줄이기 위해 ```box-sizing: border-box```등을 사용하기도 한다. 그 밖에 ```content-box```, ```border-box```, ```initial```, ```inherit``` 등이 있고 상황에 따라 달리 사용할 수도 있음을 인지한다.

# * 참고한 자료 및 블로그 출처 :

1.  CSS layout을 배우는 사이트 : <http://ko.learnlayout.com/clearfix.html>

2.  layout관련 참고한 사이트 : 
   http://ko.learnlayout.com/

   https://poiemaweb.com/css3-layout

   https://poiemaweb.com/css3-box-model

3. border-box관련 참고 사이트(블로그) : <https://www.codingfactory.net/10630>

4. float을 clear하는 방법에 관한 정리 블로그 : <https://naradesign.github.io/article/float-clearing.html>

   

   