class car(object):
    def __init__(self,name,mileage,cartype,doors,mortor_sound):
        self.__name=name
        self.__mileage=mileage
        self.__cartype=cartype
        self.__doors=doors
        self.__mortor_sound=mortor_sound

    def self_desc(self):
        print("The name of the car is %s and it has %s mileage. Its type is %s and it has %s doors. It sounds like %s"
              %(self.__name,self.__mileage,self.__cartype,self.__doors,self.__mortor_sound))

    def change_mileage(self,mileage):
        self.__mileage=mileage



mycar=car("Nissa",60000,"Van",4,"ding ding")
mycar.self_desc()
mycar.change_mileage(5000)
mycar.self_desc()
    
