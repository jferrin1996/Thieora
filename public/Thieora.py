import datetime
from Person import Person

class Thieora:
     
    '''
    firstName = raw_input("First Name: ")
    lastName = raw_input("Last Name: ")
    month = int(raw_input("Birth Month: "))
    day = int(raw_input("Birth Day: "))
    year = int(raw_input("Birth Year: "))
    address = raw_input("Address: ")
    telephone = raw_input("Phone Number: ")
    email = raw_input("Email: ")
    birthdate = datetime.date(year, month, day)
    '''

    #jake = Person(firstName, lastName, birthdate, address, telephone, email)
    
    jake = Person("Jake", "Ferrin", datetime.date(1996,9,19),
     "5521 n 92nd Ave. Omaha, NE 68134", "402-214-1343", "jake_ferrin@yahoo.com")


    print(jake.firstName)
    print(jake.age())


    #print(Person.jake.firstName)
    #print(jake.email)
    #print(jake.Person.age())




