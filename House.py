
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_name(self):
        return self.name

    def display_age(self):
        return self.age
        
class House:
    
    def __init__(self,address,numOfrooms):
        self.address = address
        self.numOfrooms = numOfrooms
        self.persons = []
        
    def add_person(self,obj):
        self.persons.append(obj)
        
    def remove_person(self,obj):
        for i in self.persons:
            if i == obj:
                self.persons.remove(i)
            else:
                continue
            
    def display(self):
        for i in range(0,len(self.persons)):
            print("Person",i+1,"Name:",self.persons[i].display_name(),"Age:",self.persons[i].display_age())
            
Muaaz = Person("Muaaz",20)
Mansion = House("21 Boulevard",10)
Mansion.add_person(Muaaz)
Mansion.add_person(Person("Ali",19))
Mansion.add_person(Person("Omer",21))
Mansion.display()
Mansion.remove_person(Muaaz)
Mansion.display()

