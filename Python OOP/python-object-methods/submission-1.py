class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self,level):
        # TODO: Implement this method
        self.hunger -= level
        # It should decrease the pet's hunger by 1
        print(f"{my_pet.name} has been fed.")
        print(f"{my_pet.name}'s hunger level: {my_pet.hunger}")
        # and print a message about feeding the pet
        
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times 
my_pet.feed(1)
my_pet.feed(1)
my_pet.feed(1)