# AirBnB Clone Project
<img align="left" width="200" scr="https://www.digital.ink/wp-content/uploads/airbnb_logo_detail.jpg">

## Introduction

Welcome to the AirBnB Clone Project! In this project, you will embark on a journey to create a simplified version of the AirBnB website. The goal is to deploy a web application on a server that covers fundamental concepts of the higher-level programming track.
The outlined process below outlines how we approached each component of the application. It's essential to note that this was a step-by-step endeavor, meaning that certain elements might have become available before others in the course of the development.
<img align="left" width="200" scr="[https://www.digital.ink/wp-content/uploads/airbnb_logo_detail.jpg](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231009%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231009T080342Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e1279706a7055a5600940856273b06df37b4d893750a9c225673cb270b28b7f9)">

## Project Timeline

### Week 1: The Console
### Week 2: SQL database
### Week 3: Web Static
The complete project will be executed in 4 months and the timeline will be update weekly

#### 1.1 Console Creation

- Commandline interpreter to manipulate data without a visual interface, similar to a Shell.
- Functionalities:
  * creating objects via the console.
  * updating objects via the console.
  * destroying objects via the console.
- Implement storage and persistence of objects to a file (JSON file).

#### 1.2 Storage Abstraction

- Develop a powerful storage system that abstracts the storage and persistence of objects.
- The console will serve as a tool to validate the storage engine.
- Emphasize the importance of separating "storage management" from "model" to make models modular and independent.

### Web Static

#### 2.1 HTML/CSS L

- HTML/CSS structure of the application.
- Templates for each object that will be used in the web application.

#### 2.2 MySQL Storage

- Replace the file storage with a Database storage (MySQL).
- Map models to a table in the database using an Object-Relational Mapping (O.R.M.).

#### 2.3 Web Framework - Templating

- Web server in Python.
- Make HTML files dynamic by utilizing objects stored in a file or database.

### Web Dynamic and API

#### 3.1 RESTful API

- Expose all objects stored via a JSON web interface.
- Implement manipulation of objects via a RESTful API.

#### 3.2 Web Dynamic

- JQuery to load objects from the client side using your own RESTful API.

## Project Structure

### 4.1 Files and Directories

- **models directory:** Contains all classes used for the entire project. A class, called "model" in an Object-Oriented Programming (OOP) project, represents an object/instance.
- **tests directory:** Contains all unit tests.
- **console.py file:** The entry point of the command interpreter.
- **models/base_model.py file:** The base class of all models containing common elements, attributes (id, created_at, updated_at), and methods (save() and to_json()).
- **models/engine directory:** Contains all storage classes (using the same prototype), initially file_storage.py.

### 4.2 Storage

Persistency is crucial for a web application. The project will involve manipulating two types of storage: file and database. For now, the focus will be on file storage.

Why separate "storage management" from "model"? To make models modular and independent, allowing easy replacement of the storage system without recoding the entire codebase.

### 4.3 Serialization/Deserialization

- Objects/instances created/updated in the command interpreter will be saved in a file and restored when the program starts.
- Convert instances to a Python built-in serializable data structure using the method my_instance.to_json().
- Convert the data structure to a string (JSON format) using JSON.dumps().
- Deserialization involves reading a string from a file, converting it to a data structure (JSON.loads()), and then converting it back to an instance.

### 4.4 *args, **kwargs



### 4.5 datetime

- The datetime module is used to manipulate date and time in Python.
- Examples include creating an instance with the current date and time, performing manipulations, and storing instances in data structures.
- The strftime method is used to make datetime instances readable.

## Conclusion

The AirBnB Clone Project is a comprehensive learning experience covering essential concepts in higher-level programming. Follow the step-by-step guide, and by the end of the first year, you'll have a complete web application ready for deployment. Happy coding!
