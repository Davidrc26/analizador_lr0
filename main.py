from view.screen import Screen
import matplotlib.pyplot as plt
import lr0.lr0 as lr0File 
import json
from pprint import pprint

def load_grammar(file):
    with open(file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    grammar = load_grammar('grammars/prueba1.json')
    lr0_instance = lr0File.Lr0(grammar, Screen())
    ##result = lr0_instance.closure(('S','.E$')) 
    ##print(lr0_instance.movePoin('.E$'))
    ##lr0_instance.createAutomaton()
    ##print(result)  

    plt.ion()
    start_symbol= lr0_instance.grammar["start_symbol"]
    start_production = lr0_instance.grammar["productions"][start_symbol][0]
    lr0_instance.createAutomaton(lr0_instance.closure((start_symbol, "."+start_production)))
    plt.show(block=True)

    pprint(lr0_instance.states)
    """  pprint(lr0_instance.transitions) """


    """ lr0_instance.states = [("I0", lr0_instance.closure(('S','.E$')))]
    print(lr0_instance.getExistStates(lr0_instance.states[0][1])) """

    
    


    """ plt.ion()
    s = Screen()
    s.add_node(1)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_node(2)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_node(3)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_node(4)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_edge(1, 2)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_edge(2, 3)
    s.draw()
    plt.draw()
    plt.pause(1)
    s.add_edge(3, 4)
    s.draw()
    plt.draw()
    plt.pause(1)
    plt.show(block=True) """

