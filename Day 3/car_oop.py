


class Car(object):
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='', model='', type=''):
        if model is '':
            self.model = 'GM'
        if name is '':
            self.name = 'General'
        else:
            self.type = type
            self.model = model 
            self.name = name
        if name == 'Porshe' or name == 'Koenigsegg':
            self.num_of_doors = 2
        if type == 'trailer':
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.type != 'trailer':
            return True

    def drive(self, pedal_on_metal):
        if self.is_saloon():
            self.speed = pedal_on_metal * (1000 / 3)
        else:
            self.speed = pedal_on_metal * 11
        return self
