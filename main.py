class Animal:
    def __init__(self, nom, espece, regime_alimentaire):
        self.nom = nom
        self.espece = espece
        self.regime_alimentaire = regime_alimentaire

    def __str__(self):
        return f"{self.nom} ({self.espece})"

    def nourrir(self, aliment):
        """Nourrit l'animal selon son régime alimentaire."""
        if self.regime_alimentaire == "carnivore" and aliment in ["viande"]:
            print(f"{self.nom} a été nourri avec de la viande. Nourriture correcte !")
        elif self.regime_alimentaire == "herbivore" and aliment in ["herbe"]:
            print(f"{self.nom} a été nourri avec de l'herbe. Nourriture correcte !")
        elif self.regime_alimentaire == "omnivore" and aliment in ["viande", "herbe"]:
            print(f"{self.nom} a été nourri avec {aliment}. Nourriture correcte !")
        else:
            print(f"{self.nom} ne mange pas {aliment}. Aliment inapproprié !")


# Sous-classes spécifiques d'animaux
class Lion(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Lion", "carnivore")


class Gazelle(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Gazelle", "herbivore")


class Hyene(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Hyène", "carnivore")


class Serpent(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Serpent", "carnivore")


class Cage:
    def __init__(self, numero):
        self.numero = numero
        self.animaux = []

    def ajouter_animal(self, animal):
        """Ajoute un animal dans la cage."""
        self.animaux.append(animal)

    def lister_animaux(self):
        """Retourne une liste des animaux dans la cage."""
        if not self.animaux:
            return "Aucun animal dans cette cage."
        return "\n".join(str(animal) for animal in self.animaux)

    def gerer_predateur_proie(self):
        """Gère la relation prédateur/proie dans la cage."""
        carnivores = [animal for animal in self.animaux if animal.regime_alimentaire == "carnivore"]
        herbivores = [animal for animal in self.animaux if animal.regime_alimentaire == "herbivore"]

        for carnivore in carnivores:
            for proie in herbivores:
                print(f"{carnivore.nom} (le prédateur) a mangé {proie.nom} (la proie).")


class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.cages = []

    def ajouter_cage(self, cage):
        """Ajoute une cage au zoo."""
        self.cages.append(cage)

    def afficher_cages(self):
        """Affiche toutes les cages et leurs animaux."""
        print(f"Le zoo {self.nom} contient les cages suivantes :")
        for cage in self.cages:
            print(f"\nCage {cage.numero} :")
            print(cage.lister_animaux())
            cage.gerer_predateur_proie()

    def nombre_de_cages(self):
        """Retourne le nombre total de cages dans le zoo."""
        return len(self.cages)


# Exemple d'utilisation

# Création du zoo
zoo = Zoo("Zoo de Paris")

# Création des animaux
lion1 = Lion("Simba")
lion2 = Lion("Mufasa")
gazelle = Gazelle("Bambi")
serpent = Serpent("Python")
hyene = Hyene("Hya")

# Création des cages
cage1 = Cage(1)
cage1.ajouter_animal(lion1)
cage1.ajouter_animal(gazelle)

cage2 = Cage(2)
cage2.ajouter_animal(serpent)

cage3 = Cage(3)
cage3.ajouter_animal(hyene)
cage3.ajouter_animal(lion2)

# Ajout des cages au zoo
zoo.ajouter_cage(cage1)
zoo.ajouter_cage(cage2)
zoo.ajouter_cage(cage3)

# Nourrir les animaux
lion1.nourrir("viande")
gazelle.nourrir("herbe")
serpent.nourrir("viande")
hyene.nourrir("viande")

# Affichage des cages et des animaux
zoo.afficher_cages()

# Affichage du nombre de cages
print(f"\nLe zoo a {zoo.nombre_de_cages()} cage(s).")
