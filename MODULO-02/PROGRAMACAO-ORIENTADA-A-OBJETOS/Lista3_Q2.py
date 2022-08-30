def main():
	class Bicicleta:
		def __init__(self, marca, cor):
			self.marca = marca
			self.cor = cor
			self.altura_cela = 6.0
			self.velocidade_atual = 0
			self.pressao_pneus = 15
			self.velocidade_max = 20

		def regular_cela(self, altura):
			if self.velocidade_atual == 0:
				if altura < 1.0:
					print('A cela foi regulada para uma altura minima de 2.0 cm')
					self.altura_cela = 2.0
				elif altura > 15.0:
					self.altura_cela = 15.0
					print('A cela foi regulada para uma altura maxima permitida de 15.0 cm')
				else:
					self.altura_cela = altura
					print(f'A altura da cela foi regulada para {self.altura_cela} cm.')
				
			else:
				print('Altura nao regulada, por favor, pare a bicicleta.')

		def calibrar_pneus(self, pressao):
			if self.velocidade_atual == 0:
				if pressao < 0:
					print('Pressao ajustada para o valor minimo possivel de 1 PSI')
					self.pressa_pneus = 1.0
				elif pressao > 30:
					print('A pressao foi ajustada para 30 PSI por conta do risco de estoura os pneus.')
					self.pressao_pneus = 30
				else:
					self.pressao_pneus = pressao
					print(f'A pressao dos pneus foram reguladas para {self.pressao_pneus} PSI.')
			else:
				print('Pressao nao regulada, por favor, pare a bicicleta')

		def acelerar(self, valor):
			if valor < 0:
				print('A bicicleta nao pode acelerar com valores negativos.')
			elif valor + self.velocidade_atual > 20:
				print('Velocidade atual da bicicleta ajustada para a maxima permitda: 20 km/h')
				self.velocidade_atual = self.velocidade_max
			else:
				self.velocidade_atual += valor
				print(f'Velocidade atual da bicicleta e de : {self.velocidade_atual} km/h')

		def frear(self, valor):
			if self.velocidade_atual > 0:
				if self.velocidade_atual - valor <= 0:
					self.velocidade_atual = 0
				else:
					self.velocidadade_atual -= valor
				print(f'A velocidade atual foi atualizada para: {self.velocidade_atual} km/h')
		
		def parar(self):
			self.velocidade_atual = 0

		def __str__(self):
			return f'Marca: {self.marca}, Cor: {self.cor}, Pressao nos Pneus: {self.pressao_pneus} PSI\nAltura da cela: {self.altura_cela} cm , Velocidade Atual: {self.velocidade_atual} km/h'

	print(" BIKE 1")
	bike1 = Bicicleta('Houston', 'Azul')
	bike1.acelerar(2)
	bike1.regular_cela(8)
	bike1.calibrar_pneus(25)
	bike1.parar()
	bike1.regular_cela(8)
	bike1.calibrar_pneus(25)
	print(">>> Dados da bike1 <<<")
	print(bike1)
	print(" ----------------------------------------- ")
	print(" BIKE 2")
	bike2 = Bicicleta('Cannondale', 'Vermelha')
	bike2.regular_cela(10)
	bike2.calibrar_pneus(22)
	bike2.acelerar(10)
	print(">>> Dados da bike2 <<<")
	print(bike2)


if __name__ == '__main__':
	main()
