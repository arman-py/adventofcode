data = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


import networkx as nx


if __name__ == "__main__":
    split_data = data.split("\n")
    mappings = {}
    for line in split_data:
        s, e = line.split(':')
        for y in e.split():
            if s in mappings:
                mappings[s].add(y)
            else:
                mappings[s] = {y}
            if y in mappings:
                mappings[y].add(s)
            else:
                mappings[y] = {s}

    graph = nx.DiGraph()
    for k, vs in mappings.items():
        for v in vs:
            graph.add_edge(k, v, capacity=1.0)
            graph.add_edge(v, k, capacity=1.0)

    for x in [list(mappings.keys())[0]]:
        for y in mappings.keys():
            if x != y:
                cut_value, (i, j) = nx.minimum_cut(graph, x, y)
                if cut_value == 3:
                    print(len(i) * len(j))
                    break
