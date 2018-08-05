
class Bird:
    """ Parent class """

    def __init__(self,bird_name, feathers):
        self.bird_name = bird_name
        self.feathers = feathers
        

    def bird_info(self):
        print('Bird: {} and it has feathers: {}'.format(self.bird_name, self.feathers))


class FlyingBird(Bird):
    """ Child class """

    def fly_or_not(self):
        print('Yes! it can Fly')


class NotFlyingBird(Bird):
    """ Child class """
    
    def fly_or_not(self):
        print("No! it can't Fly")


fly_bird_obj = FlyingBird('parrot', True)

fly_bird_obj.bird_info() # OUTPUT: Bird: Parrot and it has feathers: True
fly_bird_obj.fly_or_not() # OUTPUT: Yes! it can Fly


not_fly_bird_obj = FlyingBird('penguin', False)

not_fly_bird_obj.bird_info() # OUTPUT: Bird: Penguin and it has feathers: False
not_fly_bird_obj.fly_or_not() # OUTPUT: No! it can't Fly