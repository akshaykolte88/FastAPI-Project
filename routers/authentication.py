from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, token
from sqlalchemy.orm import Session
from..database import get_db
from blog import database, models
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user_credentials = db.query(models.User).filter(models.User.email ==  request.username).first()
    if not user_credentials:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid username')
    print(Hash.verify(user_credentials.password, request.password))
    if not Hash.verify(user_credentials.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid password')

    access_token = token.create_access_token(data={"sub": user_credentials.email})
    return {"access_token": access_token, "token_type": "bearer"}