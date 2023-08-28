# AccuknoxSocial

## Let's get started
This is a social media application(Backend) built with Django and Django Rest Framework

### Features/Functionalities
- Create User
- User Authorization
- Add Friends
- View Friends
- Search for Users

### Installation
- clone the repo from your Terminal/cmd using the command: ```https://github.com/glenveigas437/AccuknoxSocial.git```
- Make sure you have Docker installed in your local system.
  
If you do not have Docker installed you can run the same in your local system with the commands below.
- Create a virtual Environment
- Install the required libraries and modules: ```pip3 install -r requirements.txt```
- Populate the .env file with the configuration for PostgreSQL.
  Example:
  ```
  ENGINE = django.db.backends.postgresql
  DB_NAME = accuknox_social_db_local
  DB_USER = postgres
  DB_PASSWORD = password
  DB_HOST = localhost
  DB_PORT = 5432
  ```
  
- Also, Create a new DB for the same.
- Run the migrations command
  ```python manage.py makemigrations```
  ```python manage.py migrate```
- Run the Server: ```python manage.py runserver```

With Docker installed
- Run the Command: ```docker compose up -d db```
- Create the Build: ```docker compose build```
- Run: ```docker compose up```
- Open Docker Desktop and look for the running service under db you will see the container ID copy that and Go to your Terminal and hit command: ```docker inspect <container_id>``` (Replace <container_id> with the Container ID you have copied and scroll down to fetch the IP Address.
  <img width="1440" alt="Screenshot 2023-08-28 at 2 49 16 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/b2c8c1b9-8022-43d7-bf04-0c8fcb6bf4a6">
  <img width="1044" alt="Screenshot 2023-08-28 at 2 54 14 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/f196e163-e502-4bc8-bd02-a5b9dcf78d36">


- Now Open your Browser and go to [localhost:5050](http://localhost:5050/) and login wiht the credentials mentioned under pgadmin section of the docker-compose.yml file and create a new connection with the details mentioned under the db section of the docker-compose.yml file and in the host name enter the IP Address you fetched
  <img width="1440" alt="Screenshot 2023-08-28 at 2 59 12 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/0a680f10-2cb8-46e5-8846-00b269099f94">
  <img width="1440" alt="Screenshot 2023-08-28 at 2 59 17 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/860c2082-e072-4f5b-9294-9b3470298ff1">

 - You can see all the tables populated during migration
  <img width="1440" alt="Screenshot 2023-08-28 at 3 01 56 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/0fc8d5cc-f847-4b83-871e-1391166248cc">

Once you see the app is up and running you can play along with it.

## The IDs required in Adding Friends (User Id) and Accepting/Rejecting Friend Request (Friend Request ID) can be fetched from the Database via SQL queries

## Load the [Postman json](https://github.com/glenveigas437/AccuknoxSocial/blob/main/Accuknox%20Social.postman_collection.json) collection in Postman and you can work along with the urls 

## Functionalities
1) Sign Up
<img width="1440" alt="Screenshot 2023-08-27 at 11 31 15 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/92fa9914-bd77-438c-a7c6-e8da084506a4">

2) Login
<img width="1440" alt="Screenshot 2023-08-27 at 11 35 47 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/9900259a-2184-4dd4-9768-afd291bf6801">

Once you login with the right credentials(case insentivity handled)
A Token will be generated and that token needs to be added to the Headers Section
with key as ```Authorization``` value as ```token <token>```
This ensures the user is authenticated and only Authenticated users can access the APIs below.

<img width="1319" alt="Screenshot 2023-08-27 at 11 39 07 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/5674d15e-8a40-4541-821c-17c376c666b4">

3) Log Out
<img width="1440" alt="Screenshot 2023-08-27 at 11 48 16 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/52133c7e-55af-4a64-a7e9-7e955e303a52">


4) Add Friend
After loading a number of users you can also send friend requests to them and add them to your friends list subject to acceptance of your friend request by the recipient.
Cannot send more than 3 requests per minute
<img width="1440" alt="Screenshot 2023-08-27 at 11 46 02 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/d877db5a-9a28-45b1-92a7-cb419f8c923f">


6) Pending Friend Requests
   <img width="1440" alt="Screenshot 2023-08-27 at 11 58 13 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/8a54a99d-7288-4240-95ca-e2fb90463a40">

   - Accept Friend Request
   <img width="1440" alt="Screenshot 2023-08-27 at 11 57 26 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/6cd4e958-e705-47f7-b565-106c1a8290cf">

   - Reject Friend Request
   <img width="1440" alt="Screenshot 2023-08-28 at 12 01 55 AM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/d6d117c9-02d6-427f-bb04-963159c528e2">

   - Unauthorized Action
   <img width="1440" alt="Screenshot 2023-08-27 at 11 59 29 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/dd2e7fd3-ca35-4551-9637-82e110fe2fd7">

7) View Your Friends (Pagination Applied)
<img width="1440" alt="Screenshot 2023-08-27 at 11 59 29 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/8d6266da-2bba-4d2a-ba8e-656e727ccfc0">

8) View All Users and Search for Users
  - All Users
  <img width="1440" alt="Screenshot 2023-08-27 at 11 51 46 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/969efbd4-abf0-4798-bed4-bf86a35c8c8e">

  - Search Users
    - Search users containing a specific letter like 'j'
    <img width="1440" alt="Screenshot 2023-08-27 at 11 52 22 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/4509803b-4516-4efd-9190-a03f46c9916b">

    - Search with user's email (case insensitive)
    <img width="1440" alt="Screenshot 2023-08-27 at 11 52 46 PM" src="https://github.com/glenveigas437/AccuknoxSocial/assets/31877827/ef766f3b-cebd-4811-9479-20c52253e0ef">

    























