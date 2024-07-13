# Python--FastAPI
Welcome to the CRUD FastAPI Project! This repository contains a simple web API built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.
FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It's designed to be easy to use and to provide automatic interactive API documentation. FastAPI is known for its speed, efficiency, and ease of development, making it a popular choice for creating robust and scalable web applications and microservices. It supports asynchronous programming, dependency injection, and data validation, allowing developers to build secure and performant APIs quickly.

# Features
* FastAPI: Utilizes FastAPI for building APIs quickly and efficiently.
* Automatic interactive API documentation: Integrated Swagger UI and ReDoc.
* Asynchronous support: Efficient handling of asynchronous tasks.
* Type hints: Utilizes Python type hints for data validation and editor support.

# Requirements
* Python 3.7+
* FastAPI
* Uvicorn (ASGI server)

# Installation
1. Clone the repository:
   `git clone https://github.com/sriayush02/Python--FastAPI.git`
   `cd Projects`

2. Create and activate a virtual environment:
   `python -m venv env`
   `source env/bin/activate` (On Linux)
   `env\Scripts\activate`    (On Windows)

3. Install the required dependencies:
   `pip install -r requirements.txt`

# Usage
1. Run the application:
   `uvicorn main:app --reload`

2. Open your browser and navigate to http://127.0.0.1:8000 to access the API.

3. Explore the automatic interactive API documentation at http://127.0.0.1:8000/docs (Swagger UI) and http://127.0.0.1:8000/redoc (ReDoc).


# FastAPI/docs(Interface)
![main page](https://github.com/user-attachments/assets/be7ecc8e-cfb7-4689-8887-c2bc8d8f90da)

# GET Method
The GET method is used to retrieve data from the server. It's a read-only operation that does not modify any server data. In FastAPI, the @app.get decorator is used to define a GET endpoint.
![GET](https://github.com/user-attachments/assets/4ccf3ba2-f955-4399-80db-4ccd4f5a2f83)

# POST Method
The POST method is used to send data to the server to create a new resource. It's typically used for operations that involve creating or submitting data. In FastAPI, the @app.post decorator is used to define a POST endpoint.
![post1](https://github.com/user-attachments/assets/dce83087-9991-4c3a-b8f5-bd1aed5b2f36)
![post2](https://github.com/user-attachments/assets/89a4c019-946e-4f2e-9ec2-0321d338e01a)

# PUT Method
The PUT method is used to update an existing resource on the server. It's idempotent, meaning that multiple identical requests should have the same effect as a single request. In FastAPI, the @app.put decorator is used to define a PUT endpoint.
![put1](https://github.com/user-attachments/assets/8e1ca380-d271-4e32-9f80-b0117abd64ff)
![put2](https://github.com/user-attachments/assets/72105611-8687-4ffe-9dd2-86fd44e3590a)

# DELETE Method
The DELETE method is used to delete a resource from the server. In FastAPI, the @app.delete decorator is used to define a DELETE endpoint.
![del](https://github.com/user-attachments/assets/fc50a2e5-1b86-4e55-a9d6-77e48cc7fd30)







