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
        return item[pointer+1]

    def createAutomaton(self, items):
        stateName = "Q"+str(len(self.states))
        self.states.append((stateName, items))
        self.screen.add_node(stateName)
        self.screen.draw() 
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
            new_state = []
            for item in transitions[key]:
                key2, production = item
                production = self.movePoint(production)
                new_state.extend(self.closure((key2, production)))
            existsState = self.getExistStates(new_state)
            if existsState:
                self.screen.add_edge(stateName, existsState[0], key)
                self.transitions.append({"origin": stateName, "destination": existsState[0], "character":key})
            else:
                name = self.createAutomaton(new_state)
                self.transitions.append({"origin": stateName, "destination": name, "character": key})
                self.screen.add_edge(stateName, name, key)
            self.screen.draw()
            plt.pause(0.5)
        return stateName

    def movePoint(self, item: str):
        pointer = item.find(".")
        return item[:pointer] + item[pointer+1] + "." + item[pointer+2:]

    def getExistStates(self, state_param):
        for state in self.states:
            if set(state[1]) == set(state_param):
                return state
        return None
    
    