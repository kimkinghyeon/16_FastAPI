from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI()


class calculating_machine(BaseModel):
    sign: Literal["+", "-", "*", "%", "^", "//"]
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
    elif sign == "//":  # 몫과 나머지 연사
        return {"몫": num1 // num2, "나머지": num1 % num2}
    elif sign == "^":  # 거듭제곱 연산
        return {"^": num1**num2}
    else:
        raise HTTPException(status_code=400, detail="잘 못 입력하셨습니다.")


@app.post("/")
async def post_T(request: calculating_machine):

    sum = calculate(request.sign, request.num1, request.num2)

    return sum
