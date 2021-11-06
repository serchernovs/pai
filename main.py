import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

class Robot(BaseModel):
    name: str

robots = [
    Robot(name="petia"),
    Robot(name="sania"),
    Robot(name="maria"),
]

@app.get("/robots")
def list_robots():
    return robots

@app.post('/robots')
def create_robot(new_robot: Robot):
    robots.append(new_robot)
    return "created new robot"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
