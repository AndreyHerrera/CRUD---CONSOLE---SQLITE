import sqlite3
import os
import time
from _print import _print_welcome, _print_search, _print_error, _print_update


"""Busca los Usuarios con ID - Document y los actualiza"""


def update_client():
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

            os.system("cls")
            _print_welcome()
            _print_update()
            _command = int(input("\n> "))

            if _command == 1:
                os.system("cls")
                _print_welcome()
                _name = str(input("What is the new Client Name > "))
                cursor.execute("UPDATE users SET Name = '{}' WHERE ID = {} ".format(_name, client_id))
                
            elif _command == 2:
                os.system("cls")
                _print_welcome()
                _lastname = (input("What is the new Client LastName > "))
                cursor.execute("UPDATE users SET LastName = '{}' WHERE ID = {} ".format(_lastname, client_id))

            elif _command == 3:
                os.system("cls")
                _print_welcome()
                _document = (input("What is the new Client Document > "))
                cursor.execute("UPDATE users SET Document = '{}' WHERE ID = {} ".format(_document, client_id))

            elif _command == 4:
                os.system("cls")
                _print_welcome()
                _age = (input("What is the new Client Age > "))
                cursor.execute("UPDATE users SET Age = '{}' WHERE ID = {} ".format(_age, client_id))

            elif _command == 5:
                os.system("cls")
                _print_welcome()
                _email = (input("What is the new Client Email > "))
                cursor.execute("UPDATE users SET Email = '{}' WHERE ID = {} ".format(_email, client_id))

            elif _command == 6:
                os.system("cls")
                _print_welcome()
                _position = (input("What is the new Client Position > "))
                cursor.execute("UPDATE users SET Position = '{}' WHERE ID = {} ".format(_position, client_id))

            elif _command == 7:
                os.system("cls")
                _print_welcome()
                _company = (input("What is the new Client Company > "))
                cursor.execute("UPDATE users SET Company = '{}' WHERE ID = {} ".format(_company, client_id))

            elif _command == 8:
                os.system("cls")
                _print_welcome()
                _name = str(input("What is the new Client Name > "))
                _lastname = (input("What is the new Client LastName > "))
                _document = (input("What is the new Client Document > "))
                _age = (input("What is the new Client Age > "))
                _email = (input("What is the new Client Email > "))
                _position = (input("What is the new Client Position > "))
                _company = (input("What is the new Client Company > "))
                cursor.execute("UPDATE users SET Name = '{}' , LastName = '{}' , Document = '{}', Age = '{}' , Email = '{}' , Position = '{}' , Company = '{}' WHERE ID = {} ".format(_name, _lastname, _document, _age, _email, _position, _company, client_id))
               
            conexion.commit()

            cursor.execute("SELECT * FROM users WHERE ID = {} ".format(client_id))
            client = cursor.fetchone()
            conexion.commit()

            cursor.close()
            os.system("cls")
            _print_welcome()
            print("Client updated successfully :)\n")
            print("ID:", client[0],"\nName:", client[1], "\nLastName:", client[2], "\nDocument:", client[3], "\nAge:", client[4], "\nEmail:", client[5], "\nPosition:", client[6], "\nCompany: ", client[7])
            input("\n")

        if command == 2:
            os.system("cls")
            _print_welcome()
            print("Type the client Document:")
            client_document = int(input("\n> "))
            cursor.execute("SELECT * FROM users WHERE Document = {} ".format(client_document))
            client = cursor.fetchone()
            conexion.commit()

            os.system("cls")
            _print_welcome()
            _print_update()
            _command = int(input("\n> "))

            if _command == 1:
                os.system("cls")
                _print_welcome()
                _name = str(input("What is the new Client Name > "))
                cursor.execute("UPDATE users SET Name = '{}' WHERE Document = {} ".format(_name, client_document))
                
            elif _command == 2:
                os.system("cls")
                _print_welcome()
                _lastname = (input("What is the new Client LastName > "))
                cursor.execute("UPDATE users SET LastName = '{}' WHERE Document = {} ".format(_lastname, client_document))

            elif _command == 3:
                os.system("cls")
                _print_welcome()
                _document = (input("What is the new Client Document > "))
                cursor.execute("UPDATE users SET Document = '{}' WHERE Document = {} ".format(_document, client_document))
                client_document = _document

            elif _command == 4:
                os.system("cls")
                _print_welcome()
                _age = (input("What is the new Client Age > "))
                cursor.execute("UPDATE users SET Age = '{}' WHERE Document = {} ".format(_age, client_document))

            elif _command == 5:
                os.system("cls")
                _print_welcome()
                _email = (input("What is the new Client Email > "))
                cursor.execute("UPDATE users SET Email = '{}' WHERE Document = {} ".format(_email, client_document))

            elif _command == 6:
                os.system("cls")
                _print_welcome()
                _position = (input("What is the new Client Position > "))
                cursor.execute("UPDATE users SET Position = '{}' WHERE Document = {} ".format(_position, client_document))

            elif _command == 7:
                os.system("cls")
                _print_welcome()
                _company = (input("What is the new Client Company > "))
                cursor.execute("UPDATE users SET Company = '{}' WHERE Document = {} ".format(_company, client_document))

            elif _command == 8:
                os.system("cls")
                _print_welcome()
                _name = str(input("What is the new Client Name > "))
                _lastname = (input("What is the new Client LastName > "))
                _document = (input("What is the new Client Document > "))
                _age = (input("What is the new Client Age > "))
                _email = (input("What is the new Client Email > "))
                _position = (input("What is the new Client Position > "))
                _company = (input("What is the new Client Company > "))
                cursor.execute("UPDATE users SET Name = '{}' , LastName = '{}' , Document = '{}', Age = '{}' , Email = '{}' , Position = '{}' , Company = '{}' WHERE Document = {} ".format(_name, _lastname, _document, _age, _email, _position, _company, client_document))
                client_document = _document
               
            conexion.commit()
            cursor.execute("SELECT * FROM users WHERE Document = {} ".format(client_document))
            client = cursor.fetchone()
            conexion.commit()

            cursor.close()
            os.system("cls")
            _print_welcome()
            print("Client updated successfully :)\n")
            print("ID:", client[0],"\nName:", client[1], "\nLastName:", client[2], "\nDocument:", client[3], "\nAge:", client[4], "\nEmail:", client[5], "\nPosition:", client[6], "\nCompany: ", client[7])
            input("\n")

                    
    except ValueError:
        os.system("cls")
        _print_error()
        time.sleep(1.5)

    except TypeError:
        os.system("cls")
        _print_welcome()
        print("ERROR: The client dont exist :(")
        time.sleep(1.5)