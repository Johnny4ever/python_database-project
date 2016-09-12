class person(object):
    def __init__(self,name="johnny",address='7 Lewisham',age=20):
        self.name=name
        self.address=address
        self.__age=age

    def self_desc(self):
        print("The name is %s and the address is %s and the age is %s"%(self.name,self.address,self.__age))




class employee(person):
    def __init__(self,name,address,age,voice="hehe"):
        person.__init__(self,name,address,age)
        self.voice=voice

    def test_voice(self):
        print(self.voice)
'''

class employee(person):
    def __init__(self,name,address,age,voice):
        super(employee,self).__init__(name,address,age)
        self.voice=voice
        
    def test_voice(self):
        print(self.voice)
'''
ken=employee("name","Mars",20,"lol")
print(ken.name)
ken.test_voice()   



