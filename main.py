import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

robot =[
    "petia",
    "sania",
    "maria",
 ]

@app.get("/robot")
def list_robot():
    return robot

class NewRobot(BaseModel):
    name: str

@app.post('/bistro_vel')
def bistro_vel(new_robot: NewRobot):
    robot.append(new_robot.name)
    return "created new robot"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
