from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

#migrating the table
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)






# Project Key
# c0patb2o_EoNCnGc53LXtDM95TTpwDXpXaMqFtvyv
# Project ID
# c0patb2o