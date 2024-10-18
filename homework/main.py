from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI()

class calculating_machine(BaseModel):
    # sign은 연산자의 종류를 지정하며, Literal로 +, -, *, %, ^, // 만 허용
    sign: Literal["+", "-", "*", "%", "^", "//","/"]
    num1: int = Field(...,description='숫자를 입력해주세요')
    num2: int = Field(...,description='숫자를 입력해주세요')


def calculate(sign: str, num1: int, num2: int):
    if sign == "+":
        return {"+": num1 + num2}
    elif sign == "-":
        return {"-": num1 - num2}
    elif sign == "*":
        return {"*": num1 * num2}
    elif sign == "%":
        return {"%": num1 % num2}
    elif sign == "/":
        return {"/": num1 / num2}
    elif sign == "//":  # 몫과 나머지 연사
        return {"몫": num1 // num2, "나머지": num1 % num2}
    elif sign == "^":  # 거듭제곱 연산
        return {"^": num1**num2}
    else:
        raise HTTPException(status_code=400, detail="다시 입력해주세요. :(")

# 연산 기록을 저장하는 리스트
operation_history = []

@app.post("/")
async def post_T(request: calculating_machine):

    sum = calculate(request.sign, request.num1, request.num2)
    # 연산 결과를 history에 저장
    operation_history.append(f"{request.num1} {request.sign} {request.num2} = {sum}")
    return sum

@app.get("/history")
async def get_history():
    # operation_history 리스트에 저장된 모든 연산 기록 출력
    return operation_history
