# Record Management System

Record Management System is a software program that helps in managing student records. This program is written in Python, and the main objective is to provide the user with a user-friendly Graphical User Interface (GUI). For this purpose, the program uses the Tkinter library, which is the most commonly used library for creating GUI-based software. The MySQL database has been used as the backend technology for storing data.
## Software Requirements

To run this program, the following software needs to be installed on the system:

- Python 3.x
- Tkinter Library
- mysql-connector
- MySQL Server
- python-dotenv

## How to Run the Program

To run the program, follow the steps given below:

1. Clone the repository or download the source code from the repository [here](https://github.com/Gupta-Nikhil85/Record-Management-System).
2. Open the command prompt or terminal.
3. Navigate to the directory where the source code is saved.
4. Run the following command to install the required libraries and creating the database:
```bash
pip install --upgrade pip
pip --version
make install
make initializeDB
```

## Usage
- Setup the .env file.
```bash
Host=localhost
User=<your username>
Password=<your password>
```
- Run the project: 
```bash 
make run
```
- Use the Tkinter GUI to perform all the CRUD operations on the data.

- Once the program is up and running, the user can perform the following tasks:

1. Add student records
2. View all student records
3. Update student records
4. Delete student records
5. Search for a student record

## Conclusion
The Record Management System is a simple yet effective software program for managing student records. It provides a user-friendly interface that allows users to easily add, view, update, and delete student records. The program uses MySQL as the backend technology for storing data, which ensures data security and reliability. Overall, this program can be a useful tool for educational institutions and other organizations that need to manage student records.

Currently, the project is storing minimal amount of data, more tables can be added with improved by adding multiple tables with normalization.

## Contributions

Contributions are welcome! If you would like to contribute to this project, please create a fork, make your changes, and submit a pull request.