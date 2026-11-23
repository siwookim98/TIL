#### Single Thread 언어, JavaScript
하나의 일만 수행할 수 있는 Single Thread
여러 작업을 처리할 수 없음
요청한 순서대로 처리할 수 밖에 없음
JavaScript 비동기 처리 어떻게 할 수 있을까?
multi-thread

### JavaScript Runtime
#### JavaScript Runtime
runtime = 환경

#### 브라우저 환경에서의 자바스크립트 비동기 처리 관련 요소
Call Stack
순서대로 쌓이는 작업 공간
single thread

web API
브라우저에서 제공하는 runtime 환경 - 팀

Task Queue - 박스
대기열

event loop

#### 런타임의 시각적 표현 (7)
call stack 나
web api 팀원
task queue 나의 검토

#### 정리 브라우저 환경에서의 자바스크립트 비동기 처리 관련 요소
call stack 함수 호출이 순서대로 쌓이는 작업 공간
web API 언제 실행될지 모르는 비동기 작업
Task Queue
Event Loop