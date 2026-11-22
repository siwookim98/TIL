## DOM

#### 웹 브라우저에서의 JavaScript
1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console

### 문서 구조
#### Document structure
HTML 문서는 여러 상자가 중첩된 구조로 볼 수 있음
각 상자는 객체이며 개발자는 이 객체와 상호작용하여 
어떤 HTML 태그를 나타내는지, 어떤 콘텐츠가 포함되어 있는지
객체 모델(Document Object Model) = DOM

#### DOM
웹페이지를 구조화된 객체로 제공
트리 노드 구조

#### DOM API
웹페이지에 접근 및 조작 페이지 요소들을 객체 형태로 제공
메서드도 제공, 명령어 모음

### document 객체
#### document 객체
#### document 객체 예시
console -> document.title = 'siwook'

### DOM Tree
#### DOM tree
head 노드, body 노드 다시 자식 노드 가질 수 있음

#### 핵심 포인트
DOM 핵심 : 객체로 제공해서 JS에서 접근 조작할 수 있는 방법을 제공하는 API

### DOM 선택
#### DOM 조작 시 기억해야 할것
1. 요소를 선택

### 선택 메서드
#### document.querySelector(selector)
없다면 null 반환 첫번째 element 객체를 반환
#### document.querySelectorAll(selector)
NodeList를 반환
```html
<script>
    // 1. querySelector(selector)
    // - CSS 선택자와 일치하는 "첫 번째" 요소 하나를 반환 (없으면 null)
    console.log(document.querySelector('.heading')) // <h1 class="heading">
    console.log(document.querySelector('.content')) // 첫 번째 <p> (content1)만 선택

    // 2. querySelectorAll(selector)
    // - CSS 선택자와 일치하는 "모든" 요소를 NodeList로 반환
    // - NodeList는 배열과 비슷하지만 배열은 아님 (forEach는 가능, map/filter는 불가능)
    console.log(document.querySelectorAll('.content')) // NodeList(3)
    console.log(document.querySelectorAll('ul > li')) // NodeList(2), CSS의 자식 선택자도 그대로 사용 가능
  </script>
```
