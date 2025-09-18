from pprint import pprint  # import prettyprint function

# global variables
count = 42
animal = 'Wombat'

def spam(fruit):  # function parameters are local
    
    knight = 'Lancelot'  # local variable
    print(f"IN spam(): {globals() = }")

    print("Locals:")
    pprint(locals())  # locals() returns dict of all locals
    print()

spam('mango')

# globals() returns dict of all globals
print("Globals:")
pprint(globals())
print()

g = globals()
g['color'] = "blue"  # create a new variable
print("color:", color)

g['eggs'] = lambda x: 2 * x

print(f"{eggs(10) = }")
print(f"{globals() = }")
snapshot = dict(globals())
print(f"{snapshot = }")


class Foo:
    bar = 10
    def blah(self):
        x = "huh"
        print(f"{locals() = }")
        
f = Foo()
f.blah()