# Javascript DOM

## 서론

라틴어 - 1. 스페인어 2. 프랑스어 3. 이탈리아어 4. 포르투칼어
언어의 유사도 파이썬과 자바스크립트

html css js google 검색
active한 현상 = 자바스크립트
프론트엔드 개발에 있어서 3대 기초 html css js 
conerstones of internet

dom = 브라우저에서 액션을 통해 새로운 모습을 보여준다의 기반이 되는 dom
선택과 조작
html을 자바스크립트가 인식하고 바꿔줄 수 있다

## History of JavaScript

### 웹 브라우저와 JavaScript

#### 웹의 탄생(1990)

Sir Tim Berners-Lee : 
www-world wide web 전 세계적인 정보 공유 시스템
URL : 특정 웹페이지나 파일을 찾기 위한 고유한 경로 주소
HTTP : 웹 브라우저와 서버가 데이터를 주고 받기 위한 통신 규약
웹은 정작인 텍스트 페이지만 지원
공적으로 진행한 무언가

#### 웹 브라우저의 대중화(1994)

상용 웹 브라우저 Netscape Navigator : 90% 점유율, 동적인 기능 프로젝트

#### JavaScript의 탄생(1995)

Brendan Eich 웹의 동적 기능 개발을 넘어 스크립트 언어를 Mocha를 개발
java의 명성에 기대보고자 JavaScript로 이름 변겅
Netscape Navigator 2.0 탑재

#### JavaScript 파편화(1996)
인터넷 익스플로러(IE) 3.0에 JScript 도입 

#### 1차 브라우저 전쟁(1995-2001)
Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
모질라 재단 = MDN

#### 1차 브라우저 전쟁의 영향
웹 표준의 부재 -> 웹 표준의 중요성을 인식하는 계기가 됨
##### 웹 표준이 중요한 이유
브라우저나 기기에 상관없이 웹사이트가 동일하게 작동해야한다. 
브라우저별 코드를 따로 작성할 필요가 없다

#### ECMAScript 출시 (1997)
JavaScript의 파편화를 막기 위해 Netscape사는 ECMA 재단(정보 통신 시스템을 위한 국제적 표준화 기구)에 웹 표준 제작을 요청
표준 언어를 정의하여 발표, JavaScript는 ECMAScript 표준 기반

#### 2차 브라우저 전쟁(2004-2017)
IE는 웹 표준을 지키지 않았고 독자적인 규격을 유지하며 웹 시장을 주도

#### Chrome 브라우저의 등장 (2008)
Chrome 브라우저 출시
Firefox의 점유율을 점어서고 반년 뒤 IE의 점유율을 넘어섬

#### Chrome이 시장 우위를 점하게 된 이유
1. 적극적인 웹 표준 준수 + 빠른 성능, 다양한 플랫폼 지원, Google 생태계 통합
2. 호환성
- 웹 표준을 준수함으로써 일관된 웹 페이지를 볼 수 있게 됨
- 다앙햔 플랫폼 및 기기에서 웹사이트가 일관되게 동작할 수 있음
3. 강력한 개발자 도구 - 웹 개발자를 위한 강력한 도구를 제공

#### 2차 브라우저 전쟁의 영향
웹 표준을 준수, 새로운 웹 기술을 적극적으로 채택함
Microsoft Edge, Whale -> Chronium (chrome backbone)

웹의 기술적 발전과 웹 표준의 중요성

V8 자바스크립트 엔진 - 압도적인 성능

### ECMAScript

#### ECMAScript
표준화된 스크립트 프로그래밍 언어 명세
규칙, 세부사항 등을 정의

#### ECMAScript와 JavaScript
JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
명세를 기반으로 웹 브라우저나 Node.js와 같은 환경에서 실행

#### ECMAScript의 역사
ES5 안정성 생상성 높임
ES6 객체지향 프로그래밍 언어로써 많은 발전을 이루었다

#### JavaScript의 현재와 미래
Node.js 서버 사이드 개발에도 사용된다