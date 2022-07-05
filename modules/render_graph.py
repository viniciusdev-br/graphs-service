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
