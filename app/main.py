from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Example",
    summary="This is a simple FastAPI example for beginners",
    version="0.0.0"
)

@app.get("/")
async def root():
    return {"message":"Hello World!"}

