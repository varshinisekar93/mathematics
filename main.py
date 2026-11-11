from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Mathematics API")


class AdditionRequest(BaseModel):
    a: float = Field(..., allow_inf_nan=False)
    b: float = Field(..., allow_inf_nan=False)


class AdditionResponse(BaseModel):
    a: float
    b: float
    result: float


def add_numbers(a: float, b: float) -> AdditionResponse:
    import math
    from fastapi import HTTPException

    result = a + b
    if not math.isfinite(result):
        raise HTTPException(status_code=422, detail="The addition result is too large.")
    return AdditionResponse(a=a, b=b, result=result)


@app.post("/add", response_model=AdditionResponse)
def add_post(numbers: AdditionRequest):
    return add_numbers(numbers.a, numbers.b)


class SubtractionRequest(BaseModel):
    a: float = Field(..., allow_inf_nan=False)
    b: float = Field(..., allow_inf_nan=False)


class SubtractionResponse(BaseModel):
    a: float
    b: float
    result: float


@app.post("/subtract", response_model=SubtractionResponse)
def subtract_post(numbers: SubtractionRequest):
    import math
    from fastapi import HTTPException

    result = numbers.a - numbers.b
    if not math.isfinite(result):
        raise HTTPException(status_code=422, detail="The subtraction result is too large.")
    return SubtractionResponse(a=numbers.a, b=numbers.b, result=result)


class MultiplicationRequest(BaseModel):
    a: float = Field(..., allow_inf_nan=False)
    b: float = Field(..., allow_inf_nan=False)


class MultiplicationResponse(BaseModel):
    a: float
    b: float
    result: float


@app.post("/multiply", response_model=MultiplicationResponse)
def multiply_post(numbers: MultiplicationRequest):
    import math
    from fastapi import HTTPException

    result = numbers.a * numbers.b
    if not math.isfinite(result):
        raise HTTPException(status_code=422, detail="The multiplication result is too large.")
    return MultiplicationResponse(a=numbers.a, b=numbers.b, result=result)


class DivisionRequest(BaseModel):
    a: float = Field(..., allow_inf_nan=False)
    b: float = Field(..., allow_inf_nan=False)


class DivisionResponse(BaseModel):
    a: float
    b: float
    result: float


@app.post("/divide", response_model=DivisionResponse)
def divide_post(numbers: DivisionRequest):
    import math
    from fastapi import HTTPException

    if numbers.b == 0:
        raise HTTPException(status_code=422, detail="Cannot divide by zero.")
    result = numbers.a / numbers.b
    if not math.isfinite(result):
        raise HTTPException(status_code=422, detail="The division result is too large.")
    return DivisionResponse(a=numbers.a, b=numbers.b, result=result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
