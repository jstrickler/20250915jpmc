class Increment:
    def __init__(self):
        self.number = 0

    def __call__(self):
        number_to_return = self.number
        self.number += 1
        return number_to_return


i = Increment()
for _ in range(10):
    print(i())