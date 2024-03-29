def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all_contacts(contacts):
    for name, phone in contacts.items():
        print(f'{name} - {phone}')


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))   
        elif command == "all":
            print(show_all_contacts(contacts))         
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()                