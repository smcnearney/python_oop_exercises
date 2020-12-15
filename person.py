class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def contact_info(self):
        return "{}\'s e-mail address: {} and phone number: {}".format(self.name, self.email, self.phone)
