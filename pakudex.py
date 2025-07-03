import sys

sys.path.append("../")
import pakuri

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.species = []
        self.names = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.size == 0:
            return None
        return self.species

    def get_stats(self, name):
        stats = []
        for spicy in self.species:
            if spicy.species == name:
                stats.append(spicy.get_attack())
                stats.append(spicy.get_defense())
                stats.append(spicy.get_speed())
                return stats
        if len(stats) == 0:
            return None
        return stats

    def sort_pakuri(self):
        self.names.sort()

    def add_pakuri(self, name):
        for spicy in self.species:
            if spicy.species == name:
                print("Error: Pakudex already contains this species!")
                return False
        if self.size == self.capacity:
            print("Error: Pakudex is full!")
            return False
        self.species.append(pakuri.Pakuri(name))
        self.names.append(name)
        self.size += 1
        print(f"Pakuri species {name} successfully added!")
        return True

    def evolve_species(self, name):
        for spicy in self.species:
            if spicy.species == name:
                spicy.evolve()
                return True
        return False










