from person import Person

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

# print(sonny.contact_info())
# print(jordan.contact_info())

sonny.print_contact_info()

sonny.print_contact_info() 

jordan.add_friend(sonny)

jordan.num_friends()

jordan.greeting_count()

print(jordan)

# from vehicles import Vehicle

# car = Vehicle('BMW','2002tii',1969)

# print(car.print_info())
# print(car)