from fastapi import FastAPI
from Core.config import setting
app=FastAPI(title=setting.PROJECT_TITLE,version=setting.PROJECT_VERSION)
