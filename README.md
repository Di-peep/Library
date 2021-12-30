
# Library of hospital
This is a web application for managing departments and
employees of hospital. It uses a RESTful web service to perform crud 
operations. The app allows you to:  
- enter as admin to get all privileges
- display a list of departments and the average salary
calculated automatically for these departments  
- display a list of employees in the departments 
with an indication of the salary for each employee 
and a search field to search for employees born on a
 certain date or in the period between dates
 - create, update and delete the departments and the
 employees if user is admin
 
 
 
 #### Set up the database
 MySql must be installed. Go to the mysql console,
  login as root and create a new user:  
 ```CREATE USER *user* IDENTIFIED BY *password*```  
 Create a database for the app:  
 ```CREATE DATABASE IF NOT EXISTS hospital_app```  
 Grant all the privileges on the created database to the user:  
 ```GRANT ALL PRIVILEGES ON hospital_app . * TO '*user*'@'localhost'```  
 Replace the \*user* and the \*password* with your own values
 
 #### Set the environmental variables
 For Windows:  
```set FLASK_APP=run.py```  
```set FLASK_CONFIG=*config*```   
```set SECRET_KEY=*secret_key*```  
```set DB_URL=mysql+pymysql://*user*:*password*@localhost/hospital_app```  
 
 
Replace the \*config* with one of the values: *development*,
 *production*, *testing*


 
 #### Run the migration scripts to create database schema
 Run the following commands:  
 ```flask db migrate```  
 ```flask db upgrade```
 

 
 ### Everything is ready! Run the app
 To launch the app just run:  
 ```flask run```
 

 
  


 #### Here is the list of available addresses of web application:

    
 #### Departments

 - /departments - display all the departments
 - /departments/add - add a new department
 - /departments/edit/*id* - edit a department with a specified id 
   
   
#### Employees

 - /employees - display all the employees
 - /employees/add - add a new employee
 - /employees/edit/*id* - edit an employee with a specified id 

    

#### General

 - /home - home page
   
#### Admin

 - /profile - display admins profile
 - /login - login as admin
 - /logout - logout from current accaunt

