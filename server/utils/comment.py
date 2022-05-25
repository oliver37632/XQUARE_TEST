from server.core.model.comment import Comment
from server.utils.security import check_comment

from sqlalchemy.orm import Session


async def create_comment(content: str, username: str, post_id: int, session: Session):
    session.add(Comment(
        content=content,
        username=username,
        post_id=post_id
    ))

    session.commit()

    return {
        "message": "success"
    }


async def delete_comment(comment_id: int, username:str, session: Session):
    comment = check_comment(comment_id=comment_id, username=username, session=session)

    session.delete(comment)

    return {
        "message": "success"
    }


async def edit_comment(comment_id: int, username: str, content: str, session: Session):
    comment = check_comment(comment_id=comment_id, username=username, session=session)

    comment.content = content

    return {
        "message": "success"
    }


