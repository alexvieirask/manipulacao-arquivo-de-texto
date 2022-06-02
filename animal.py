class Animal(object):
    def __init__(self, codigo_cadastro:int, nome_popular:str, peso:float, altura:str, classe:str) -> None:
        self.codigo_cadastro = codigo_cadastro
        self.nome_popular = nome_popular
        self.peso = peso
        self.altura = altura
        self.classe = classe
    
    def converter_txt(self, token:str=" // ") -> str:
        return str(self.codigo_cadastro) + token + self.nome_popular + token + str(self.peso) + token + self.altura + token + self.classe 

class AnimalCarnivoro(Animal):
    def __init__(self, codigo_cadastro:int,nome_popular: str, peso: float, altura:str,classe:str, consumidor:str, carne_necessaria:float) -> None:
        super().__init__(codigo_cadastro,nome_popular, peso, altura, classe)
        self.consumidor = consumidor # consumidor secundário ou consumidor terciário.
        self.carne_necessaria = carne_necessaria # Quantidade de carne necessaria por dia para suprir as necessidades do animal.
        
    def converter_txt(self, token:str=" // ") -> str:
        texto = super().converter_txt(token)
        return texto + token + self.consumidor + token + str(self.carne_necessaria) + token + "Car"

class AnimalHerbivoro(Animal):
    def __init__(self,codigo_cadastro:int, nome_popular: str, peso: float, altura: str,classe:str, classificacao:str,alimento_recomendado:str) -> None:
        super().__init__(codigo_cadastro,nome_popular, peso, altura, classe)
        self.classificacao = classificacao # Herbívoros pastadores ou Herbívoros podadores.
        self.alimento_recomendado = alimento_recomendado # O alimento que melhor supre as necessidades do animal.

    def converter_txt(self, token:str=" // ") -> str:
        texto = super().converter_txt(token)
        return texto + token + self.classificacao + token + self.alimento_recomendado + token + "Her"