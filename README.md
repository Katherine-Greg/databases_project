##  Task 2:
### Create a Service Worker

Now we have a database with one large table, so we need to:
1. Design a table system that adheres to the third normal form.
2. Migrate the old database to the new structure.
3. Create a new database and deploy it from the previously created migration.
4. Populate new database.

For this task, we chose only one subject because of conflicts in the migration process.

For migrations, we use Django ORM.

Make sure that you add your environment variables to .env, also don`t forget to add your new database variables to settings.py

Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

Use following command to start program
```
python main.py
```
