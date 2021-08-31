phonebook_array = [
  {'phone': '08160006890', 'name': 'Akporowho Marvelous', 'address': 'Lagos', 'email': 'marvelous@gmail.com'},
  {'phone': '08060349373', 'name': 'Akporowho Mark', 'address': 'Jos', 'email': 'mark@gmail.com'},
  {'phone': '08161246893', 'name': 'Akporowho Marrieth', 'address': 'Delta', 'email': 'marrieth@gmail.com'},
  {'phone': '08162426892', 'name': 'Akporowho Melvina', 'address': 'Delta', 'email': 'melvina@gmail.com'},
]

class Contact:
  def __init__(self, **kwargs):
    # create new contact as array
    new_contact = {'phone': kwargs["phone"], 
                   'name': kwargs["name"], 
                   'address': kwargs["address"], 
                   'email': kwargs["email"]
                  }
    # add contact to contact dictionary to phone book array
    phonebook_array.append(new_contact)

  
  # create contact
  def create_contact():
    first_name = input("Enter your first name: ==> ")
    last_name = input("Enter your last name: ==> ")
    address = input("Enter your address: ==> ")
    phone = input("Enter your phone: ==> ")
    email = input("Enter your email address: ==> ")
    # build full name
    full_name = last_name + " " + first_name
    new_contact = Contact(name=full_name, address=address, phone=phone, email=email)
    print(phonebook_array)
    initialize()

  
  # search contact
  def search_contact():
    search_key= input("Enter phone number: ===> ")
    key = 'phone'
    # search for a dictionary within an array
    for i in phonebook_array:
      if i.get("phone") == search_key:
        print(i)  
    initialize()


  # delete contact
  def delete_contact():
    search_key= input("Enter phone number: ===> ")
    x = search_key
    for x in phonebook_array:
      if x.get("phone") == search_key:
        phonebook_array.remove(x)
    print(phonebook_array)
    initialize()
    
  # show all contacts
  def get_all_contacts():
    print(phonebook_array)
    initialize()



def initialize():
  print("""
  To Create new contact, press 1
  To Search contact, press 2
  To Delete contact, press 3
  To Show all contacts, press 4
  To Exit phonebook, press 5
  """)

  option = input("+++>>: ")
  
  response = int(option)
  
  if response== 1:
    Contact.create_contact()
  elif response == 2:
    Contact.search_contact()
  elif response == 3:
    Contact.delete_contact()
  elif response == 4:
    Contact.get_all_contacts()
  elif response == 5:
    pass
  else:
    print ("404 Not found")

# run code
initialize()