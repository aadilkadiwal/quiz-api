.PHONY: run migrate deps sh db
FILENAME:= .appname
APPNAME:= `cat $(FILENAME)`

# target: run - Run a dev server on localhost:8000
run:
	manage runserver

# target: migrate - Migrate the database
migrate:
	manage makemigrations
	manage migrate	

# target: deps - Install dependencies from requirements file
deps:
	pip install -r requirements.txt
	pip install -e .

# target: sh - Open django extension's shell plus
sh:
	manage shell_plus

# target: db - Open Django DB shell 
db:
	manage dbshell
