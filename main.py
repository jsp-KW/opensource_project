from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
from typing import List

import uvicorn

app = FastAPI()

# Templates 설정
templates = Jinja2Templates(directory='templates')

# Static 파일 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# BaseModel 정의
class Comment(BaseModel):
    name: str
    msg: str
    time: str
    comment_id:str

comments_li: List[Comment] = []  # Comments 객체들을 저장할 리스트 생성
comment_id =0
#cm_count = 0

# 루트 경로
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# about.html  get 방식
@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


# email.html get 방식
@app.get("/email", response_class=HTMLResponse)
async def read_email(request: Request):
    return templates.TemplateResponse("email.html", {"request": request})


# 현재까지 작성되어있는 방명록을 렌더링하는 백엔드단 구현
# 방명록 작성자 이름, 작성자 내용, 작성시간 정보 가져오기.
@app.get("/comments")
async def get_comments():
    return comments_li




@app.post("/add_comment")

async def add_comment(comment: Comment):
   # global cm_count
    global comment_id
    #cm_count += 1
   
  
    comments_li.append(comment)

    print("comments_li 출력", comments_li)

    return {"message": "Comment가 성공적으로 작성되었습니다.","coment_id": comment.comment_id}



# 방명록 삭제
@app.delete("/del_comment/{comment_id}")
async def del_comment(comment_id: str):
    global comments_li
    deleted_index = -1  # 삭제할 댓글의 인덱스를 추적하기 위한 변수 초기화
    for i, comment in enumerate(comments_li):
        if comment.comment_id == comment_id:
            deleted_index = i  # 삭제할 댓글의 인덱스를 저장
            break

    if deleted_index != -1:
        del comments_li[deleted_index]  # 저장된 인덱스의 댓글을 삭제
        return {"message": "Comment 삭제가 완료되었습니다."}
    else:
        return {"message": "삭제할 Comment를 찾을 수 없습니다ㅠㅠ."}




if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5500, reload=True)
