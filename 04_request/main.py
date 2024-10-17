from fastapi import FastAPI , Request

app = FastAPI()

@app.get('/items')
async def read_items(request : Request):
    # 클라이언트 ip
    host = request.client.host
    # request 객체로 확인 가능한 것
    # body() : 본문
    # headers : 헤더
    return {"client_host":host}

# request body
# 클래스타입으로 만들고, basemodel 을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working : bool
    name : str
    nickname : str
    
@app.post('/teachers')
async def teachers_info(teacher:Teacher):
    if teacher.nickname:
        return f'hello my name{teacher.name} , i working {teacher.is_working}, nickname {teacher.nickname}'
    return f'hello my name{teacher.name} , i working {teacher.is_working}'

# path_parameter
# query_parameter
# requestBody

# student_no : path_parameter 로 받고 int
# Student :  rquestBody (이름,나이)
# lecture_name : query_parameter

# student no , name , age , lecture_name 을 전부 출력하는 문자열로 return 해주는 api

from pydantic import BaseModel

class Student(BaseModel):
    name : str
    age : int
    
@app.post('/student/{student_no}')
async def teachers_info(
    student_no : int ,
    student:Student , 
    lecture_name : str):
    
    return f'student_no : {student_no} , name : {student.name} , age : {student.age} , lecture_name : {lecture_name}'

