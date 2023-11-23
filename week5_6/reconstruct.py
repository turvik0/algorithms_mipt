def eulerian_path(graph):
    indegree = {}
    outdegree = {}
    for node, neighbors in graph.items():
        if node not in indegree:
            indegree[node] = 0
        if node not in outdegree:
            outdegree[node] = 0

        outdegree[node] += len(neighbors)
        for i in neighbors:
            if i not in indegree:
                indegree[i] = 0
            if i not in outdegree:
                outdegree[i] = 0
            indegree[i] += 1

    start = ''
    for node, degree in outdegree.items():
        if degree > indegree[node]:
            start = node
            break

    if start == '':
        start = next(iter(graph))

    path = []
    st = [start]

    curr = start

    while len(st) > 0:
        if curr in graph and graph[curr]:
            st.append(curr)
            curr = graph[curr].pop()
        else:
            path.append(curr)
            curr = st.pop()

    return path[::-1]

def debruijn_pair(paired_kmers):
    graph = {}
    for paired_kmer in paired_kmers:
        prefix = (paired_kmer[0][:-1], paired_kmer[1][:-1])
        suffix = (paired_kmer[0][1:], paired_kmer[1][1:])

        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    return graph

def paired_path(path, k, d):
    prefix_string = path[0][0]
    suffix_string = path[0][1]

    for i in range(1, len(path)):
        prefix_string += path[i][0][-1]
        suffix_string += path[i][1][-1]

    return prefix_string + suffix_string[len(suffix_string) - k - d:]

input_filename = 'reconstruct.txt'

with open(input_filename, 'r') as infile:
    k, d = map(int, infile.readline().strip().split())
    paired_reads = [tuple(line.strip().split('|')) for line in infile.readlines()]

graph = debruijn_pair(paired_reads)
path = eulerian_path(graph)
result = paired_path(path, k, d)

output_filename = 'output.txt'
with open(output_filename, 'w') as outfile:
    outfile.write(result)