from pydantic import BaseModel, constr


class Post(BaseModel):
    title: constr(min_length=1, max_length=16)
    content: constr(min_length=1, max_length=256)


