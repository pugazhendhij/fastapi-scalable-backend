from fastapi import FastAPI

app = FastAPI(title="FastAPI Scalable Backend")

@app.get("/")
async def root():
    return {"message":"Hello FastAPI"}