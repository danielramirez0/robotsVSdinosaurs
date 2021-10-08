# Robots vs. Dinosaurs

Console application uses the concepts of OOP by creating classes and using objects (instances of those classes) to interact with each other

## Classes and Features

Includes a class for each of the following:

- Robot
- Dinosaur
- Fleet
- Herd
- Weapon
- Battlefield

**Robot** properties:

- Name
- Health
- Power level (aka *stamina* decreases by 10 each attack)
- Weapon (own class and object) with a name (i.e. sword) and attack power.
- Ability to choose from a List of different weapons that will be then assigned as weapon

**Dinosaur** properties:

- Name
- Health
- Aattack power
- Energy (aka *stamina* decreases by 10 each attack)
- Ability to choose attack name from a tuple of different attack names before attacking a Robot in battle

Instantiates three Robot objects and three Dinosaur objects

Robot objects are stored in a Fleet and the Dinosaur objects are stored in a Herd (the Fleet and Herd use a List to store the objects)

Robot can attack a Dinosaur and a Dinosaur can attack a Robot on a Battlefield

Robot/Dinosaur lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it

Battle concludes once either team members' health or endurance reaches zero (all the robots in the Fleet have their health/energy points reach zero or all of the dinosaurs in the Herd have their health/stamina points reach zero)

Includes two modes:

- One player against AI
- Two players against each other
