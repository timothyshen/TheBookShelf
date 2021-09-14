# TheBookShelf
The BookShelf project

# Get your Django running

## Before any action
Add the environment 
use `pip install requirements.txt` to install all the dependencies.


## Intergrating Django
1. Check if all the <app_name>/migration folder contain migration
2. If so delete them else jump to 3
3. Add SQLite db.sqlite3 to the database, here I am using Pycharm
4. run this `python manage.py makemigration` - make the migration records
5. `python manage.py migrate` - migrate the changes
6. `python manage.py runserver` - start server
7. `python manage.py createsuperuser` - for superuser
