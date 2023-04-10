class Proyecto(object):
	"""docstring for ClassName"""
	def __init__(self, ganancia:int,prestigio:int)->None:
		self.ganancia = ganancia
		self.prestigio = prestigio

	def valoracion()->(int,int):
		return self.ganancia,self.prestigio

	def __str__(self)->str:
		return f" Proyecto: ganancia = {self.ganancia}, prestigio = {self.prestigio} "

		