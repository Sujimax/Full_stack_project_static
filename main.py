from fastapi import FastAPI
from database import engine, Base
from router.user_complaint import user_complaint
from router.admin import admin_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Complaint Management API")

Base.metadata.create_all(bind=engine)

app.include_router(user_complaint)
app.include_router(admin_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
