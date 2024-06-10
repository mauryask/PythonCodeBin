import chunk
from fastapi import FastAPI
from pydantic import BaseModel
from db_connection import execute_query, insert_data
from read_excel import read_excel
import time


class User(BaseModel):
    email: str
    password: str   

app = FastAPI()


@app.post("/login")
async def authenticate(user: User):
    query = "SELECT email, password FROM employee WHERE email=%s AND password=%s LIMIT 1"
    value = (user.email, user.password)
    cursor =  execute_query(query, value) 
    row = cursor.fetchone()
    if row is not None:
        return {"status" : "success", "message": "Login sucessful"}
    else:
        return {"status" : "failure", "message": "Login failed"}

@app.get("/insert")
async def insert():
    query = "INSERT INTO records (name, joiningdate) VALUES (%s, %s)"
    df = read_excel()
    batch_size=100
    for i in range(0, len(df), batch_size):
        try:
            batch = df.iloc[i:i+batch_size]  # Get a batch of rows
            data = batch.to_records(index=False).tolist()  
            insert_data(query, data)
        except:
            print(f"Error inserting chunk of rows")


        
    
    

    