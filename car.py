class Car:
    def __init__(self, brand, engine_status='off'):
        self.brand = brand
        self.screen = ''
        self.engine_status = engine_status
        self.__memory = {}

    def type_letter(self, letter):
        self.screen = letter
        self.__memory['last_letter'] = letter

    def __erase_the_memory(self):
        self.__memory = {}
        print('memory is clean')

    def turn_off(self):
        self.engine_status = 'off'
        print('Turning off')

    def turn_on(self):
        self.engine_status = 'on'
        print('Turning on')

    def show_me_the_memory(self):
        print(self.__memory)

    def clean_my_brain(self):  
        self.__erase_the_memory()

my_car = Car("Tesla")
print(my_car.brand)          
my_car.turn_on()              
print(my_car.engine_status)  
my_car.type_letter('Q')
print(my_car.screen)          
my_car.turn_off()   

my_car2 = Car("Tesla")
my_car2.clean_my_brain()
