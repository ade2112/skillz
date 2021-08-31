from fastapi import FastAPI
from handler import Business, SignUp, Skill_up_africa, Login


app = FastAPI()




@app.post("/business")
def business(business: Business):
    return business

@app.post("/skillupafrica")
def skill_up_africa(skill:Skill_up_africa):
    return skill
    
@app.post("/blog")
def blog():
    pass

@app.post("/login")
def login(login:Login):
    return login

@app.post("/signup")
def signup(signup:SignUp):
    return signup