from variable import Variable
from numpy.random import choice


class Node(Variable):

	last_id = 0

	def __init__(self, domain: list = [], neighbors: list = []):
		super().__init__(domain=domain)
		self.neighbors = set(neighbors)
		# node id is a number that we will use to help the
		# networkx differentiate graph's nodes in the graph's plot
		Node.last_id += 1
		self.id = Node.last_id
  
	def add_neighbor(self, neighbor):
		'''
		This method adds a new neighbor to the self node
		'''
		self.neighbors.add(neighbor)

	def count_conflicts(self):
		'''
		This is an abstract method from Variable class that
		ia defined to return amount of constraints that have 
		conflict this variable's value.
		Here, it returns amount of neighbor nodes that
		have conflict with self node
		'''
		conflicts = 0
		for neighbor in self.neighbors:
			if neighbor.value == self.value:
				conflicts += 1
		return conflicts if self.value else -1
