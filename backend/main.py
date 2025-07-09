from fastapi import FastAPI
from routes.auth import router as auth_route
from routes.company import router as comapines_route
from routes.contact import router as contact_route
from config.databse import Base,engine

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


app.include_router(auth_route,prefix="/api",tags=["auth"])
app.include_router(comapines_route,prefix="/api",tags=["company"])
app.include_router(contact_route,prefix="/api",tags=["contact"])

@app.get("/health")
def health():
    return {"message":"healthy"}