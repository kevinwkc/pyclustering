import unittest;

from gcolor.dsatur import dsatur;

from support import read_sample, read_graph;

from samples.definitions import GRAPH_SIMPLE_SAMPLES;

class Test(unittest.TestCase):
    def templateTestColoring(self, filename):
        graph = read_graph(filename);
        map_coloring = dsatur(graph.data);
        
        # Check number of colors
        assigned_colors = set(map_coloring);
        
        # Check validity of color numbers
        for color_number in range(1, len(assigned_colors) + 1, 1):
            assert color_number in assigned_colors;
            
        # Check validity of colors
        for index_node in range(len(graph.data)):
            color_neighbors = [ map_coloring[index] for index in range(len(graph.data[index_node])) if graph.data[index_node][index] != 0 and index_node != index];
            #print(index_node, map_coloring[index_node], color_neighbors, assigned_colors, map_coloring, "\n\n");
            assert map_coloring[index_node] not in color_neighbors;
    
    def testColoringFull1(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FULL1);
        
    def testColoringBrokenCircle1(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_BROKEN_CIRCLE1);
         
    def testColoringOneLine(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_LINE);
         
    def testColoringOneCircle1(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_CIRCLE1);
         
    def testColoringFivePointedStar(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FIVE_POINTED_STAR);
        
    def testColoringVerification(self):
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_BROKEN_CIRCLE1);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_BROKEN_CIRCLE2);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FIVE_POINTED_FRAME_STAR);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FIVE_POINTED_STAR);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FULL1);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_FULL2);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_CIRCLE1);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_CIRCLE2);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_CIRCLE3);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_CROSSROAD);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_ONE_LINE);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_SIMPLE1);
        self.templateTestColoring(GRAPH_SIMPLE_SAMPLES.GRAPH_TWO_CROSSROADS);
        
         

if __name__ == "__main__":
    unittest.main();