from fastapi import FastAPI, Form, HTTPException
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Establish the database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="dcmsdb"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    raise HTTPException(status_code=500, detail="Database connection error.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_dentistdata")
def get_dentistdata():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_dentist")
        records = cursor.fetchall()
        cursor.close()
        return records
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise HTTPException(status_code=500, detail="Failed to retrieve data.")

@app.post("/add_dentistdata")
def add_dentistdata(
    dfirstname: str = Form(...), 
    dlastname: str = Form(...), 
    speciality: str = Form(...),
    tel: str = Form(...),
    email: str = Form(...),
    empStatus: str = Form(...),
    password: str = Form(...)
):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tb_dentist (dfirstname, dlastname, speciality, tel, email, status, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
            (dfirstname, dlastname, speciality, tel, email, empStatus, password)
        )
        conn.commit()
        cursor.close()
        return {"message": "Added Successfully"}
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise HTTPException(status_code=500, detail="Failed to insert data.")

@app.post("/delete_dentistdata")
def delete_dentistdata(id: int = Form(...)):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_dentist WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        return {"message": "Deleted Successfully"}
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise HTTPException(status_code=500, detail="Failed to delete data.")
