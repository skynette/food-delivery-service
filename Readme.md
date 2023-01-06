Welcome to the Food Delivery Service project!

## What is it?

This project is a food delivery service that allows customers to browse through available restaurants, view their menus, place orders, and track their delivery status. It also allows restaurant owners to manage their restaurant's menu, orders, and deliveries.

## How to run it

To run this project, you will need to have Python and Django installed on your machine.

1.  Clone the repository: `git clone https://github.com/skynette/food-delivery-service.git`
2.  Change into the project directory: `cd food-delivery-service`
3.  Create a virtual environment: `python -m venv env`
4.  Activate the virtual environment: `source env/bin/activate`
5.  Install the required dependencies: `pip install -r requirements.txt`
6.  Run the migration to set up the database: `python manage.py migrate`
7.  Create a superuser to access the admin panel: `python manage.py createsuperuser`
8.  Run the development server: `python manage.py runserver`

You should now be able to access the project at [http://localhost:8000/](http://localhost:8000/). The admin panel is located at [http://localhost:8000/admin/](http://localhost:8000/admin/).

## How to contribute

We welcome contributions to this project! If you have an idea for a feature or a bug fix, follow these steps:

1.  Fork the repository: `https://github.com/skynette/food-delivery-service.git`
2.  Create a new branch for your changes: `git checkout -b my-feature`
3.  Make your changes and commit them: `git commit -am 'Add my feature'`
4.  Push the branch to your fork: `git push origin my-feature`
5.  Create a new pull request from your fork.

Please follow the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) for Python code and the [Django coding style guide](https://docs.djangoproject.com/en/3.1/internals/contributing/writing-code/coding-style/) when contributing to this project.

Thank you for considering contributing to the Food Delivery Service project!