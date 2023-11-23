def debruijn_from_pairs(kmer_pairs):
    sequence_map = {}
    for pair in kmer_pairs:
        head = (pair[0][:-1], pair[1][:-1])
        tail = (pair[0][1:], pair[1][1:])

        if head in sequence_map:
            sequence_map[head].append(tail)
        else:
            sequence_map[head] = [tail]
    return sequence_map

def computeeulerian(sequence_graph):
    incount = {}
    outcount = {}
    for vertex, adjacents in sequence_graph.items():
        if vertex not in incount:
            incount[vertex] = 0
        if vertex not in outcount:
            outcount[vertex] = 0

        outcount[vertex] += len(adjacents)
        for adjacent in adjacents:
            if adjacent not in incount:
                incount[adjacent] = 0
            if adjacent not in outcount:
                outcount[adjacent] = 0
            incount[adjacent] += 1

    begin_vertex = None
    for vertex, out_degree in outcount.items():
        if out_degree > incount[vertex]:
            begin_vertex = vertex
            break

    if begin_vertex == None:
        begin_vertex = next(iter(sequence_graph))

    route = []
    stack = [begin_vertex]

    current_vertex = begin_vertex

    while stack:
        if current_vertex in sequence_graph and sequence_graph[current_vertex]:
            stack.append(current_vertex)
            current_vertex = sequence_graph[current_vertex].pop()
        else:
            route.append(current_vertex)
            current_vertex = stack.pop()

    return route[::-1]

def get_paired_sequence(route, kmer_size, gap):
    head_str = route[0][0]
    tail_str = route[0][1]

    for idx in range(1, len(route)):
        head_str += route[idx][0][-1]
        tail_str += route[idx][1][-1]
    return head_str + tail_str[-( kmer_size + gap):]

data_file = 'reconstruct.txt'

with open(data_file, 'r') as data:
    kmer_size, gap = map(int, data.readline().strip().split())
    pairs = [tuple(line.strip().split('|')) for line in data.readlines()]

sequence_map = debruijn_from_pairs(pairs)
route = computeeulerian(sequence_map)
output_str = get_paired_sequence(route, kmer_size, gap)

result_file = 'result.txt'
with open(result_file, 'w') as result:
    result.write(output_str)