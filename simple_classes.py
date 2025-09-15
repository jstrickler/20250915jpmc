colors = [] # colors = list()
cities = list()  # list cities = new list();
cities.append('Glasgow')
cities.append("Bangalore")
cities.append("Jersey City")

x = 5   # x = int(5)
print(f"{type(x) = }")

# type value ID
t = type(x)
m = t(55)
print(f"{m = }")
print(f"{type(m) = }")

# TitleCase  UpperCamelCase  StudlyCaps
class Dog:
    def bark(self, bark_type):
        self.loud()
        print(f"{bark_type}! {bark_type}!")

    def loud(self):
        pass

    @staticmethod
    def spam():
        print("I am spam")

d1 = Dog()
d2 = Dog()
d1.bark("woof")    # Dog.bark(d1)
d2.bark("yip")
