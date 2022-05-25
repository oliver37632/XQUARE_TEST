from server.core.model.post import Post
from server.core.model.comment import Comment
from server.utils.security import check_post
from server import get_settings

from sqlalchemy.orm import Session

settings = get_settings()


def create_post(title: str, content: str, username: str, session: Session):

    new_post = Post(
        title=title,
        content=content,
        username=username
    )

    session.add(new_post)
    session.commit()

    return {
        "message": "success"
    }


async def get_post_list(session: Session):
    posts = session.query(Post).all()

    return {"posts": [{
        "title": post.title,
        "content": post.content,
        "username": post.username,
        "created_at": post.created_at
    } for post in posts]}


async def see_more_post(post_id: int, session: Session):
    post = session.query(Post).filter(Post.id == post_id).first()
    comments = session.query(Comment).filter(Comment.post_id == post_id).all()

    return {
        "title": post.title,
        "content": post.content,
        "username": post.username,
        "created_at": post.created_at,
        "comment": [{
            "comment_id": comment.id,
            "content": comment.content,
            "username": comment.username,
            "created_at": comment.created_at
        }for comment in comments]
    }


async def edit_post(post_id: str, title: str, content: str, username:str, session: Session):
    post = check_post(post_id=post_id, username=username, session=session)

    post.title = title
    post.content = content

    return {
        "message": "success"
    }


async def delete_post(post_id: int, username: str, session: Session):
    post = check_post(post_id=post_id, username=username, session=session)

    session.delete(post)

    return {
        "message": "success"
    }
