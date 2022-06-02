from animal import AnimalCarnivoro, AnimalHerbivoro

class OpcaoInvalida(Exception):
    def __init__(self, *args: object) -> None: # Ocorre quando o Usúario digita uma opção Inválida -  Código do Erro: [-7]
        super().__init__(*args)

class CodigoInvalido(Exception):
    def __init__(self, *args: object) -> None: # Ocoore quando o Usúario digita um código de cadastro Inválido - Código do Erro [-8]
        super().__init__(*args)

class NenhumCadastro(Exception):
    def __init__(self, *args: object) -> None: # Ocorre quando não existe nenhum animal cadastrado - Código do Erro [-9]
        super().__init__(*args)

class Gerenciador(AnimalCarnivoro): 
    def __init__(self) -> None:
        
        self.animais = []           # Lista com todos os animais
        self.animal_carnivoro = []  # Lista com apenas animais carnívoros
        self.animal_herbivoro = []  # Lista com apenas animais herbívoros

    def cadastrar_animal(self) -> int: # Método criado para realizar o cadastro de um animal
        try:
            tipo_animal = int(input("Digite 1 para cadastrar um animal carnívoro // Digite 2 para cadastrar um animal herbívoro: "))  # Escolher entre cadastrar um animal carnivoro ou herbívoro
            if tipo_animal == 1:   # Cadastrar um animal carnívoro
                print("________________")
                print("")
                self.cadastrar_animal_carnivoro()
            elif tipo_animal == 2: # Cadastrar um animal herbívoro
                print("________________")
                print("")
                self.cadastrar_animal_herbivoro()
            else:
                raise OpcaoInvalida 

        except OpcaoInvalida:
            print("Opção Inválida!")
            return -7
        return 0 

    def cadastrar_animal_carnivoro(self)-> int: # Método criado para realizar o cadastro de um animal carnívoro
        invalido = True
        while invalido:
            try:
                codigo_cadastro = int(input("Digite um código de cadastro:")) # Definir o código de cadastro do animal
                nome_popular = str(input("Digite o nome popular: "))          # Definir o nome popular do animal
                peso = float(input("Digite o peso do animal [kg]: "))         # Definir o peso do animal
                altura = str(input("Digite a altura do animal: "))            # Definir a altura do animal
                classe = str(input("Digite a classe do animal: "))            # Definir a classe do animal
                
                print("")
                print("O animal é consumidor terciário ou secundário?")       
                x  = 0 
                
                while not(x == 1 or x == 2):
                    x = int(input("Digite 1 para consumidor secundário // Digite 2 para consumidor terciário: ")) # Definir se o animal é um consumidor secundário ou terciário
                    if x == 1:
                        consumidor = "consumidor secundario"
                    elif x == 2:
                        consumidor = "consumidor terciario"
                    
                carne_necessaria = float(input("Digite a quantidade de carne necessaria que o animal precisa diariamente[kg]: ")) # Definir a quantidade de carne diaria que o animal precisa
                invalido = False

            except ValueError:
                print("O tipo do valor inserido é inválido!")
                print("Tente novamente")    
                return -10 

            novo_animal = AnimalCarnivoro(codigo_cadastro,nome_popular, peso, altura, classe, consumidor,carne_necessaria) 
            self.animais.append(novo_animal)          # Inserir animal na lista: animais
            self.verificar_codigo()
            self.animal_carnivoro.append(novo_animal) # Inserir animal na lista: animal_carnivoro

    def cadastrar_animal_herbivoro(self)-> int: # Método criado para realizar o cadastro de um animal herbívoro
        invalido = True
        while invalido:
            try:
                codigo_cadastro = int(input("Digite um código de cadastro:")) # Definir o código de cadastro do animal
                nome_popular = str(input("Digite o nome popular: "))          # Definir o nome popular do animal
                peso = float(input("Digite o peso do animal [kg]: "))         # Definir o peso do animal
                altura = str(input("Digite a altura do animal: "))            # Definir a altura do animal
                classe = str(input("Digite a classe do animal: "))            # Definir a classe do animal

                print("")
                print("O animal é um Herbívoro pastador ou podador?")
                x  = 0 
                while not(x == 1 or x == 2):
                    x = int(input("Digite 1 para Herbívoros pastador  // Digite 2 para Herbívoro podador: ")) # Definir se o animal é um herbívoro podador ou pastador
                    if x == 1:
                        classificacao = "Herbivoros pastador"
                    elif x == 2:
                        classificacao = "Herbivoro podador"
            
                alimento_recomendado = str(input("Digite o alimento recomendado destinado ao animal: ")) # Definir o alimento recomendado para o animal
                invalido = False
            
            except ValueError:
                print("O tipo do valor inserido é inválido!")
                print("Tente novamente")    
                return -10  
            
            novo_animal = AnimalHerbivoro(codigo_cadastro,nome_popular, peso, altura, classe, classificacao, alimento_recomendado)
            self.animais.append(novo_animal)          # Inserir animal na lista: animais
            self.verificar_codigo()
            self.animal_herbivoro.append(novo_animal) # Inserir animal na lista: animal_carnivoro

    def verificar_codigo(self)-> None: # Método criado para impedir que dois animais tenham o mesmo código de cadastro
        x = []
        for animais in self.animais:
            x.append(animais.codigo_cadastro)
            for i in x:
                if (x.count(i)> 1):
                    print("")
                    print("Este código já foi cadastrado anteriormente")
                    print("Utilize outro código!")
                    print("")
                    animais.codigo_cadastro = int(input("Digite o código de cadastro: "))
                    if animais.codigo_cadastro == i: 
                        self.verificar_codigo()
                    break
    
    def remover_animal(self)-> int: # Método criado para remover um animal das listas: animais, animal_carnivoro, animal_herbivoro
        lista_vazia = []
        try:
            if self.animais != lista_vazia:
                self.listar_animais()
                x = int(input("Digite o código de cadastro do animal que deseja remover: "))     
    
                invalido = 1 
            
                for animal in self.animais:
                    if x == animal.codigo_cadastro:
                        print("O animal [",animal.nome_popular,"] foi retirado do sistema!")
                        self.animais.remove(animal)                 # Removendo da lista: animais
                        invalido = 0
                
                if self.animal_carnivoro != lista_vazia:
                    for animal in self.animal_carnivoro:
                        if x == animal.codigo_cadastro:
                            self.animal_carnivoro.remove(animal)    # Removendo da lista: animal_carnivoro
                
                if self.animal_herbivoro != lista_vazia:
                    for animal in self.animal_herbivoro:
                        if x == animal.codigo_cadastro:
                            self.animal_herbivoro.remove(animal)    # Removendo da lista: animal_herbivoro
                
                if invalido == 1:
                    raise CodigoInvalido
            
            if self.animais == lista_vazia:
                raise NenhumCadastro
        
        except ValueError:
                print("O tipo do valor inserido é inválido!")
                return -10
        
        except CodigoInvalido:
            print("Código Inválido") 
            return -8
        
        except NenhumCadastro:
            print("Não existe nenhum animal cadastrado no sistema!") 
            return -9
        return 0

    def resetar_catalogo(self) -> int: # Método criado para resetar o catálogo de animais
        lista_vazia = []
        try:
            if self.animais != lista_vazia:
                self.animais =  [] 
                self.animal_carnivoro = []
                self.animal_herbivoro = []
                
                print("Todos os animais do seu catálogo foram excluidos!")
                print("Seu catálogo foi resetado!")
                return 0
            else:
                raise NenhumCadastro
        except NenhumCadastro:
            print("Não existe nenhum animal cadastrado!")
            return -9
            
    def caracteristicas_animal(self) -> int: # Método criado para que todos os atributos de um animal sejam vísiveis 
        try:
            lista_vazia = []
            invalido = False

            if self.animais != lista_vazia:
                self.listar_animais()
                x = int(input("Digite o código de cadastro no animal que você deseja ver as características: "))
                
                for i in self.animais:
                    if i.codigo_cadastro == x:
                        if self.animal_carnivoro != lista_vazia:
                            for animal in self.animal_carnivoro:
                                if animal.codigo_cadastro == x:
                                    print("")
                                    print("Código de cadastro:",animal.codigo_cadastro)         # Mostrar o codigo de cadastro do animal
                                    print("Nome popular:",animal.nome_popular)                  # Mostrar o nome popular do animal
                                    print("Peso:",animal.peso)                                  # Mostrar o peso do animal
                                    print("Altura:",animal.altura)                              # Mostrar a altura do animal
                                    print("Classe:",animal.classe)                              # Mostrar a classe do animal
                                    print("Consumidor:",animal.consumidor)                      # Mostrar qual qual o tipo do animal [ Consumidor secundário ou Consumidor terciário ]
                                    print("Carne necessária diaria:",animal.carne_necessaria)   # Mostrar a quantidade necessaria de carne que o animal necessita
                                    invalido = True

                        if self.animal_herbivoro != lista_vazia:
                            for animal in self.animal_herbivoro:
                                if animal.codigo_cadastro == x:
                                    print("")
                                    print("Código de cadastro:",animal.codigo_cadastro)         # Mostrar o codigo de cadastro do animal
                                    print("Nome popular:",animal.nome_popular)                  # Mostrar o nome popular do animal
                                    print("Peso:",animal.peso)                                  # Mostrar o peso do animal
                                    print("Altura:",animal.altura)                              # Mostrar a altura do animal
                                    print("Classe:",animal.classe)                              # Mostrar a classe do animal
                                    print("Classificação:",animal.classificacao)                # Mostrar a classificação do animal [ Herbivoro podador ou Herbívoro Pastador]
                                    print("Alimento recomendado:",animal.alimento_recomendado)  # Mostrar o alimento recomendado para o animal
                                    invalido = True
            else:
                raise NenhumCadastro
            
            if invalido == False:
                        raise CodigoInvalido

        except ValueError:
                print("O tipo do valor inserido é inválido!")
                return -10

        except CodigoInvalido:
            print("Código Inválido!")
            return -8

        except NenhumCadastro:
            print("Não existe nenhum animal cadastrado no sistema!")
            return -9

    def listar_animais(self) -> int: # Método criado para listar todos os animais de forma simples [ código de cadastro, nome popular, consumidor/classificação ]
        try:
            lista_vazia = []
            if self.animais != lista_vazia: 
                print("-------------- Animais Cadastrados ---------------")
                if self.animal_carnivoro != lista_vazia:
                    for i in self.animal_carnivoro:
                        print("Código de cadastro:",i.codigo_cadastro)  # Mostrar o código de cadastro do animal
                        print("Nome popular:",i.nome_popular)           # Mostrar o nome popular do animal
                        print("Consumidor:",i.consumidor)               # Mostrar qual qual o tipo do animal [ Consumidor secundário ou Consumidor terciário ]
                        print("________________________")

                if self.animal_herbivoro!= lista_vazia:
                    for i in self.animal_herbivoro:
                        print("Código de cadastro:",i.codigo_cadastro)  # Mostrar o código de cadastro do animal
                        print("Nome popular:",i.nome_popular)           # Mostrar o nome popular do animal
                        print("Classificação:",i.classificacao)         # Mostrar a classificação do animal [ Herbivoro podador ou Herbívoro Pastador]
                        print("________________________")
                    
                return 0 
            else:
                raise NenhumCadastro
        except NenhumCadastro:
            print("Não existe nenhum animal cadastrado no sistema!")
            return -9
    
    def retornar_animais(self) -> list: # Método criado para retornar a lista com todos os animais cadastrados
        return self.animais

    def definir_arquivo(self) -> str:   # Método criado para definir qual o nome do arquivo que será salvo
        lista_vazia = []
        if self.animais != lista_vazia:
            nome_arquivo = str(input("Digite o nome do arquivo que será salvo:"))
        else:
            print("Não existe nenhum animal cadastrado!")
            nome_arquivo = "Nenhum animal cadastrado"
        return nome_arquivo
    
    def retornar_arquivo_recuperar(self)-> str: # Método criado para retornar o nome do arquivo que será recuperado
        nome_arquivo = str(input("Digite o nome do arquivo que vai ser recuperado:"))
        return nome_arquivo + ".txt"