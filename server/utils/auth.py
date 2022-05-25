import bcrypt

from server import get_settings
from server.core.model.user import User
from server.utils.security import verify_password

from fastapi import HTTPException, status, Depends
from fastapi_jwt_auth import AuthJWT

from sqlalchemy.orm import Session

settings = get_settings()


async def id_overlap(username: str, session: Session):
        user = session.query(User).filter(User.username == username).scalar()

        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username is overlap")
        return {
            "message": "Available username"
        }


async def create_user(username: str, password: str, session: Session):
        session.add(User(
            username=username,
            password=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        ))

        session.commit()

        return {
            "message": "success"
        }


def login(session: Session, username: str, password: str, authorize: AuthJWT = Depends()):
    user = session.query(User).filter(User.username == username)

    if not user.scalar():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email does not exist")

    user = user.first()
    if not verify_password(plain_password=password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong password")

    access_token = authorize.create_access_token(subject=user.username)

    return {
        "access_token": access_token
    }