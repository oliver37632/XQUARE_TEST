from pydantic import BaseModel, constr


class Sign_up(BaseModel):
    username: constr(min_length=1, max_length=16)
    password: constr(min_length=8, max_length=8)


class Overlap(BaseModel):
    username: constr(min_length=1, max_length=16)

