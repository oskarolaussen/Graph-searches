'''This is an implementation of the depth first search for graphs. It takes as input an graph (dictionary) and starting node
and outputs the order the nodes were visited.'''

def dfs(g, starting_node, visited=None):
	if visited==None:
		visited=[]
	visited.append(starting_node)
	for x in g[starting_node]:
		if x not in visited:
			dfs(g, x, visited)
	return visited;

graph={'A':['B','C','D'], 'B':['A','E'], 'C':['A','D','G'], 'D':['A','C'], 'E':['B','F'], 'F':['E'], 'G':['C']}

order_of_visitation=dfs(graph, 'B')
print(order_of_visitation)