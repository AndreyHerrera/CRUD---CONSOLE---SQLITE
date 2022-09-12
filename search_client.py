import sqlite3
import os
import time
from _print import _print_welcome, _print_search, _print_error


"""Buscar Usuarios con ID - Document"""
def search_client():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    _print_welcome()
    _print_search()

    try:
        command = int(input("\n> "))

        if command == 1:
            os.system("cls")
            _print_welcome()
            print("Type the client ID:")
            client_id = int(input("\n> "))
            cursor.execute("SELECT * FROM users WHERE ID = {} ".format(client_id))
            client = cursor.fetchone()
            conexion.commit()
            cursor.close()
            os.system("cls")
            _print_welcome()
            print("ID:", client[0],"\nName:", client[1], "\nLastName:", client[2], "\nDocument:", client[3], "\nAge:", client[4], "\nEmail:", client[5], "\nPosition:", client[6], "\nCompany: ", client[7])
            input()

        if command == 2:
            os.system("cls")
            _print_welcome()
            print("Type the client Document:")
            client_document = int(input("\n> "))
            cursor.execute("SELECT * FROM users WHERE Document = {} ".format(client_document))
            client = cursor.fetchone()
            conexion.commit()
            cursor.close()
            os.system("cls")
            _print_welcome()
            print("ID:", client[0],"\nName:", client[1], "\nLastName:", client[2], "\nDocument:", client[3], "\nAge:", client[4], "\nEmail:", client[5], "\nPosition:", client[6], "\nCompany: ", client[7])
            input()

            
    except ValueError:
        os.system("cls")
        _print_error()
        time.sleep(1.5)

    except TypeError:
        os.system("cls")
        _print_welcome()
        print("ERROR: The client dont exist :(")
        time.sleep(1.5)