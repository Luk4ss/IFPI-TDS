def main():
	class Relogio:
		def __init__(self, horas=0, minutos=0):
			self.horas = horas
			self.minutos = minutos
			self.segundos = 0
			self.bateria = True
			self.vida_util = 9999999

		def ajustar_horas(self, hora):
			self.vida_util -= 1
			if self.vida_util <=0:
				self.bateira = False
			if self.bateria:
				if hora < 0:
					self.horas = 0
				elif hora > 23:
					while hora > 23:
						hora -= 23
					self.horas = hora
				else:
					self.horas = hora
		
		def ajustar_minutos(self, minuto):
			self.vida_util -= 1
			if self.vida_util <=0:
				self.bateira = False
			if self.bateria:
				if minuto < 0:
					self.minutos = 0
				elif minuto > 59:
					while minuto > 59:
						minuto -= 59
					self.minutos = minuto
				else:
					self.minutos = minuto
		
		def incrementar_tempo(self):
			self.segundos += 1
			if self.segundos > 59:
				self.minutos += 1
				self.segundos = 0
			if self. minutos > 59:
				self.minutos = 0
				self.horas += 1
			if self.horas > 23:
				self.horas = 0
			

		def __str__(self):
			if self.horas < 10 and self.minutos < 10:
				return f'Hora Atual: 0{self.horas}:0{self.minutos}'
			if self.horas < 10:
				return f'Hora Atual: 0{self.horas}:{self.minutos}'
			elif self.minutos < 10:
				return f'Hora Atual: {self.horas}:0{self.minutos}'
			return f'Hora Atual: {self.horas}:{self.minutos}'
			


	
	relogio1 = Relogio(15,35)
	print('>>>> RELOGIO 1 <<<<')
	print(relogio1)
	relogio1.incrementar_tempo()
	relogio2 = Relogio()
	print(">>>> RELOGIO 2 <<<<")
	print(relogio2)
	relogio2.incrementar_tempo()
	relogio2.ajustar_horas(15)
	print(">>>> RELOGIO 2 <<<<")
	print(relogio2)
	print('>>>> RELOGIO 1 <<<<')
	relogio1.ajustar_minutos(10)
	relogio1.incrementar_tempo()
	print(relogio1)


if __name__ == "__main__":
	main()
