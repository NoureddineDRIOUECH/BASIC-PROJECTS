# methof kayn f dictionnaire dial .get(hna kadir lkey li bghiti, o hna la nghiti dik chi default value la kan lkey makaynch aslan)
days = {1:"Mondaya",2:"Tuesday",3:"friday"}
print(days.get(1))
# string object
str = "         Noureddine  Driouech     "
str.capitalize() #hadi kathad awal 7arm mn kola kelma katdiro majuscle
str.center(30) #tbadel lpostion dialha f lconsole
str.upper() # kolchi majuscule
str.strip() # ila kano les espaces f lbadya kit7aydo  o ila kano f lakhar kiy7aydo
str.lower() # kolchi minuscule
str.replace("driouech","Zine") #hadi ra bayna
str.swapcase() #majucule iwali minuscule o lminuscule iwali majuscule
str.isprintable() #boolean o rah char7a rassha
str.isalnum() # wach kolchi ar9am
str.isalpha() # wach kamla string o mafiha 7ta espace
str.isdecimal() # wach ar9am
str.find("Driouech") #ki3tik l'index dial awal 7arf fiha fin kayn
str.isupper() # wach majuscule
str.rstrip() #hadi kat7ayed les espaces ghir f lekhar dial lkelma f7al leblan li kiw9a3 lk f gmail



# tuple

ls = [12,21,32]
ls.index(21) # te3tik l'index fin kayn dak l'element li 3ititiha
ls.remove(32) #atamssa7 dak l'element o tuple ra mata9darch temsse7



# OOP

# classes
 ## declaration class
class Person:

    def __init__(self,name): #constructer
        print("an obeject was created !")
        self.name = name
    def printname(self): # self darouri dirha kata3ni anna dik lfct ola l'arg ra tab3a lclass
        print(f"Hello {self.name} !")
## declatarion object
Noureddine = Person("Noureddine")
Noureddine.printname()

## toujours pour les class implementation faire self
## fefault value constructor

class Merson:

    def __init__(self, name = "Anaass"): # default constructer ila dekcalriti f lewel sf sinon ra par defaut smito anass
        print("an obeject was created !")
