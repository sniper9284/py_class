class Transport():
    def __init__(self, speed, oil):
        self._speed = speed
        self._oil = oil

    def setSpeed(self, speed):
        self._speed = speed

    def setOil(self, oil):
        self._oil = oil

    def getSpeed(self):
        return self._speed
    
    def getOil(self):
        return self._oil
    
    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)

    def out(self):
        print(self.speed, self.oil)

class Auto(Transport):
    
    def __init__(self, speed, oil, color):
        super().__init__(speed, oil)
        self.__color = color

    def getColor(self):
        return self.__color
    
    def setColor(self):
        self.__color = input("Enter color = ")

    color = property(getColor, setColor)

    def out(self):
        print(self.speed, self.oil, self.color)

listTr = [Transport(50, "92"), Auto(100, "95", "red"), Transport(120, "95"), Auto(200, "92", "green")]

def out(transport):
    for t in transport:
        t.out()

out(listTr)

auto = Auto(111, "95", "black")
auto.out()
# auto.color = "red"  не верное обращение
auto.setColor()
auto.out()