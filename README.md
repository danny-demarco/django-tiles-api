# Django REST API technical challenge

## Summary 

This project is a fun technical challenge to create a Django project that includes some database design and construction of an API. The requirements are to:


Django plays a big role in abstracting away the need to deal with database management. However, this means as developers we have to make good choices about what structures and data our models contain and how they are related to enable the ORM to work most efficiently.

In our research software we have task objects that a user has to complete, each task has a title, an order field, a description and a type (such as survey, discussion, diary). We group tasks together in a container which we call a tile. Each tile has a launch date and a status. The status can be either live, pending or archived. A tile can be made up of one or many tasks. A task can only belong to a single tile.

Therefore, this exercise is to create a Django 3.x project that contains task and tile models, configured as outlined above. We would also like you to create a simple API to allow interaction with these models with DRF (Django Rest Framework version 3.10), using the appropriate viewsets and serialisers provided by DRF. No frontend work is required for this task.

## Project Setup

This project has been built using Django version 3.2.18 and Django Rest Framework 3.10

Full details of all packages used during development can found in the included requirements.txt file

The solutions produced for the exercise can be found in the following locations:

`tile_app_api/models.py`
`tile_app_api/serializers.py`
`tile_app_api/views.py`
`tile_app_api/tests.py`


### Running this project on your machine

Install Python 3.11.0 + [python.org](https://www.python.org/downloads/)

install Django version 3.x [djangoproject.org](https://docs.djangoproject.com/en/4.0/intro/install/)

Change directory so you are located in:

`\django_tiles_api`

Run:

`python manage.py makemigrations`

This will create you a sqlite3 embedded database

`python manage.py migrate`

Will apply all migrations to the database

The application should now be ready for you to run the automated tests. Detailed in the Testing section below.

## Testing

Testing has been implemented with a series of automated tests located in 

`tile_app_api/tests.py` 

and can be run by first ensuring you are located in 

`\django_tiles_api` 

then running the following command:

`python manage.py test`


## Future Improvements

Further, more specific information could be obtained from the client as to the specific behaviour required upon changes to the database, for example the behaviour required on deletion of tile objects. It is also unclear what the field 'order' pertains to, so this needs to be clarified.