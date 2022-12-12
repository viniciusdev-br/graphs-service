import graphviz
from models.graphs import RenderGraph

class GraphGenerator(object):
    def __init__(self):
        self.graph = graphviz.Graph('G', graph_attr={'rankdir': 'LR'})

    def render_graph(self, graph : RenderGraph):
        if(graph.oriented):
            self.graph = graphviz.Digraph('G', graph_attr={'rankdir': 'LR'})
        
        for edge in graph.edges:
            self.graph.edge(edge.start, edge.end, label=str(edge.weight))

        # generate graph image and return it in bytes
        return self.graph.pipe(format='png')

    def render_graph_topology(self, ordering, graph : RenderGraph):
        if(graph.oriented):
            self.graph = graphviz.Digraph('G', engine='dot')
            self.graph.attr(shape="circle", rankdir="TB", size="30.0", ordering='in', rank='same')
            with self.graph.subgraph() as level:
                for node_name in range(0, len(ordering)):
                    level.node(ordering[node_name])
                for edge_inv in range(0, len(ordering)-1):
                    level.edge(ordering[edge_inv], ordering[edge_inv+1], style='invis')
        
        for edge in graph.edges:
            self.graph.edge(edge.start, edge.end, label=str(edge.weight))

        # generate graph image and return it in bytes
        return self.graph.pipe(format='png')