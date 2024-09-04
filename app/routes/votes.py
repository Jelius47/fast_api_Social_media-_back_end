from fastapi import APIRouter,FastAPI,status,HTTPException,Depends,Response
from sqlalchemy.orm import Session
from .. import schema,database,models
from . import oath2

router = APIRouter(
    prefix="/votes",
    tags=["Vote"]
)  

@router.post("/",status_code=status.HTTP_201_CREATED)

def vote(vote: schema.Vote,db: Session = Depends(database.get_db),current_user: int = Depends(oath2.get_current_user)):
    found_vote = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    if (vote.dir == 1):
        if found_vote.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id,user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote does not exist")

        found_vote.delete(synchronize_session=False)
        db.commit()
