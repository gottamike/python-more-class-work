# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# November 5, 2019                                    |
# Michael Gotta                                       |
# -----------------------------------------------------

class Queue():                        # creating class
    def __init__(self, number):
        self.numbers = number
        self.list = []

    def __iadd__(self, number):
        self.list.append(number)
        return self


    def enqueue(self, number):
        self.list.append(number)

    def dequeue(self):
        result = self.list[0]
        self.list.pop(0)
        return result
    def is_empty(self):
        if len(self.list) == 0:
            return True

    def __str__(self):
        return "Contents: " + str(" ".join(str(number) for number in self.list))


# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()