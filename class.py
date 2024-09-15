class Puppy():
    def __init__(self,name,fav_toy):
        self.name=name
        self.fav_toy=fav_toy

    def play(self):
     print(self.name+ " is playing with the "+ self.fav_toy)

# Creating an instance and calling the method
marble = Puppy('Marble', 'Teddy Bear')
marble.play()

