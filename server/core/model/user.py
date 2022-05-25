from server.core.model import Base
from server.core.model.post import Post

from sqlalchemy.sql.schema import Column
from sqlalchemy import VARCHAR, CHAR
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    username = Column(VARCHAR(16), primary_key=True)
    password = Column(CHAR(63), nullable=False)




