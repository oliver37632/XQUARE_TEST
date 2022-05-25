from server.core.model import Base

from sqlalchemy import Column, VARCHAR, INTEGER, DATETIME, text


class Comment(Base):
    __tablename__ = "comment"

    id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR(16), nullable=False)
    content = Column(VARCHAR(256), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

