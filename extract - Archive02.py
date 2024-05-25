from PyPDF2 import PdfReader
import os














class EncodeAutomate():
    def __init__(self, activation_function : dict):
        self.af = activation_function
        self.activation = {}
        def insere(sequence : str , sequence_list : [str]):
            if sequence_list == []:
                return [sequence]
            for inc in range(len(sequence_list)):
                if (len(sequence) >= len(sequence_list[inc])):
                    return sequence_list[:inc] + [sequence] + sequence_list[inc:]
        for sequence in self.af:
            if sequence[0] in self.activation:
                self.activation[sequence[0]] = insere(sequence, self.activation[sequence[0]])
            else:
                self.activation[sequence[0]] = [sequence]
    def sequence(self, sentence : str):
        def activation(work : str , sentence : str):
            assert len(work) == len(sentence)
            if len(work) == 0:
                return True
            else:
                if (work[0] == sentence[0]) or (sentence[0] == "¨"):
                    return activation(work[1:],sentence[1:])
                else:
                    return False
        my_new_sentence = ""
        increase = 0
        while increase < len(sentence):
            if sentence[increase] in self.activation:
                NotEqual = True
                sec_increase = 0
                while NotEqual and (sec_increase < len(self.activation[sentence[increase]])):
                    sequence = self.activation[sentence[increase]][sec_increase]
                    if increase + len(sequence) <= len(sentence):
                        if activation(sentence[increase:increase + len(sequence)],sequence):
                            my_new_sentence = my_new_sentence + self.af[sequence]
                            increase = increase + len(sequence)
                            NotEqual = False
                        else:
                            sec_increase += 1
                    else:
                        sec_increase += 1
                if NotEqual:
                    my_new_sentence = my_new_sentence + sentence[increase]
                    increase += 1
            else:
                my_new_sentence = my_new_sentence + sentence[increase]
                increase += 1
        return my_new_sentence



coder = EncodeAutomate({"-\n" : ""," - " : "\n - ","– ¨ – " : "" , "– ¨¨ – " : "" , "– ¨¨¨ – " : ""})
def test():
    reader = PdfReader("file.pdf")
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = text + coder.sequence((page.extract_text()).lower())
    print(text)
test()









"""
   
coder = EncodeAutomate({"a" : "c" , "aa" : "b"})
"""

