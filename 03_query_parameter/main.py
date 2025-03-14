from fastapi import FastAPI

app = FastAPI()

@app.get('/teachers/')
async def print_teacher_num(num:int,name:str):
    return {f'{num} , {name}'}

# 쿼리 매개변수를 필수로 만들려면 기본값을 설정안하면 된다.
# 다양한 매개변수를 작성할 때, 매개변수는 이름으로 찾아지기 때문에 순서는 상관없다.

# 선택적 매개변수
from typing import Union

@app.get('/teacher/{teacher_id}')
async def print_teacher(
    teacher_id : int, #path parameter
    name: Union[str,None] = None # query parameter / optional
):
    # (조건문)name 값이 있으면 id , name 응답
    if name:
        return {f"teacher_id : {teacher_id} , teacher_name : {name}"}
    return {f"teacger_id : {teacher_id}"}

