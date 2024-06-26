import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-g', '--generate', action='store_true', help='auto generation')
group.add_argument('-u', '--user-provided', action='store_true', help='user provided list')

args = parser.parse_args()

if args.generate:
    saturation = int(input('saturation> '))
    nodes = int(input('     nodes> '))
    while True:
        representation = input('representation:\n1. List\n2. Matrix\n3. Table\n> ')
        match representation:
            case '1' | '1.':
                from Graph import Graph
                graph = Graph(nodes, mode='generate', saturation=saturation)
                break
            case '2' | '2.':
                from Graph_matrix import GraphMatrix
                graph = GraphMatrix(nodes, mode='generate', saturation=saturation)
                break
            case '3' | '3.':
                from Graph_table import GraphTable
                graph = GraphTable(nodes, mode='generate', saturation=saturation)
                break
            case _:
                print('Choose 1-3!')

elif args.user_provided:
    while True:
        representation = input('representation:\n1. List\n2. Matrix\n3. Table\n> ')
        match representation:
            case '1' | '1.':
                from Graph import Graph
                graph = Graph(int(input('nodes> ')))
                break
            case '2' | '2.':
                from Graph_matrix import GraphMatrix
                graph = GraphMatrix(int(input('nodes> ')))
                break
            case '3' | '3.':
                from Graph_table import GraphTable
                graph = GraphTable(int(input('nodes> ')))
                break
            case _:
                print('Choose 1-3!')

else:
    raise Exception("Must provide program's working mode!")


while True:
    action = input('action> ')
    match action.strip().lower():
        case 'print matrix' | 'pm':
            graph.print_matrix()
        case 'print list' | 'pl':
            graph.print_list()
        case 'print table' | 'pt':
            graph.print_table()
        case 'find edge' | 'f':
            frm = input('  from> ').strip()
            to = input('    to> ').strip()
            graph.find_edge(frm, to)
        case 'bfs':
            graph.bfs()
        case 'dfs':
            graph.dfs()
        case 'kahn' | 'ks':
            graph.kahn_sort()
        case 'tarjan' | 'ts':
            graph.tarjan_sort()
        case 'help' | 'h':
            print('''
+================================================================================+
|  Help          | h   |   Show this message                                     |
|  Print Matrix  | pm  |   Print matrix representation                           |
|  Print List    | pl  |   Print list representation                             |
|  Print Table   | pt  |   Print table representation                            |
|  Find Edge     | f   |   Check if the edge exists in the graph                 |
|  BFS           | bfs |   Breath-first search                                   |
|  DFS           | dfs |   Depth-first search                                    |
|  Kahn          | ks  |   Topological sort with Kahn algorithm                  |
|  Tarjan        | ts  |   Topological sort with Tarjan algorithm                |
|  Exit          | q   |   Exits the program (same as ctrl+D)                    |
+================================================================================+''')
        case 'exit' | 'q':
            break
        case _:
            print('command not found! type help')

