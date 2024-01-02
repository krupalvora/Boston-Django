# Boston-Django

pip install django-cors-headers
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

API Endpoints:
1. Task1(root route) : http://127.0.0.1:8000/
2. Task2(RESTful API) : 
    a. Post request http://127.0.0.1:8000/add_book
    {"book_id":"2","author":"Ravi kant",        "book_name":"rich dad","price":200}

    b. Fetch books http://127.0.0.1:8000/get_books
3. Task3(Database Interaction) : Get spefic book http://127.0.0.1:8000/get_book/1
4. Task4(Authentication) : Login post req http://127.0.0.1:8000/api/login/
{"username": "krupal", "password": "1234"}
5. Task5(Video Generation): Rotate video by passed angle in url http://127.0.0.1:8000/rotate_video/90/
## Screenshots
Get Books![Get Books](https://raw.githubusercontent.com/krupalvora/Boston-Django/main/media/get_books.png)
Authentication
![Authentication](https://raw.githubusercontent.com/krupalvora/Boston-Django/main/media/login.png)

