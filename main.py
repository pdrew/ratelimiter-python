from fastapi import FastAPI

app = FastAPI()

@app.get("/limited")
async def limited():
    return { "type": "limited" }

@app.get("/unlimited")
async def unlimited():
    return { "type": "unlimited" }