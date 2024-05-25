"""
Semantic Graph Tests Workspace
"""

class Structure_Transition():
    def __init__(self):
        self.dictionnary = {}
    def verbial_struc(self, sentence : str):
        pass
    def adjec_struc(self, sentence : str):
        pass
    def prename_struc(self, sentence : str):
        pass







class DictAutomate():
    def __init__(self, transitions : [dict], final_state : int, initial_state=0):
        self.transitions = transitions
        self.final_state = final_state
        self.initial_state = initial_state
        def ddelete_occurence(my_list : list):
            new_list = []
            for k in my_list:
                if k not in new_list:
                    new_list.append(k)
            return new_list
        self.links = [ddelete_occurence([k for k in tr.values()]) for tr in transitions]
        pass
    def recognize(self, sentence : [str], state=0):
        if sentence == []:
            return (state== self.final_state)
        else:
            if sentence[0] in self.transitions[state]:
                return self.recognize(sentence[1:], self.transitions[state][sentence[0]])
            else:
                return False
    def recognize_sentence(self, sentence : str):
        return self.recognize(sentence.split(" "), self.initial_state)



test = DictAutomate([{"ab" : 1 , "aa" : 1 , "aaa" : 1 , "ba" : 1},{"bbbb" : 2 , "aaaa" : 0},{}] , 2)
test.recognize(["ab","bbbb"])



    
class StructurizeAutomate():
    def __init__(self):
        pass
    def transition(self, state : int, sequence):
        if len(sequence) == 0:
            return state
        else:
            pass
    def recognize(self, sentence : str):
        words_applied = sentence.split(" ")
class SemanticAutomate():
    def __init__(self , La : list):
        self.La = La
        pass
    def recognize(self, sentence : str):
        return [a.recognize_sentence(sentence) for a in La]
