# FastAPI
from fastapi import FastAPI
from config.openapi import custom_openapi

# My imports
from routes.users import router as user_router
from routes.tweets import router as tweet_router

# Initialize app
app = FastAPI()

# Includes
# app.include_router(auth_router, prefix='/auth')
app.include_router(user_router, prefix='/users')
app.include_router(tweet_router, prefix='/tweets')

# Custom OPEN API
app = custom_openapi(app)