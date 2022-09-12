import sqlite3
import os
import time
from _print import _print_welcome

"""Creación de Usuarios con ID - Nombre - Apellidos - Document - Edad - Email - Posicion - Company"""
def create_client():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    user = []

    _print_welcome()
    try:
        _name = (input("What is the Client Name > "))
        _lastname = (input("What is the Client LastName > "))
        _document = (input("What is the Client Document > "))
        _age = (input("What is the Client Age > "))
        _email = (input("What is the Client Email > "))
        _position = (input("What is the Client Position > "))
        _company = (input("What is the Client Company > "))

        user.append(_name)
        user.append(_lastname)
        user.append(_document)
        user.append(_age)
        user.append(_email)
        user.append(_position)
        user.append(_company)

        cursor.execute("INSERT INTO users VALUES (null,?,?,?,?,?,?,?)", user)
        conexion.commit()

        cursor.execute("SELECT * FROM users WHERE Document = {} ".format(_document))
        client = cursor.fetchone()
        conexion.commit()
        cursor.close()

        os.system("cls")
        _print_welcome()
        print("Client added successfully :)\n")
        print("ID:", client[0],"\nName:", client[1], "\nLastName:", client[2], "\nDocument:", client[3], "\nAge:", client[4], "\nEmail:", client[5], "\nPosition:", client[6], "\nCompany: ", client[7])
        input("\n")

    except ValueError:
        pass
    
    except sqlite3.IntegrityError:
        os.system("CLS")
        _print_welcome()
        print("ERROR: The data already exists :(")
        time.sleep(1.5)

    except sqlite3.ProgrammingError:
        os.system("CLS")
        _print_welcome()
        print("ERROR: Check the data and try again :(")
        time.sleep(1.5)

    except sqlite3.OperationalError:
        os.system("CLS")
        _print_welcome()
        print("ERROR: Check the data and try again :(")
        time.sleep(1.5)

    except TypeError:
        os.system("CLS")
        _print_welcome()
        print("ERROR: Check the data and try again :(")
        time.sleep(1.5)

    user.clear()
    cursor.close()

        