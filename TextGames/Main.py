# Autor: Angy Gorgoglione
# Data: 12/03/2024

import pickle



#Variaveis
Age_User = 1
Name_User = " "


print("\n\nSeja Bem Vindo ao TextGames!\n\n")


def Age():
    try:
        Age_User = int(input("Qual Sua Idade?: \n"))
        while True:
            if Age_User < 18:
                print("Idade não pode ser negativa")
                Age_User = int(input("Qual Sua Idade?: \n"))
            else:
                print("Você é maior de idade")
    except ValueError:
        print("Erro ao tentar acessar o texto")



class Personagem:
    def __init__(self, name, age, genero):
        self.name = name
        self.age = age
        self.genero = genero
        
    def save(self):
        with open(f'TextGames/UsersData/{self.name}.txt', 'w') as f:
            f.write(str(self.__dict__))
            print("save")
            
    @classmethod
    def load(cls, nome):
        with open(f'TextGames/UsersData/{nome}.pkl', 'rb') as f:
            return pickle.load(f)

    
def New_user(cls):
    
    Name_User = str(input("Como deseja ser chamado?: "))
    Gender_User = str(input("Entre com seu genero: "))
    return cls(Name_User, Age_User, Gender_User)
        


