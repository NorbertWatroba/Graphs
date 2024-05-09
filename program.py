from Graph import Graph

graph = Graph(int(input('nodes> ')))

while True:
    action = input('action> ')
    match action.strip().lower():
        case 'print matrix' | 'pm':
            graph.print_matrix()
        case 'print list' | 'pl':
            graph.print_list()
        case 'find edge' | 'f':
            frm = input('from> ').strip()
            to = input('  to> ').strip()
            graph.find_edge(frm, to)
        case 'bfs':
            graph.bfs()
        case 'dfs':
            graph.dfs()
        case 'exit' | 'q':
            break
        case _:
            print('command not found! type help')

