class Animal:
    def __init__(self, nom, espece, regime_alimentaire):
        self.nom = nom
        self.espece = espece
        self.regime_alimentaire = regime_alimentaire

    def __str__(self):
        return f"{self.nom} ({self.espece})"


class Carnivore(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Carnivore", "carnivore")


class Herbivore(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Herbivore", "herbivore")


class Omnivore(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Omnivore", "omnivore")


class Cage:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def lister_animaux(self):
        if not self.animaux:
            print("La cage est vide.")
        else:
            print("Animaux dans la cage :")
            for animal in self.animaux:
                print(animal)

    def gerer_relations_predateur_proie(self):
        for animal in self.animaux:
            if isinstance(animal, Carnivore):
                for proie in self.animaux:
                    if isinstance(proie, Herbivore) or isinstance(proie, Omnivore):
                        print(f"{animal.nom} a mangé {proie.nom} !")
                        self.animaux.remove(proie)  # Le prédateur mange la proie


class Zoo:
    def __init__(self):
        self.cages = []

    def ajouter_cage(self):
        self.cages.append(Cage())
        print("Une nouvelle cage a été ajoutée.")

    def afficher_nombre_cages(self):
        print(f"Il y a actuellement {len(self.cages)} cages dans le zoo.")

    def choisir_cage(self, numero_cage):
        return self.cages[numero_cage - 1]

    def nourrir_animal(self, animal_nom, aliment):
        for cage in self.cages:
            for animal in cage.animaux:
                if animal.nom.lower() == animal_nom.lower():
                    if (aliment == "viande" and animal.regime_alimentaire == "carnivore") or \
                       (aliment == "herbe" and animal.regime_alimentaire == "herbivore") or \
                       (aliment in ["viande", "herbe"] and animal.regime_alimentaire == "omnivore"):
                        print(f"{animal.nom} a été nourri avec {aliment}.")
                    else:
                        print(f"{animal.nom} ne peut pas manger {aliment}. Nourrissez-le correctement !")


def afficher_menu():
    print("\n--- Menu Zoo ---")
    print("1. Ajouter une cage")
    print("2. Ajouter un animal")
    print("3. Afficher le nombre de cages")
    print("4. Afficher les animaux dans une cage")
    print("5. Nourrir un animal")
    print("6. Gérer les relations prédateur/proie")
    print("7. Quitter")
    print("----------------")

def program_interactif():
    zoo = Zoo()

    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-7): ")

        if choix == "1":
            zoo.ajouter_cage()

        elif choix == "2":
            if len(zoo.cages) == 0:
                print("Aucune cage n'est disponible. Ajoutez d'abord une cage.")
                continue

            animal_type = input("Quel type d'animal voulez-vous ajouter ? (1: Carnivore, 2: Herbivore, 3: Omnivore) : ")
            nom = input("Entrez le nom de l'animal : ")

            if animal_type == "1":
                animal = Carnivore(nom)
            elif animal_type == "2":
                animal = Herbivore(nom)
            else:
                animal = Omnivore(nom)

            numero_cage = int(input("Dans quelle cage souhaitez-vous mettre cet animal ? (Entrez le numéro de la cage) : "))
            if numero_cage <= len(zoo.cages):
                cage = zoo.choisir_cage(numero_cage)
                cage.ajouter_animal(animal)
                print(f"{animal.nom} a été ajouté à la cage {numero_cage}.")
            else:
                print("Cage non existante.")

        elif choix == "3":
            zoo.afficher_nombre_cages()

        elif choix == "4":
            numero_cage = int(input("Entrez le numéro de la cage à afficher : "))
            if numero_cage <= len(zoo.cages):
                cage = zoo.choisir_cage(numero_cage)
                cage.lister_animaux()
            else:
                print("Cage non existante.")

        elif choix == "5":
            animal_nom = input("Entrez le nom de l'animal à nourrir : ")
            aliment = input("Entrez l'aliment (viande, herbe) : ")
            zoo.nourrir_animal(animal_nom, aliment)

        elif choix == "6":
            numero_cage = int(input("Entrez le numéro de la cage pour gérer les relations prédateur/proie : "))
            if numero_cage <= len(zoo.cages):
                cage = zoo.choisir_cage(numero_cage)
                cage.gerer_relations_predateur_proie()
            else:
                print("Cage non existante.")

        elif choix == "7":
            print("Merci d'avoir utilisé le programme de gestion du zoo. À bientôt !")
            break

        else:
            print("Option invalide. Essayez à nouveau.")

if __name__ == "__main__":
    program_interactif()
