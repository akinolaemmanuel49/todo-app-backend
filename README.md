# TODO APP BACKEND

This is a simple backend application for a Todo Web App.

# How to launch this project on your local machine.

First you have to clone this repository, you can do this by typing in the command below into your terminal

> `git clone https://github.com/KrazyKahunaGuy/todo-app-backend.git`

> `cd todo-app-backend`

If you intend on using poetry to manage your dependencies you can run the following commands to install the required dependencies and run the project. Ensure these commands are run from the projects root directory.

> `poetry install`

> `poetry shell`

> `poetry run uvicorn todo.api_v1.main:app`

If you intend on using the `requirements.txt` file to set up the environment for the project run the following commands.

> `virtualenv venv`

> `source venv/bin/activate`

> `pip install -r requirements.txt`

> `uvicorn todo.api_v1.main:app`

This project makes use of a postgresql database to store data and cloudinary to to images. You'll need to set up and provide the connection string and required values for the project in the example.env file.
Rename the example.env file to simply .env after filling in the missing values.

> <a href="https://cloudinary.com">CLOUDINARY</a> Visit the cloudinary website to create an account and get an API key if you do not already have one.

> This <a href="https://cloudinary.com/documentation/how_to_integrate_cloudinary">LINK</a> provides some helpful information on integrating cloudinary with your code
