import datetime

#this class stores our person's personal info
class Person:

    def __init__(self, firstName, lastName, birthdate, address, telephone, email, married, TDID):
        self.firstName = firstName
        self.lastName = lastName
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.email = married
        self.TDID = TDID

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def taxBracket(self):
        pass
    
    '''def get_user_input(self):
        while 1:
            try:
                firstName = input('First Name: ')
                lastName = input('Last Name: ')
                birthdate = datetime.date(input('Birthdate Year: '), input('Birth Month: '), input('Birth Day: '))
                address = input('Address: ')
                telephone = input('Phone Number: ')
                email = input('Email: ')
                return self(firstName, lastName, birthdate, address, telephone, email)
            except:
                continue'''