"""Реализуйте класс «Человек». Необходимо хранить в
полях класса: ФИО, дату рождения, контактный телефон,
город, страну, домашний адрес. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса."""

class Human():
    
    def __init__(self, fio, birsdey, phone, city, country, address):
        self.fio = fio
        self.birsdey = birsdey
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def out(self):
        print("FIO = ", self.fio)
        print(self.birsdey)

    def setFio(self):
        self.fio = input("enter FIO")


h1 = Human("test", "09.02.1984", "12354", "test", "cou", "add")
h1.out()
h1.setFio()

