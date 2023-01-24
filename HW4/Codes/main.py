from graph import Graph
from node import Node
from solver import MinConflictSolver

if __name__ == '__main__':
	G = Graph.random(10, prob=1/3, domain=['blue', 'green', 'red', 'yellow'])
	solver = MinConflictSolver(G)
	
	cnt = 1
	while not solver.step() and cnt < 1000:
		conflicts_amo = sum([var.count_conflicts() for var in G.variables])
		print(f'Iteration {str(cnt)}: {conflicts_amo} conflicts')
		G.visualize()	
		cnt += 1
  
	if cnt == 1000:
		print('No solution found')
	else:
		print(F'Solution found in {str(cnt)} steps')
		G.visualize()
