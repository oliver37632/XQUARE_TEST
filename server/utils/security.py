from server import get_settings

from fastapi import HTTPException, status, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AccessTokenRequired, RefreshTokenRequired, JWTDecodeError, MissingTokenError
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from server.core.model.user import User
from server.core.model.post import Post
from server.core.model.comment import Comment
from server.core.model import session_scope

from jose import jwt, JWTError

from datetime import datetime

from passlib.context import CryptContext

settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def token_check(authorize: AuthJWT, type: str):
    try:
        if type == "access":
            authorize.jwt_required()
        elif type == "refresh":
            authorize.jwt_refresh_token_required()
        else:
            raise ValueError
    except ValueError:
        raise ValueError
    except AccessTokenRequired:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="access token required")
    except RefreshTokenRequired:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="refresh token required")
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token has expired")
    except MissingTokenError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="token not found")


def check_post(username: str, post_id: int, session: Session):
    post = session.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this post is not found")

    if post.username == username or username == "admin":
        return post

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The user is not valid")


def check_comment(username: str, comment_id: int, session: Session):
    comment = session.query(Comment).filter(Comment.id == comment_id).scalar()

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this comment is not found")

    if comment.username == username or username == "admin":
        return comment

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user is not valid")


def token_check(authorize: AuthJWT, type: str):
    try:
        if type == "access":
            authorize.jwt_required()
        elif type == "refresh":
            authorize.jwt_refresh_token_required()
        else:
            raise ValueError
    except ValueError:
        raise ValueError
    except AccessTokenRequired:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="access token required")
    except RefreshTokenRequired:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="refresh token required")
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token has expired")
    except MissingTokenError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="token not found")
