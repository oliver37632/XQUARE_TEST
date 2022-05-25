from server.core.model import Base

from sqlalchemy import INTEGER, DATETIME, Column, VARCHAR, text


class Post(Base):
    __tablename__ = "post"

    id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR(16), nullable=False)
    title = Column(VARCHAR(16), nullable=False)
    content = Column(VARCHAR(256), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

