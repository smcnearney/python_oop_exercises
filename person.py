class Person:
     def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.count_greetings = 0

     def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))
         self.count_greetings += 1

     def contact_info(self):
        return "{}\'s e-mail address: {} and phone number: {}".format(self.name, self.email, self.phone)
    
     def print_contact_info(self):
         return "{}\'s e-mail address: {} and phone number: {}".format(self.name, self.email, self.phone)

     def add_friend(self, new_friend):
          self.friends.append(new_friend)
     
     def num_friends(self):
          print(len(self.friends))
     
     def greeting_count(self):
          print(self.count_greetings)
     
     def __str__(self):
          return """
          %s
          %s
          %s
          %s
          """ % (self.name, self.email, self.phone, self.count_greetings)
     

          

     