class Car:
    def __init__(self, brand, engine_status='off'):
        self.brand = brand
        self.screen = ''
        self.engine_status = engine_status

    def type_letter(self, letter):
        self.screen = letter

    def turn_off(self):
        self.engine_status = 'off'
        print('Turning off')

    def turn_on(self):
        self.engine_status = 'on'
        print('Turning on')

my_car = Car("Tesla")
print(my_car.brand)           
my_car.turn_on()              
print(my_car.engine_status)  

my_car.type_letter('A')
print(my_car.screen)         

my_car.turn_off()        