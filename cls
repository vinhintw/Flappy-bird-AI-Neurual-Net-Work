[1mdiff --git a/population.py b/population.py[m
[1mindex 1f529d5..1224b52 100644[m
[1m--- a/population.py[m
[1m+++ b/population.py[m
[36m@@ -1,9 +1,15 @@[m
 import config[m
 import player[m
[32m+[m[32mimport math[m
[32m+[m[32mimport species[m
[32m+[m[32mimport operator[m
[32m+[m
 [m
 class Population:[m
     def __init__(self, size):[m
         self.players = [][m
[32m+[m[32m        self.generation = 1[m
[32m+[m[32m        self.species = [][m
         self.size = size[m
         for i in range(0, self.size):[m
             self.players.append(player.Player())[m
[36m@@ -17,6 +23,96 @@[m [mclass Population:[m
                 p.draw(config.window)[m
                 p.update(config.ground)[m
 [m
[32m+[m[32m    def natural_seclection(self):[m
[32m+[m[32m        print('SPECIATE')[m
[32m+[m[32m        self.speciate()     # speciate[m
[32m+[m
[32m+[m[32m        print('CALCULATE FITNESS')[m
[32m+[m[32m        self.calulate_fitness()     #Calulate fitness[m
[32m+[m
[32m+[m[32m        print('KILL EXTINCT')[m
[32m+[m[32m        self.kill_extinct_species()[m
[32m+[m
[32m+[m[32m        print('KILL STALE')[m
[32m+[m[32m        self.kill_stale_species()[m
[32m+[m
[32m+[m[32m        print('CHILDREN GOR NEXT GEN')[m
[32m+[m[32m        self.next_gen()[m
[32m+[m
[32m+[m[32m    def speciate(self):[m
[32m+[m[32m        # Remove current players before speciate[m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            s.players = [][m
[32m+[m[41m        [m
[32m+[m[32m        for p in self.players:      #loops on all players[m
[32m+[m[32m            add_to_species = False[m
[32m+[m[32m            for s in self.species:[m
[32m+[m[32m                if s.similarity(p.brain):       #if player's brain is similarity -> add to species[m
[32m+[m[32m                    s.add_to_species = True[m
[32m+[m[32m                    break[m
[32m+[m[32m            if not add_to_species:[m
[32m+[m[32m                self.species.append(species.Species(p))[m
[32m+[m
[32m+[m[32m    def calulate_fitness(self):[m
[32m+[m[32m        for p in self.players:[m
[32m+[m[32m            p.calulate_fitness()[m
[32m+[m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            s.calcalulate_average_fitness()[m
[32m+[m
[32m+[m[32m    def kill_extinct_species(self):[m
[32m+[m[32m        species_bin = [][m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            if len(s.players) == 0:[m
[32m+[m[32m                species_bin.append(s)[m
[32m+[m[32m        for s in species_bin:[m
[32m+[m[32m            self.species.remove(s)[m
[32m+[m
[32m+[m[32m    def kill_stale_species(self):[m
[32m+[m[32m        player_bin = [][m
[32m+[m[32m        species_bin = [][m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            if s.staleness >= 8:[m
[32m+[m[32m                if len(self.species) > len(species_bin) +1:[m
[32m+[m[32m                    species_bin.append(s)[m
[32m+[m[32m                    for p in s.players:[m
[32m+[m[32m                        player_bin.append(p)[m
[32m+[m[32m                else:[m
[32m+[m[32m                    s.staleness = 0[m
[32m+[m[32m        for p in player_bin:[m
[32m+[m[32m            self.players.remove(p)[m
[32m+[m[32m        for s in species_bin:[m
[32m+[m[32m            self.species.remove(s)[m
[32m+[m
[32m+[m
[32m+[m[32m    def sort_species_by_fitness(self):[m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            s.sort_player_by_fitness()[m
[32m+[m
[32m+[m[32m        self.species.sort(key=operator.attrgetter('benchmark_fitness'), reverse=True)[m
[32m+[m
[32m+[m[32m    def next_gen(self):[m
[32m+[m[32m        children = [][m
[32m+[m
[32m+[m[32m        # Clone of champion is added to each species[m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            children.append(s.champion.clone())[m
[32m+[m
[32m+[m[32m        # Fill open player slots are dead[m
[32m+[m[32m        children_per_species = math.floor((self.size - len(self.species)) / len(self.species))[m
[32m+[m
[32m+[m[32m        for s in self.species:[m
[32m+[m[32m            for i in range(0, children_per_species):[m
[32m+[m[32m                children.append(s.offspring())[m
[32m+[m
[32m+[m[32m        while len(children) < self.size:[m
[32m+[m[32m            children.append(self.species[0].offspring())[m
[32m+[m
[32m+[m[32m        self.players: [][m
[32m+[m[32m        for child in children:[m
[32m+[m[32m            self.players.append(child)[m
[32m+[m[32m        self.generation += 1[m
[32m+[m
     #Return true if all player are dead[m
     def extinct(self):[m
         extinct = True[m
