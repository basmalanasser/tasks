Contacts={}
def add_contact(Contacts,name,phone):
    if name in Contacts:
        print(f"Contact {name} already exists!")
    else:
        Contacts[name]={"phone number":phone}
    print(f"Contact {name} added successfully!")


def search_contact(Contacts,name):
    if name in Contacts:
        details=Contacts[name]
        print(f"Name:{name}")
        print(f"Phone:{details['phone']}")

    else:
        print(f"Contact {name} not found!")


def show_all_contacts(Contacts):
    if Contacts:
        for name,details in Contacts.items():
            print(f"Name:{name}")
            print(f"Phone number:{details['phone']}")
            print("-"*20)

    else:
        print("no contacts found!")



def delete_contact(Contacts,name):
    if name in Contacts:
        del Contacts[name]
        print(f"Contact {name}deleted successfully!")

    else:
        print(f"Contact {name} not found!")


def update_contact(Contacts,name,phone=None):
    if name in Contacts:
        if phone:
            Contacts[name]['phone']=phone

        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact{name} not found")


def main():
    while True:
     print("Contact Management System")
     print("1. Add contact")
     print("2. Search contact")
     print("3. Delete contact")
     print("4. Show all contacts")
     print("5. Update contact")
     print("6. Exit")
     option=int(input("enter an option:"))


     if option==1:
            name=input("enter the contact's name:")
            phone=input("enter the contact's phone:")
            add_contact(Contacts,name,phone)

     elif option==2:
        name=input("enter the name of the contact:")
        search_contact(Contacts,name)

     elif option==3:
        name=input("enter the name of the contact:")
        delete_contact(Contacts,name)


     elif option==4:
        show_all_contacts(Contacts)


     elif option==5:
        name=input("enter the name of the contact:")
        phone=input("enter the number of the contact:")
        update_contact(Contacts,name,phone if phone else None)

     elif option==6:
        break

     else:
        print("invalid option!")
        
    
main()



