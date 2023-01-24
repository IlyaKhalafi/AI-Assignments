from abc import ABC, abstractmethod
from numpy.random import choice

class Problem():
	
	def __init__(self, variables:list = []):
		self.variables = variables
 
	@abstractmethod
	def shuffle_assignment(self):
		'''
		Assigns random values to variables
		from their domains
		'''
		pass

	@abstractmethod
	def get_conflict(self):
		'''
		returns a random conflicted variable 
		returns None if there is no conflicted variable
		'''
		pass
 