from fastapi import APIRouter, status, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from server.core.model import session_scope
from server.core.schemas.auth import Sign_up, Overlap
from server.utils.auth import create_user, id_overlap, login
from server import get_settings, Settings

app = APIRouter()


@app.post("/overlaps", status_code=status.HTTP_200_OK)
async def overlap(body: Overlap, settings: Settings = Depends(get_settings)):
    with session_scope(settings.MYSQL_DB_URL) as session:
        response = await id_overlap(username=body.username, session=session)

        return response


@app.post("/signups", status_code=status.HTTP_201_CREATED)
async def sign_up(body: Sign_up, settings: Settings = Depends(get_settings)):
    with session_scope(settings.MYSQL_DB_URL) as session:
        try:
            response = await create_user(username=body.username, password=body.password, session=session)
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username is overlap")

        return response


@app.post("/logins", status_code=status.HTTP_200_OK)
async def sign_in(body: Sign_up, settings: Settings = Depends(get_settings), authorize: AuthJWT = Depends()):
    with session_scope(settings.MYSQL_DB_URL) as session:
        response = login(session=session, username=body.username, password=body.password, authorize=authorize)

        return response