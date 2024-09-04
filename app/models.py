# Here all the models are defined(also known as the database talbe and or  somehting like that)
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import null,text
from sqlalchemy.orm import relationship


from .database import Base

# Creating a table for the database
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    tittle = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,
                        server_default=text("now()"))
   
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE")
                ,nullable=False)

    owner = relationship("User")
    


# So whenever the application starts the code above will chech for 
# any mentioned database if its there it will not do anything
# else it will create it 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,
                        server_default =text("now()"))
    

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    



