from pydantic import BaseModel, constr


class Comment(BaseModel):
    post_id: constr(min_length=1, max_length=16)
    content: constr(min_length=1, max_length=256)
