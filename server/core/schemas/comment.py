from pydantic import BaseModel, constr


class Comment(BaseModel):
    content: constr(min_length=1, max_length=256)
