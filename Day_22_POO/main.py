class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.__ano = ano

    def buzinar(self):
        print("Biii! Biii!")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    def atualizar_ano(self, novo_ano):
        if novo_ano > 0:
            self.__ano = novo_ano
        else:
            print("\nAno Inválido! ")

    def atualizar_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def consultar_ano(self):
        return self.__ano

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano > 0:
            self.__ano = novo_ano
        else:
            print("\nAno Inválido! ")
            
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, capacidade_bateria):
        super().__init__(marca, modelo, ano)
        self.capacidade_bateria = capacidade_bateria

    def exibir_bateria(self):
        print(f"\nCapacidade da bateria: {self.capacidade_bateria} kWh")

    def buzinar(self):
        print("\nBiiiiii! Som de carro elétrico!")

class Moto():
    def buzinar(self):
        print("\nFom fom fom!")


gol = Carro("Volkswagen", "Gol", 2015)
tesla = CarroEletrico("Tesla", "Model 3", 2025, 75)
moto = Moto()

tesla.exibir_bateria()
gol.buzinar()
tesla.buzinar()
moto.buzinar()

print(tesla.marca)
print(tesla.modelo)
print(tesla.ano)
print(tesla.capacidade_bateria)

carro1 = Carro("Volkswagen", "Gol", 2015)
carro2 = Carro("Chevrolet", "Onix", 2023)

# Atualizando informações
carro1.atualizar_modelo("Fox")
carro1.atualizar_ano(2020)

carro2.ano = 2022
carro2.ano = -500

carro1.modelo = "T-Cross"
carro1.ano = 2024
carro2.ano = -100

# Exibindo informações
print("\n--- CARRO 1 ---")
carro1.exibir_informacoes()

print("\n--- CARRO 2 ---")
carro2.exibir_informacoes()

# Consultando os anos
print("\nAnos dos veículos:")
print(carro1.ano)
print(carro2.consultar_ano())