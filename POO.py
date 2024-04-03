# from typing_extensions import Self
# from os import name
import random
import sys
from datetime import date

class DreamHouse:
  def __init__(self, tamano,color, num_habitaciones, username, password ):
    self.tamano = tamano
    self.color = color
    self.garaje = random.choice([True, False])
    self.num_habitaciones = num_habitaciones
    self.balcon =  random.choice(["si", "no"])
    self.username = username
    self.password = password

  @classmethod
  def saludar(cls):
    print(f"La Empresa {cls.__name__} es una Agenda mundial para sugerir una casa de tus sueños")


  def login(self):
    attempts = 3
    while attempts > 0:
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contraseña: ")
      if username == self.username and password == self.password:
        return True
      else:
        print("¡Credenciales incorrectas! Quedan {} intentos.".format(attempts - 1))
        attempts -= 1
    print("¡Se han agotado los intentos! Por favor, comuníquese con el servicio al cliente.")
    return False

  def lugar(self):
    print("""QUE LUGAR DESEAS:
    1 Bogota
    2 Cartagena
    3 barranquilla
    4 cucuta
    5 santa marta
    6 medellin
    """)

    dia = date.today()
    print(dia)

    while True:
      self.opcion = int(input("QUE LUGAR DESEAS "))
      if self.opcion == 1:
         print("El lugar que eligiste Bogota")
         break
      elif self.opcion == 2:
         print("El lugar que eligiste Cartagena")
         break
      elif self.opcion == 3:
         print("El lugar que eligiste Barranquilla")
         break
      elif self.opcion == 4:
         print("El lugar que eligiste Cucuta")
         break
      elif self.opcion == 5:
         print("El lugar que eligiste Santa marta")
         break
      elif self.opcion == 6:
         print("El lugar que eligiste Medellin")
         break
      else:
        self.opcion != [1,2,3,4,5,6]
        print("ingrese un valor valido ")


  def sugerir_casa_sola_o_compartida(self):

    casa_sola = "1.Cartagena, 2.Bogota , 3.Medellin"
    casa_compartida = "4.Barranquilla, 5.Cucuta, 6.Santa Marta "
    print("Si le gustaria estar SOLO ")
    solo = input("Digite si le gustaria estar solo o casa compartida:  ").lower()

    if solo == "solo":
      print(f"Le recomiendo estas casa {casa_sola} elija una de ellas")
      casa_solaa = int(input("Elija entre la opcion 1 2 o 3:  "))
      if casa_solaa == 1:
        print("Usted desea una casa de cartagena ")
      elif casa_solaa == 2:
        print("Usted desea una casa de bogota ")
      elif casa_solaa == 3:
        print("Usted desea una casa de Medellin ")


    elif solo == "Casa compartida":
      print(f"Casa compartida {casa_compartida}")
      casa_compartidaa = int(input("Elija entre la opcion 1, 2 o 3: "))
      if casa_compartidaa == 4:
        print("Usted desea una casa de Barranquilla")
      elif casa_compartidaa == 5:
        print("Usted desea una casa de Cucuta")
      elif casa_compartidaa == 6:
        print("Usted desea una casa de Santa Marta")


  def sugerir_mascota(self):
     animal = input("Deseas animal si o no: ").lower()
     if animal == "si":
      print("""      _________________
      |  1.PERRO       |
      |  2.GATO        |
      |  3.BALLENA     |
      |  4.AGUILA      |
      |  5.PEZ         |
      |  6.TIGRE       |
      |  7.Cual Deseas |
      |________________|""")
      mascota = int(input("Que mascotas deseas: "))
      if mascota == 1:
        print("Usted decidio tener un perro en su casa")

      elif mascota == 2:
        print("Usted decidio tener un gato en su casa")
      elif mascota == 3:
        print("Usted decidio tener una ballena  en su casa")
      elif mascota == 4:
         print("Usted decidio tener un aguila en su casa")
      elif mascota == 5:
         print("Usted decidio tener un pez en su casa")
      elif mascota == 6:
         print("Usted decidio tener un tigre en su casa")
      elif mascota == 7:
        print("Cual mascota deseas")
        mascota_deseada = input("Digite la mascota que desea")
        print(f"Usted eligio un/una {mascota_deseada}")

     elif animal == "no":
        print("Usted eligio que no desea animal en su casa: ")

  def sugerir_direccion(self):
      if self.opcion == 1:
        print(f" {self.opcion}  Bogota 1.olaya esta cerca de la playa 2.malambo esta de un campo 3.localidad kenenny parque de atraccion ")

        bogota = int(input("elija entre el 1 2 o 3: "))
        if bogota == 1:
          print("usted eligio olaya esta cerca de la playa")
        elif bogota == 2:
          print("usted eligio  malambo esta de un campo")
        elif bogota == 3:
          print("usted eligio localidad kenenny parque de atraccion")

      elif self.opcion == 2:
        print(f" {self.opcion}  Cartagena 1. cerca de un parque jurasico 2. cerca de un potrero 3. iglesia para rezar ")
        cartagena = int(input("elija entre el 1 2 o 3: "))
        if cartagena == 1:
          print("usted eligio cerca de un parque jurasico")
        elif cartagena == 2:
          print("usted eligio   cerca de un potrero")
        elif cartagena == 3:
          print("usted eligio iglesia para rezar")

      elif self.opcion == 3:
        print(f" {self.opcion}  Barranquilla 1. cerca de un centro comercial 2. cerca de un autodromo 3. cerca del campo ")
        barranquilla = int(input("elija entre el 1 2 o 3: "))
        if barranquilla == 1:
          print("usted eligio cerca de un centro comercial")
        elif barranquilla == 2:
          print("usted eligio  cerca de un autodromo")
        elif barranquilla == 3:
          print("usted eligio cerca del campo")
        else:
          print("el lugar que sea")

      elif self.opcion == 4:
        print(f" {self.opcion}  Cucuta 1. pozo azul  2. laguna de san luis 3.vientos del malecon ")
        cucuta = int(input("elija entre el 1 2 o 3: "))
        if cucuta == 1:
          print("usted eligio cerca de un pozo azul")
        elif cucuta == 2:
          print("usted eligio  cerca de una laguna llamada san luis")
        elif cucuta == 3:
          print("usted eligio cerca del viento del malecon")
        else:
          print("el lugar que sea")

      elif self.opcion == 5:
        print(f" {self.opcion}  Santa Marta 1.ciudad perdida  2. ciudad fastasma 3. parque nacional tairona ")
        santa_marta = int(input("elija entre el 1 2 o 3: "))
        if santa_marta == 1:
          print("usted eligio cerca de un centro comercial")
        elif santa_marta == 2:
          print("usted eligio  cerca de una ciudad fastasma ")
        elif santa_marta == 3:
          print("usted eligio cerca del parque nacional tairona")
        else:
          print("el lugar que sea")

      elif self.opcion == 6:
        print(f" {self.opcion}  Medellin 1.museo del oro  2.el rodadero  3. playa grande ")
        medellin = int(input("elija entre el 1 2 o 3: "))
        if medellin == 1:
          print("usted eligio cerca de un museo del oro ")
        elif medellin == 2:
          print("usted eligio  cerca de  el rodadero ")
        elif medellin == 3:
          print("usted eligio cerca de playa grande")
        else:
          print("el lugar que sea")

class PersonajeKen(DreamHouse):
  def __init__(self,tamano,color, num_habitaciones,name, edad, personalidad, profesion, username, password):
    super().__init__(tamano,color, num_habitaciones, username, password)
    self.profesion = profesion
    self.edad = edad
    self.name = name
    self.personalidad = personalidad
    self.emocion = random.choice(["Feliz","Triste", "Amargado", "cariñoso"])
    self.deseos = []


  def deseos_ken(self):
    whishesken = input("Digite su mayor deseo de acorde a sus necesidades del hogar: ")

    self.deseos.append(whishesken)
    print("Su mayor desseo es {}".format(self.deseos))

    for i,o in enumerate(self.deseos):
      print(f"{o}")

  def ken_saludo(self):
     print(f"""Hola yo soy {self.name} tengo {self.edad} años de edad, mi personalidad es {self.personalidad},
     mi {self.tamano}, el color de mi casa es {self.color}, el numero de mi casa es {self.num_habitaciones},
     la emocion que me caracteriza es {self.emocion},mi casa tiene balcon? {self.balcon}
     Mi casa tiene garaje? {self.garaje} """)



ken = DreamHouse("Tamaño de mi casa 100m2", "blanca", "2", "kendoctor", "pass123")
ken.login()
ken.lugar()
ken.sugerir_casa_sola_o_compartida()
ken.sugerir_mascota()
ken.sugerir_direccion()
DreamHouse.saludar()
ken1 = PersonajeKen("Tamaño de mi casa 100m2","blanca", "2","ken diego","24","ayudar a las demas personas","doctor", "kendoctor", "pass123")
ken1.deseos_ken()
ken1.ken_saludo()