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
    plt.ion()
    start_symbol= lr0_instance.grammar["start_symbol"]
    start_production = lr0_instance.grammar["productions"][start_symbol][0]
    lr0_instance.createAutomaton(lr0_instance.closure((start_symbol, "."+start_production)))
    lr0_instance.screen.paintSinks()
    lr0_instance.screen.draw()
    lr0_instance.screen.showInfo(lr0_instance.states)
    plt.show(block=True)

