
class Grammar:
    def __init__(self, terminals, non_terminals, productions, start_symbol):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def __str__(self):
        return f"Terminals: {self.terminals}\nNon-terminals: {self.non_terminals}\nProductions: {self.productions}\nStart symbol: {self.start_symbol}"

    def __repr__(self):
        return f"Grammar({self.terminals}, {self.non_terminals}, {self.productions}, {self.start_symbol})"

class Lr0:
    def __init__(self, grammar):
        self.grammar = grammar
        self.states = []
        self.transitions = []

    def closure(self, item: str, pointer):
        response = [item]
        character = item[pointer]
        if character in self.grammar["non_terminals"]:
            productions = self.grammar["productions"][character]
            for production in productions:
                response.extend(self.closure(production, 0))  
        return response
    

    def remove_left_recursion(self):
        for key in self.grammar["non_terminals"]:
            productions = self.grammar["productions"][key]
            hasRecursion = False
            for production in productions:
                if production != "":
                    if production[0] == key:
                        hasRecursion = True
                        self.grammar["productions"][key] = []
                        self.grammar["non_terminals"].append(key+"'")
                        if key+"'" not in self.grammar["productions"].keys():
                            self.grammar["productions"][key+"'"] = []
                        self.grammar["productions"][key+"'"].extend([production[1:] + key + "'"])
                    elif hasRecursion:
                        self.grammar["productions"][key].extend([production + key + "'"])
            if hasRecursion:
                self.grammar["productions"][key+"'"].append("")
    
    """ def remove_left_recursion(self):
        for non_terminal in self.grammar['non_terminals']:
            # Buscar producciones que tienen recursión por la izquierda
            recursive_productions = [p for p in self.grammar['productions'][non_terminal] if p and p[0] == non_terminal]
            non_recursive_productions = [p for p in self.grammar['productions'][non_terminal] if not p or p[0] != non_terminal]

            if recursive_productions:
                # Crear un nuevo símbolo no terminal
                new_non_terminal = non_terminal + "'"
                self.grammar['non_terminals'].append(new_non_terminal)

                # Reemplazar las producciones recursivas por la izquierda
                self.grammar['productions'][non_terminal] = [p + new_non_terminal for p in non_recursive_productions]
                self.grammar['productions'][new_non_terminal] = [p[1:] + new_non_terminal for p in recursive_productions] + [''] """
        
