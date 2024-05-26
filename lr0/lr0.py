import matplotlib.pyplot as plt


class Lr0:
    def __init__(self, grammar, screen):
        self.grammar = grammar
        self.states = []
        self.transitions = []
        self.states_acceptance = []
        self.screen = screen

    def closure(self, key_item_tupla):
        item = key_item_tupla[1]
        key = key_item_tupla[0]
        response = [(key, item)]
        pointer = item.find(".")
        if pointer == len(item)-1:
            return response
        character = item[pointer+1]
        if character == key and pointer == 0:
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
                        self.grammar["productions"][key +
                                                    "'"].extend([production[1:] + key + "'"])
                    elif hasRecursion:
                        self.grammar["productions"][key].extend(
                            [production + key + "'"])
            if hasRecursion:
                self.grammar["productions"][key+"'"].append("")

    def getCharacter(self, item):
        pointer = item.find(".")
        if pointer == len(item)-1:
            return None
        if item[pointer+1] == "'":
            return item[pointer+1] + "'"
        else:
            return item[pointer+1]

    def createAutomaton(self, items):
        stateName = "I"+str(len(self.states))
        self.states.append((stateName, items))
        ##self.screen.add_node(stateName)
        ##self.screen.draw()
        ##plt.pause(1)
        new_state = []
        transitions = {}
        if not items:
            return
        for item in items:
            key, production = item
            character = self.getCharacter(production)
            if character:
                if character not in transitions:
                    transitions[character] = [item]
                else:
                    transitions[character].append(item)
        transitionsKeys = transitions.keys()
        for key in transitionsKeys:
            for item in transitions[key]:
                key, production = item
                production = self.movePoint(production)
                new_state.extend(self.closure((key, production)))
            existsState = self.getExistStates(new_state)
            if existsState:
                ##self.screen.add_edge(stateName, existsState[0])
                self.transitions.append({
                    "from": stateName,
                    "to": existsState[0],
                    "label": key
                })
            else:
                self.states.append(("I"+str(len(self.states)), new_state))
                self.transitions.append({
                    "from": stateName,
                    "to": "I"+str(len(self.states)-1),
                    "label": key
                })

            ##self.screen.add_edge(stateName, "I"+str(len(self.states)))
            ##self.screen.draw()
            ##plt.pause(1)

    def movePoint(self, item: str):
        pointer = item.find(".")
        return item[:pointer] + item[pointer+1] + "." + item[pointer+2:]

    def getExistStates(self, state_param):
        list_states = [state[1] for state in self.states]
        for state in list_states:
            if set(state) == set(state_param):
                return state
        return None

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
