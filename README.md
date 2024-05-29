# 활용한 오픈소스 링크

- google font
- https://fonts.googleapis.com
- bootstrap
- https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css
- opensource software lecture note /박규동 교수님/강의자료/
- favicorn

# option 구현
 - 방명록 기능 fastapi 를 통하여 작성자, 작성내용, 작성시간을 구현했습니다.
 - 삭제하는 기능은 자유로우며, 삭제시 fastapi를 통해 javascript 에서 일렬번호를 부여하는 함수를 생성하여,
 - 일렬번호를 넘겨주고, 백엔드단 (fastapi)에서 해당하는 일렬번호를 가지고 있는 방명록의 내용을 삭제합니다. 
 - 삭제할 댓글의 인덱스를 저장하여, del함수를 통해 삭제 합니다.

# 구현시 참고, 참고(?) 했던 내용들
- Jinja2Templates 모듈을 통하여, Templates 폴더를 생성후, html 파일을 구성하는 이미지파일, 오디오 파일, css 파일을 관리하였습니다.
- main.py 를 통해, 각 html 파일들에 따른 get 방식을 정의하였고, 추가적으로 현재까지 추가되어있는 방명록들을 가져오는 기능을 구현
- BaseModel을 정의하여 방명록 구성요소인 작성자 이름, 메세지 내용, 작성시간, 일렬번호를 js 프론트엔드단에서 가져옴으로써 처리하기 위해 작성하였습니다.
- 방명록 작성 함수를 js에 정의하고, main.py에 post 방식으로 정의후, append 함수를 통해 작성된 방명록을 list 형태로 append
- 방명록 삭제 기능의 로직을 구현하기 위한 새로운 방법을 구안-> 빅데이터 프로그래밍 수업때 배운 랜덤번호 부여 예제를 기반으로 일렬번호를 작성하는 함수를 작성하여 방명록에 따른 랜덤일렬번호 부여.
- Aws instance 의 인바운드 규칙을 통해, port 5501 번을 추가함으로써 특정 port 번호로 배포되도록 설정
- 작성시간은 datetime 을 통하여 만들수 있음을 구글링을 통해 학습
- nginx +fastapi 기반 배포
- http://34.204.152.39:5501/ 를 통해 접속가능
