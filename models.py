from pydantic import BaseModel


class EchoInput(BaseModel):
    name: str
    age: int
