import imp
from urllib import response
from webbrowser import get
from fastapi import APIRouter, Depends, Response, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from..database import get_db
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
    )

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response , db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show_blog(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db)
