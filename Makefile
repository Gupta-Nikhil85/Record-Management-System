#Makefile for the Record Management System

#Installation Target
install:
	pip install -r requirements.txt

#Database Initalization Target

initializeDB:
	python3 db_init.py

#Run Target
run:
	python3 frontend.py