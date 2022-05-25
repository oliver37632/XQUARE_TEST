from fastapi import APIRouter

from server.app import auth, comment, post

api_router = APIRouter()

api_router.include_router(auth.app, prefix="/auths", tags=["auth"])
api_router.include_router(comment.app, prefix="/comments", tags=["comment"])
api_router.include_router(post.app, prefix="/posts", tags=["post"])