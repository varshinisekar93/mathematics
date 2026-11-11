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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
