import matplotlib.pyplot as plt
class Lr0:
    def __init__(self, grammar, screen):
        self.grammar = grammar
        self.states = []
        self.transitions = []
        self.screen = screen

    def validateExistTuples(sef, temp_tuples, response):
        for temp_tuple in temp_tuples:
            if temp_tuple not in response:
               return False
        return True
    

    def closure(self, key_item_tupla):
        item = key_item_tupla[1]
        key = key_item_tupla[0]
        response = [(key, item)]
        pointer = item.find(".")
        if pointer == len(item)-1:
            return response
        character = item[pointer+1]
        if character == key:
            return response
        if character in self.grammar["non_terminals"]:
            productions = self.grammar["productions"][character]
            for production in productions:
                response.extend(self.closure((character, "." + production)))
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
    
    def getCharacter(self, item):
        pointer = item.find(".")
        if pointer == len(item)-1 :
            return None
        if item[pointer+1] == "'":
            return item[pointer+1]+ "'" 
        else:
            return item[pointer+1]


    def createAutomaton(self, items):
        self.states.append(("I"+len(self.states), items))
        for item in items:
            key, production = item
            character = self.getCharacter(production)

            



            

        


        

    
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
        
