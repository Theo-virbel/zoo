## Description du projet

Le projet implémente une gestion de zoo en utilisant la programmation orientée objet (POO). Il permet de simuler la gestion des cages et des animaux dans un zoo. Les fonctionnalités incluent l'ajout de cages, l'ajout d'animaux, l'affichage des animaux dans chaque cage, ainsi que la gestion des relations prédateur/proie et l'alimentation des animaux.

## Fonctionnalités

- **Gestion des cages** : Ajouter des cages au zoo et afficher le nombre de cages.
- **Ajout des animaux** : Ajouter des animaux à chaque cage et lister les animaux présents dans une cage.
- **Relations prédateur/proie** : Les carnivores mangent les herbivores si ces derniers se trouvent dans la même cage.
- **Alimentation des animaux** : Nourrir les animaux en fonction de leur régime alimentaire (carnivore, herbivore, omnivore) et vérifier si l'aliment est approprié.

## Structure du Projet

Le projet contient plusieurs classes pour modéliser le zoo, les cages, et les animaux :

### Classes

- **Zoo** : Représente le zoo contenant plusieurs cages. Permet d'ajouter des cages et d'afficher leur nombre.
- **Cage** : Représente une cage contenant plusieurs animaux. Permet d'ajouter des animaux et de lister les animaux présents.
- **Animal** : Classe de base pour les animaux. Contient un nom et une méthode pour les nourrir.
- **Carnivore, Herbivore, Omnivore** : Sous-classes d'`Animal` représentant les différents régimes alimentaires des animaux.
- **Lion, Gazelle, Hyène, Serpent** : Sous-classes spécifiques d'animaux représentant des espèces précises, héritant des classes appropriées (`Carnivore` ou `Herbivore`).

### Fonctionnalités bonus :

- **Relations Prédateur/Proie** : Lorsqu'un carnivore et un herbivore se trouvent dans la même cage, le carnivore peut manger l'herbivore.
- **Alimentation des Animaux** : Les animaux sont nourris en fonction de leur régime alimentaire (carnivore, herbivore, omnivore). Si un animal est nourri avec un aliment inapproprié, un message d'erreur est affiché.

## Instructions d'Utilisation

1. **Clonez ce repository** :

   ```bash
   git clone https://github.com/votre-utilisateur/zoo.git
   cd zoo
