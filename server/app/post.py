from fastapi import APIRouter, status, Depends
from fastapi_jwt_auth import AuthJWT

from server.core.model import session_scope
from server.core.schemas.post import Post
from server.utils.post import create_post, see_more_post, get_post_list, edit_post, delete_post
from server.utils.security import token_check
from server import Settings, get_settings

app = APIRouter()


@app.post("", status_code=status.HTTP_201_CREATED)
def write_post(body: Post, settings: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(settings.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()
        response = create_post(title=body.title, content=body.content, username=username, session=session)

        return response


@app.get("/{post_id}", status_code=status.HTTP_200_OK)
async def get_post(post_id: int, settings: Settings = Depends(get_settings)):
    with session_scope(settings.MYSQL_DB_URL) as session:
        return await see_more_post(post_id=post_id, session=session)


@app.get("", status_code=status.HTTP_200_OK)
async def all_get_post(settings: Settings = Depends(get_settings)):
    with session_scope(settings.MYSQL_DB_URL) as session:
        return await get_post_list(session=session)


@app.put("/{post_id}", status_code=status.HTTP_201_CREATED)
async def update_post(post_id: int, body: Post, setting: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(setting.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()

        return await edit_post(title=body.title, content=body.content, post_id=post_id, username=username, session=session)


@app.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(post_id: int, settings: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(settings.MYSQL_DB_URL) as session:
        token_check(authorize=authorize, type="access")
        username = authorize.get_jwt_subject()

        return await delete_post(post_id=post_id, username=username, session=session)



