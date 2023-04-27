# Dave
This is male measurements app. You can enter your body parameter and get your approx waist measurement list. If you don't find your waist measurement then you can even add it to it

**##HOW TO RUN**

**##SETTING DATABASE**

1. Install mongodb on local system and create user with a role of admin for the database **measures**.
2. You can refer this for creating user https://www.geeksforgeeks.org/create-user-and-add-role-in-mongodb/

**##BUILDING BACKENED**

1. The techstack is PYTHON , DJANGO AND MONGODB
2. Clone the repo , navigate to dave folder and create virtual env
3. Install django on the virtual env by the command `pip install django`
4. Install all the dependencies using `pip install -r requirements.txt`
5. Run the data alteration script using command `python3 dataAlterationScript.py`. This is will alter .csv data to json format
6. Replace the username and password in the file Dave/dave/measure/database/MongoConnection.py with your credentials.
7. Run the migration `python manage.py migrate` 
8. Run the migration script `python3 migrationScript.py`. This will add all the .csv data in the database
9. Now start the server by command `python3 manage.py runserver`
10. Your backened is ready!!!

**##BUILDING FRONTEND**

1. The techstack is REACTJS, CSS, BOOTSTRAP
2. Navigate to folder dave/frontend
3. Run the command `npm install` to install all dependencies
4. Now the build the frontend with the command `npm build`
5. Start the reactjs frontend with `npm start` command
6. Your frontend is live!!!

**START YOUR FUN**
