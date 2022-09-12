from create_database import create_database
from create_client import create_client
from search_client import search_client
from delete_client import delete_client
from update_client import update_client
from _print import _print_exit, _print_menu, _print_error
import os
import sys
import time

def main():
    create_database()
    while True:
        os.system("CLS")
        _print_menu()
        command = (input("> ")).upper()

        if command == "C":
            os.system("CLS")
            create_client()

        elif command == "S":
            os.system("CLS")
            search_client()

        elif command == "U":
            os.system("CLS")
            update_client()
        elif command == "D":
            os.system("CLS")
            delete_client()
        
        elif command == "E":
            os.system("CLS")
            _print_exit()
            time.sleep(1.5)
            os.system("CLS")
            sys.exit()
        else:
            os.system("CLS")
            _print_error()
            time.sleep(1.5)
            os.system("CLS")


if __name__ == "__main__":
    main()
