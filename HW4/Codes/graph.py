from problem import Problem
from node import Node
import networkx as nx
import matplotlib.pyplot as plt
from numpy.random import choice

class Graph(Problem):
    
	def __init__(self, nodes:list = []):
		self.nodes = nodes
		super().__init__(variables=self.nodes)
  
	def random(num_nodes:int, prob:float = 0.5, domain:list = []):
		'''
		This method returns an instance of graph class
		with random structure, arguments are:
			nums_nodes = amount of the nodes in the graph
			prob = probility for each edge to be present in the graph,
					this arg will be used to control density of edges.
					This arg should be in range [0, 1]
			domain = domain of each node of the graph will be set to this arg
		'''
		g = Graph(nodes = [Node(domain=domain) for _ in range(num_nodes)])
		for i in range(num_nodes):
			for j in range(i+1, num_nodes):
				if choice([0, 1], p=[1-prob, prob]):
					g.add_edge(i, j)
		return g
		
	def shuffle_assignment(self):
		'''
		Assigns random values to variables
		from their domains
		'''
		for var in self.variables:
			var.value = choice(var.domain)
  
	def add_edge(self, node1_index:int, node2_index:int):
		'''
		This method takes index of two nodes in its internal
		nodes list and add an edge between  
		Adding edge between 2 nodes of graph
		'''
		self.nodes[node1_index].add_neighbor(self.nodes[node2_index])
		self.nodes[node2_index].add_neighbor(self.nodes[node1_index])

	def get_conflict(self):
		'''
		returns a random conflicted variable 
		returns None if there is no conflicted variable
		'''
		conflicted = []
		for node in self.nodes:
			if node.count_conflicts() != 0:
				conflicted.append(node)

		# Pick and return a random conflcited variable using choice method
		# Notice that empty lists are considered as False in python
		return choice(conflicted) if conflicted else None

	def visualize(self):
		'''
		Drawing picture of graph using networkx library.
		To use networkx, we make an instance of networkx Graph class
		and add nodes of our graph to this instance, the we add edges
		of each node to this instance
		'''
		G = nx.Graph()
		for node in self.nodes:
			G.add_node(node)
			for neighbor in node.neighbors:
				G.add_edge(node, neighbor)
		nx.draw(G, 
                node_color=[node.value if node.value != None else 'black' for node in list(G.nodes)],
            	labels={node:node.id for node in list(G.nodes)}
             )
		plt.show()
