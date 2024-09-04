from fastapi import FastAPI,Depends,Response,status,HTTPException,APIRouter
from typing import Optional,List

# For the pydantic schema
from ..schema import *
from . import oath2


# Database 
from ..database import engine,get_db
from .. import models
from sqlalchemy.orm import Session  

router = APIRouter(
     prefix="/posts",
     tags=["Posts"]
)

# The decorator is used to define a path operation.
@router.get("/",response_model=List[PostResponse])

def get_posts(db: Session = Depends(get_db),current_user: int =Depends(oath2.get_current_user),
              limit: int = 10,skip: int = 0,search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts""")
    # db_posts = cursor.fetchall()
    # print(db_posts)
    
    posts = db.query(models.Post).filter(models.Post.tittle.contains(search)).limit(limit).offset(skip).all()

    # Retrieving the posts/data from the databaase
    # cursor.execute("""SELECT * FROM posts""")
    # db_posts = cursor.fetchall()
    # print(db_posts)

    # return db_posts
    

    # We no longer need the code bellow because of the limit implementation
    # post = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    return posts


# @app.post("/createPost")
# def create_posts(post: dict = Body(...)):
#     print(post)
#     return {"newpost": post}

# now revelaging pydantic model for defining the schema of our data.
@router.post("/",status_code = status.HTTP_201_CREATED,)
def create_posts(post: PostCreate,db: Session = Depends(get_db),current_user: int =Depends(oath2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    # print(post)
    # print(post.dict())

    # post_dict = post.dict()
    # post_dict['id'] =  randrange(0,100000)

    # Adding more data in the list
    # my_post.append(post_dict)
    
    # # Inserting the data using the cursor by hard codding it
    # cursor.execute(""" INSERT INTO posts (title,content,publish) VALUES(%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published)) 
    # new_post = cursor.commit()
    # conn.commit()

    # return{"Data":new_post}


    # Creating a post using ORM method 




    # return {"newpost": post_dict}

# The order does really matter hence the bellow code brings conflicts with /posts/{id}

# @router.app.get('/posts/latest')

# def get_latest():
#     post_latest = my_post[len(my_post)-1]
#     return {"detail": post_latest}


# Getting posts of specific users
@router.get("/{id}",response_model=PostResponse) # This is the implementation of path params
# Getting the post by id 

# def get_posts_w_Id(id : int,response: Response,): #the validation process 
#     post = find_post(id)
#     # if not post:
#     #     response.status_code = status.HTTP_404_NOT_FOUND # Resetting the status code 

 
#     # print(post)
#     return {"Data":f"This is the new post you requested is {post}"}




def get_posts_w_Id(id : str,db:Session=Depends(get_db),current_user: int =Depends(oath2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id ==id)
    # print(post)





    # cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
    # test_post = cursor.fetchone()

    # post = find_post(id)
    if post.first() == None:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                               detail=f"""Sorry CUDA DON'T COME HERE AGAIN the post with id :{id} was not found !!""")
    if post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    return post.first()
  





@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    # Deleting a post 
    # Finding the index
    # index = find_post_indx(id)
    # cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING * """,str(id))
    # deleted_post = conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""Sorry CUDA DON'T COME HERE AGAIN the post with id :{id} was not found !!""")
    
    if post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post.delete(synchronize_session=False)
    db.commit()
    # my_post.pop(index)
    # return {"The remained posts ": my_post}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}')
def update_info(id: int,post : PostCreate,db:Session=Depends(get_db),current_user: int =Depends(oath2.get_current_user)):
    # cursor.execute("""UPDATE posts SET tittle=%s,content=%s,published=%s WHERE id=%s RETURNING * """,
    #                (post_update.tittle,post_update.content,post_update.published,post_update.id))
    # post = cursor.fetchone()
    # conn.commit()
    # index = find_post_indx(id)
    post = db.query(models.Post).filter(models.Post.id ==id)
    post.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} was not found !!")
    
    if post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    
    post.update(post.model_dump(),synchronize_session=False) 
    db.commit()
    
    
    # post_dict = post_update.dict()
    # post_dict["id"] = id
    # my_post[index] = post_dict

    
    return {"Message": f"Successfully updated the new post is {post.first()}"}


