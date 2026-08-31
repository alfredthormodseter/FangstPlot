from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class PolygonRequest(BaseModel):
    coordinates: list

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/catches")
def get_catches():
    return {"catches": []}

@app.post("/create-grid")
def create_grid(polygon: PolygonRequest):
        //Lag grids etter omrissing

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)