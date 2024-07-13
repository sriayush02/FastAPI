import fastapi
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests

app= FastAPI()

students ={
    1:{
        "name" : "Ayush",
        "age" : 22,
        "Course" : "Btech"
    }
}

class Student(BaseModel):
    name: str
    age : int 
    Course : str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age : Optional[int] = None
    Course: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First user"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

#@app.get("/get-by-name/{name}")
#ef get_student(name: str):
    name = request.args.get("name")
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        
    return {"Data" : "Not Found"}
        
    

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id]= student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id :int , student: UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    
    if student.name!=None:
        students[student_id].name= student.name

    if student.age != None:
        students[student_id].age=student.age

    if student.Course != None:
        students[student_id].Course= student.Course
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    del students[student_id]
    return {"Message" : "Student deleted succesfully"}


 




 
  


