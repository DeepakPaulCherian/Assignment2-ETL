# Assignment2-ETL
The assignment is to:-
- Use Python to access the API links and download the JSON data to local directory.
- Convert JSON to CSV (flatten nested data).
- Load CSV file into a Database (locally hosted).
- Run SQL Queries with joins and such to get the answers for Objectives.

### Objectives:-
The object of this assignment is to find the SQL queries for the following objectives.
- Find the user who made the LONGEST post.
- Find the post with MOST comments.
- Find the user with LEAST number of items pending in TODO.

### Resources:-
- https://jsonplaceholder.typicode.com/users -> All Users
- https://jsonplaceholder.typicode.com/posts -> Posts made by the user
- https://jsonplaceholder.typicode.com/comments -> Comments under post
- https://jsonplaceholder.typicode.com/todos -> [EXTRA] TO DO items created by user


## Steps Performed:
First , we perform the code in the file task2.py to convert the json data into csv form and to flatten the nested data. We then get 4 csv files. 
In pgAdmin, we create a database and create 4 tables with the same columns as that of the csv files that we converted.Then we copy the contents of the csv files into the tables in the database using copy command and then we perform the sql queries to get the solutions for the objectives.
The SQL queries used in this task are contained in the file SQL Queries.txt .


### Findings:
- Find the user who made the LONGEST post:-   **2,"Ervin Howell","Antonette"**
- Find the post with MOST comments:- **55,"sit vel voluptatem et non libero"**
- Find the user with LEAST number of items pending in TODO:- **8,"Nicholas Runolfsdottir V"**
