import sys

sys.path.append("../")
import pakuri
import pakudex

def mainMenu(pakudex):
    repeat = True
    while repeat:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n")
        choice = input("What would you like to do? ")
        if choice.isdigit() and int(choice) == 1:
            if len(pakudex.species) == 0:
                print("No Pakuri in Pakudex yet!")
            print("Pakuri In Pakudex:")
            i = 1
            for name in pakudex.names:
                print(f"{i}. {name}")
                i += 1
        elif choice.isdigit() and int(choice) == 2:
            name = input("Enter the name of the species to display: ")
            foundspecies = False
            for spicy in pakudex.species:
                if spicy.species == name:
                    foundspecies = True
                    print(f"Species: {spicy.species}")
                    print(f"Attack: {spicy.attack}")
                    print(f"Defense: {spicy.defense}")
                    print(f"Speed: {spicy.speed}")
            if not foundspecies:
                print("Error: No such Pakuri!")

        elif choice.isdigit() and int(choice) == 3:
            if pakudex.get_size() == pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                name = input("Enter the name of the species to add: ")
                pakudex.add_pakuri(name)

        elif choice.isdigit() and int(choice) == 4:
            name = input("Enter the name of the species to evolve: ")
            evolved = pakudex.evolve_species(name)
            if not evolved:
                print("Error: No such Pakuri!")

        elif choice.isdigit() and int(choice) == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice.isdigit() and int(choice) == 6:
            print("Thanks for using Pakudex! Bye!")
            repeat = False

        else:
            print("Unrecognized menu selection!\n")



if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    valid_capacity = False
    while not valid_capacity:
        capacitystr = input("Enter max capacity of the Pakudex: ")
        if capacitystr.isdigit():
            capacity = int(capacitystr)
            if capacity > 0:
                valid_capacity = True
        else:
            print("Please enter a valid size.")
    print(f"The Pakudex can hold {capacity} species of Pakuri.\n")
    Pakudex = pakudex.Pakudex(capacity)
    mainMenu(Pakudex)



