# vue-router-structure

## vue cli를 통해 vue 프로젝트 만들기

1. 생성

```bash
$ vue create 프로젝트이름
```

2. 개발용 서버 돌리기(프로젝트 경로에 위치한 상태여야 합니다)

```bash
$ npm run serve
```

- 프로젝트를 git으로 clone한 경우

1. node_modules 설치

```bash
$ npm install
```

2. 개발용 서버 돌리기

```bash
$ npm run serve
```

## 파일구조

- node_modules/ : django의 venv와 같은 역할, 다운로드 받은 모듈파일이 들어있다.
- public/ : 최종 만들어질 html파일의 base가 들어있다.
- src/ : vue로 작업한 코드가 위치한 폴더
- src/assets : 사진 등 정적 파일 모음
- src/components : 컴포넌트들 모음
- src/router : 라우터 설정 파일 모음
- src/views : 라우터 별 화면 모음
- src/App.vue : (보통)최상위 컴포넌트
- src/main.js : 메인 뷰 세팅
- package.json : django의 requirements.txt, 패키지 리스트 모음, 설치되면 자동갱신