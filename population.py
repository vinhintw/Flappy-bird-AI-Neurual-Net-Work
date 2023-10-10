import config
import player
import math
import species
import operator


class Population:
    def __init__(self, size):
        self.players = []
        self.generation = 1
        self.species = []
        self.size = size
        for i in range(0, self.size):
            self.players.append(player.Player())

    
    def update_live_player(self):
        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                p.draw(config.window)
                p.update(config.ground)

    def natural_seclection(self):
        print('SPECIATE')
        self.speciate()     # speciate

        print('CALCULATE FITNESS')
        self.calulate_fitness()     #Calulate fitness

        print('KILL EXTINCT')
        self.kill_extinct_species()

        print('KILL STALE')
        self.kill_stale_species()

        print('CHILDREN GOR NEXT GEN')
        self.next_gen()

    def speciate(self):
        # Remove current players before speciate
        for s in self.species:
            s.players = []
        
        for p in self.players:      #loops on all players
            add_to_species = False
            for s in self.species:
                if s.similarity(p.brain):       #if player's brain is similarity -> add to species
                    s.add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(p))

    def calulate_fitness(self):
        for p in self.players:
            p.calulate_fitness()

        for s in self.species:
            s.calcalulate_average_fitness()

    def kill_extinct_species(self):
        species_bin = []
        for s in self.species:
            if len(s.players) == 0:
                species_bin.append(s)
        for s in species_bin:
            self.species.remove(s)

    def kill_stale_species(self):
        player_bin = []
        species_bin = []
        for s in self.species:
            if s.staleness >= 8:
                if len(self.species) > len(species_bin) +1:
                    species_bin.append(s)
                    for p in s.players:
                        player_bin.append(p)
                else:
                    s.staleness = 0
        for p in player_bin:
            self.players.remove(p)
        for s in species_bin:
            self.species.remove(s)


    def sort_species_by_fitness(self):
        for s in self.species:
            s.sort_player_by_fitness()

        self.species.sort(key=operator.attrgetter('benchmark_fitness'), reverse=True)

    def next_gen(self):
        children = []

        # Clone of champion is added to each species
        for s in self.species:
            children.append(s.champion.clone())

        # Fill open player slots are dead
        children_per_species = math.floor((self.size - len(self.species)) / len(self.species))

        for s in self.species:
            for i in range(0, children_per_species):
                children.append(s.offspring())

        while len(children) < self.size:
            children.append(self.species[0].offspring())

        self.players: []
        for child in children:
            self.players.append(child)
        self.generation += 1

    #Return true if all player are dead
    def extinct(self):
        extinct = True
        for p in self.players:
            if p.alive:
                extinct = False
        return extinct