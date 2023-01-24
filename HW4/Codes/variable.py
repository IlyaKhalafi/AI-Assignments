from abc import ABC, abstractmethod

class Variable(ABC):
    
	def __init__(self, domain:list = []):
		self.domain = domain
		self.value = None
        
	@abstractmethod
	def count_conflicts(self):
		'''
		returns amount of constraints that have 
		conflict this variable's value
		'''
		pass
    