from gerenciador import Gerenciador, OpcaoInvalida
from gravador import GravadorAnimal

class Interface(GravadorAnimal,Gerenciador): 

    def mostrar_interface(self)-> None:
        print("-------------- Cadastro de Animais   --------------") # Software desenvolvido com o objetivo de realizar o cadastro de animais em um zoológico
        print("        1 - Cadastrar um animal                    ") 
        print("        2 - Remover um animal                      ") 
        print("        3 - Listar todos os animais                ")              
        print("        4 - Caracteristicas do animal              ") 
        print("        5 - Gravar os animais                      ")
        print("        6 - Recuperar animais                      ")
        print("        7 - Resetar estoque do catálogo            ")
        print("        8 - Sair                                   ")
        print("---------------------------------------------------")
    
    def main(self) -> int:
        sair = False
        
        while not sair:
            try:
                self.mostrar_interface()
                escolha = int(input("Escolha uma opção: "))
            
                if escolha == 1:            # Opção responsável por realizar o cadastro de um animal
                    self.cadastrar_animal() 

                elif escolha == 2:          # Opção responsável por realizar a remoção de um animal
                    self.remover_animal()   

                elif escolha == 3:          # Opção responsável por realizar a listagem dos animais de forma simples [ código de cadastro, nome popular, consumidor/classificação ]
                    self.listar_animais()   

                elif escolha == 4:          # Opção responsável por mostrar todas as caracteristicas de um animal   
                    self.caracteristicas_animal() 

                elif escolha == 5:          # Opção responsável por gravar e salvar os animais cadastrados
                    self.gravar()          

                elif escolha == 6:          # Opção responsável por recuperar os animais que foram salvos
                    self.recuperar()        
                
                elif escolha == 7:          # Opção responsável por resetar o catálogo de animais
                    self.resetar_catalogo()

                elif escolha == 8:          # Opção responsável por realizar o encerramento do software
                    sair = True
                else:
                    raise OpcaoInvalida

            except ValueError:
                print("O tipo do valor inserido é inválido!")
                self.main()
                return -10

            except OpcaoInvalida:
                print("Opção Inválida!")
                self.main()
                return -7
        return 0

app = Interface()
app.main()