from fastapi import APIRouter, status, Depends
from fastapi_jwt_auth import AuthJWT

from server.core.model import session_scope
from server.core.schemas.comment import Comment
from server.utils.comment import create_comment, delete_comment, edit_comment
from server.utils.security import token_check
from server import Settings, get_settings

app = APIRouter()


@app.post("/{post_id}", status_code=status.HTTP_201_CREATED)
async def write_comment(body: Comment, post_id: int, settings: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(settings.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()
        response = await create_comment(post_id=post_id, content=body.content, username=username, session=session)

        return response


@app.put("/{comment_id}", status_code=status.HTTP_201_CREATED)
async def update_comment(comment_id: int, body: Comment, setting: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(setting.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()

        return await edit_comment(comment_id=comment_id, content=body.content, username=username, session=session)


@app.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletes_comment(comment_id: int, settings: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(settings.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()
        response = await delete_comment(comment_id=comment_id, username=username, session=session)
        return response



