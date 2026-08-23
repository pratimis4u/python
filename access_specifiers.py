class Super:
	var1 = None
	_var2 = None
	__var3 = None
	def __init__(self, var1, var2, var3): 
		self.var1 = var1
		self._var2 = var2
		self.__var3 = var3
	def PublicM(self):
		print("Public", self.var1)
	def _ProtectM(self):
		print("Protected ", self._var2)
	def __PrivateM(self):
		print("Private", self.__var3)
	def accessPrivateM(self):	
		self.__PrivateM()
class Sub(Super):
	def __init__(self, var1, var2, var3): 
				Super.__init__(self, var1, var2, var3)
	def accessProtectM(self):
				self._ProtectM()
obj = Sub("abc", "hii", "pqr") 
obj.PublicM()
obj.accessProtectM()
obj.accessPrivateM()
print("accessing protected", obj._var2)