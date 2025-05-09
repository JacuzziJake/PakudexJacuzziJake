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
        choice = int(input("What would you like to do?"))
        if choice == 1:
            if len(pakudex.species) == 0:
                print("No Pakuri in Pakudex yet!")
            print("Pakuri in Pakudex:")
            i = 1
            for name in pakudex.names:
                print(f"{i}. {name}")
                i += 1
        elif choice == 2:
            name = input("Enter the name of the species you would like to display:")
            for spicy in pakudex.species:
                if spicy.species == name:
                    print(f"Species: {spicy.species}")
                    print(f"Attack: {spicy.attack}")
                    print(f"Defense: {spicy.defense}")
                    print(f"Speed: {spicy.speed}")

        elif choice == 3:
            name = input("Enter the name of the species you would like to add:")
            pakudex.add_pakuri(name)

        elif choice == 4:
            name = input("Enter the name of the species to evolve:")
            evolved = False
            for species in pakudex.species:
                if species.species == name:
                    species.evolve()
                    evolved = True
                    print(f"{species.species} has evolved!")
                    break
            if not evolved:
                print("Error: No such Pakuri!")

        elif choice == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            repeat = False





if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = int(input("Enter max capacity of the Pakudex:"))
    print(f"The Pakudex can hold {capacity} species of Pakuri.\n")
    Pakudex = pakudex.Pakudex(capacity)
    mainMenu(Pakudex)



