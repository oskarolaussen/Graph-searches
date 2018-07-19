'''This is an implementation of bredth first search for graphs. It takes as input a graph (dictionary), the starting node and a list of nodes
and outputs the order that the nodes were visited in.'''

def bfs(g, starting_node, list_of nodes):
	visited_but_not_finished, finished = [], []
	unvisited=list_of_nodes
	visited_but_not_finished.append(starting_node)
	unvisited.remove(starting_node)
	while visited_but_not_finished:
		x=visited_but_not_finished.pop(0)
		for y in g[x]:
			if y in unvisited:
				visited_but_not_finished.append(y)
				unvisited.remove(y)
		finished.append(x)
	return finished;

graph={'A':['B','C','D'], 'B':['A','E'], 'C':['A','D','G'], 'D':['A','C'], 'E':['B','F'], 'F':['E'], 'G':['C']}
nodes=['A','B','C','D','E','F','G']
order_of_visitation=bfs(graph, 'A', nodes)
print(order_of_visitation)