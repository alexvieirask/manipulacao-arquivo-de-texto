from gerenciador import Gerenciador
from animal import Animal, AnimalCarnivoro, AnimalHerbivoro

class GravadorAnimal(Gerenciador,Animal):

    def gravar(self)->int: # Método responsável por gravar/salvar os animais que foram cadastrados
        lista_animais = self.retornar_animais()
        nome_arquivo = self.definir_arquivo() 

        if nome_arquivo != "Nenhum animal cadastrado":
            nome_arquivo = nome_arquivo + ".txt"
            try:
                arquivo = open(nome_arquivo, "x")
                arquivo.close()
            except FileExistsError:
                print("Já existe esse arquivo!")
                return -1
            except PermissionError:
                print("Você não tem autorização de gravar aqui!")
                return -2
            except OSError:
                print("Deu um erro indesejado!")
                return -3
            
            print("Sucesso! Todos os animais foram gravados!")
            arquivo = open(nome_arquivo, "w")
            for animal in lista_animais:
                arquivo.write(animal.converter_txt()+"\n")
            arquivo.close()
            return 0

    def recuperar(self, token:str=" // ") -> int: # Método responsável por recuperar os animais que foram salvos em um arquivo
        nome_arquivo = self.retornar_arquivo_recuperar()
        lista_vazia = []
        try:
            arquivo = open(nome_arquivo, "r")
        except FileNotFoundError:
            print("Nenhum arquivo foi encontrado!")
            return -4
        except PermissionError:
            print("Você não tem autorização de gravar aqui!")
            return -2
        except OSError:
            print("Deu um erro indesejado!")
            return -3
        
        for linha in arquivo.readlines():
                linha = linha.replace("\n", "")
                dados = linha.split(token)
                
                if dados[len(dados)-1] == "Car":
                    animal = AnimalCarnivoro(int(dados[0]),dados[1], float(dados[2]), dados[3], dados[4], dados[5], float(dados[6]))
                    self.animais.append(animal)
                    self.animal_carnivoro.append(animal)
                
                else: 
                    animal = AnimalHerbivoro(int(dados[0]),dados[1], float(dados[2]), dados[3], dados[4], dados[5], dados[6])
                    self.animais.append(animal)
                    self.animal_herbivoro.append(animal)

        if self.animais != lista_vazia:
            print("Os animais do arquivo",nome_arquivo,"foram recuperados e adicionados ao catálogo!")
        arquivo.close()
        return 0