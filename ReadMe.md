# Ten Coins Recruitment Test - Mark Muscat

### Prerequisites

Django and REST Framework dependencies were used and are required. Anaconda environment was created to run the project. 

```
Django version : 2.0.5
REST Framework version : 3.8.2
Python version : 3.6.5
```

### Implementation Check-List

##### Tasks Implemented Successfully

```
- categories app
- Basic Admin User
- /categories/ API POST EndPoint
- /categories/ API GET EndPoint
- Database Category model
- Category JSON Serializer
- GET request of Node and all available children nodes
- POST request of Node and children _shell_.
- Basic system unit tests
- Sample data implemented through Admin panel.

```

##### Tasks Attempted

```
- POST request of node children (Bug present when accessing child attributes).
- GET request of node parents (non-functioning).
- GET request of node siblings (non-functioning).
```

### Usage

```
_$cd into project directory_
 $python manage.py runserver  - _run the server_
 $python manage.py test - _run system unit tests_
 In Browser URL : 127.0.0.1:8000/categories/ - _Categories POST EndPoint_
 In Browser URL : 127.0.0.1:8000:categories/<id> - _Category specific GET EndPoint (id = 17 for sample data)_
```