class Counter:
    def __init__(self):
        self._value = 0

    def add(self):
        self._value += 1

    def close(self):
        print("Counter closed.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

class Animal:
    def __init__(self, name):
        self._name = name

    def produce_sound(self):
        print("Animal produces a sound!")

class DomesticAnimal(Animal):
    pass

class Dog(DomesticAnimal):
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed
        self._commands = []

    def produce_sound(self):
        print("Dog barks!")

    def train(self, new_command):
        self._commands.append(new_command)

class Cat(DomesticAnimal):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color

    def produce_sound(self):
        print("Cat meows!")

class Hamster(DomesticAnimal):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def produce_sound(self):
        print("Hamster squeaks!")

def introduce_animal(animal):
    print(f"Name: {animal._name}")
    if isinstance(animal, Dog):
        print(f"Breed: {animal._breed}")
        print(f"Trained Commands: {', '.join(animal._commands)}")
    elif isinstance(animal, Cat):
        print(f"Color: {animal._color}")
    elif isinstance(animal, Hamster):
        print(f"Size: {animal._size}")

def main():
    animals = []

    while True:
        print("\nMenu:")
        print("1. Add a new animal")
        print("2. Identify the animal")
        print("3. Show commands of the animal")
        print("4. Train the animal with new commands")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                with Counter() as counter:
                    print("\nChoose the type of animal:")
                    print("1. Dog")
                    print("2. Cat")
                    print("3. Hamster")

                    animal_type_choice = input("Enter the type of animal: ")

                    name = input("Enter the name of the animal: ")

                    if animal_type_choice == '1':
                        breed = input("Enter the breed of the dog: ")
                        animal = Dog(name, breed)
                    elif animal_type_choice == '2':
                        color = input("Enter the color of the cat: ")
                        animal = Cat(name, color)
                    elif animal_type_choice == '3':
                        size = input("Enter the size of the hamster: ")
                        animal = Hamster(name, size)
                    else:
                        print("Invalid choice")

                    animals.append(animal)
                    print(f"{name} added to the registry!")
                    counter.add()
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            name = input("Enter the name of the animal: ")
            found = False
            for animal in animals:
                if animal._name == name:
                    introduce_animal(animal)
                    found = True
                    break
            if not found:
                print(f"{name} not found in the registry!")

        elif choice == '3':
            name = input("Enter the name of the animal: ")
            found = False
            for animal in animals:
                if animal._name == name:
                    animal.produce_sound()
                    found = True
                    break
            if not found:
                print(f"{name} not found in the registry!")

        elif choice == '4':
            name = input("Enter the name of the animal: ")
            found = False
            for animal in animals:
                if animal._name == name:
                    if isinstance(animal, Dog):
                        new_command = input("Enter a new command for the dog: ")
                        animal.train(new_command)
                        print(f"{name} trained with a new command: {new_command}")
                    else:
                        print(f"{name} cannot be trained with new commands")
                    found = True
                    break
            if not found:
                print(f"{name} not found in the registry!")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
