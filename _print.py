def _print_welcome():
    print("*" * 55)
    print("\t\tDATABASE ANDREY HERRERA")
    print("*" * 55)

def _print_menu():
    _print_welcome()
    print("What would you like to do today?")
    print("[C]reate client")
    print("[S]earch client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[E]xit")
    print()

def _print_exit():
    _print_welcome()
    print("See you Later :)")
    print()

def _print_error():
    _print_welcome()
    print("Invalid Command :(")
    print()

def _print_search():
    print("How would you like to Search the client?")
    print("[1] Client ID ")
    print("[2] Client Document")

def _print_update():
    print("What would you like to update about the client?")
    print("[1] Client Name")
    print("[2] Client LastName")
    print("[3] Client Document")
    print("[4] Client Age")
    print("[5] Client Email")
    print("[6] Client Position")
    print("[7] Client Company")
    print("[8] All Client Data")