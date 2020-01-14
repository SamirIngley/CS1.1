class Person(object):
    def __init__(self, name, age, mood, hobbies):
        self.name = name
        self.age = age
        self.mood = mood
        self.hobbies = hobbies
    
    def attrib(self):
        print(self.name, self.age, self.mood, self.hobbies)

    def say_hello(self):
        print("hello")

    def say_name(self):
        print("hi, I'm {}".format(self.name))

    def say_age(self):
        print("hi, I'm {}".format(self.age))

    def say_mood(self):
        print("hi, I'm {}".format(self.mood))
    
    def say_hobbies(self):
        print("hi, I do {}".format(self.hobbies))

class Student(Person):
    def say_hello(self):
        print("Hey! I'm {} and I'm studying CS1.1".format(self.name))
    def get_courses(self):
        print("These are the courses I'm taking at Make School: CS1.1")

class Teacher(Person):
    def say_hello(self):
        print("Welcome to class! My name is {} and I am your teacher.".format(self.name))
    def get_schedule(self):
        print("These are the current courses I'm teaching: CS1.1")


samir = Person("Samir", "12", "happy", "tennis")
print(samir.age)
samir.age = 21
# samir.say_name()
# samir.attrib()
# print(samir.age)
# print(samir.hobbies)
# samir.say_hello()


bob = Student("Bob", "13", "happy", "writing")
# bob.say_hello()

Bill = Teacher("Bill", "22", "excited", "biking")
# Bill.say_hello()


people = [samir, bob, Bill]

for person in people:
    person.say_hello()
