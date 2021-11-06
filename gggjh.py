import fastapi
import uvicorn

app = fastapi.FastAPI()

robot =[
    "petia",
    "sania",
    "maria",
 ]

@app.get("/robot")
def list_robot():
    return robot

@app.post('/bistro_vel')
def bistro_vel():
    return"vel_bistro"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
