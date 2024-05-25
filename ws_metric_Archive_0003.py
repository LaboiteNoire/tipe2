"""
Metric System
"""
import matplotlib.pyplot as plt
import threading
import os
import io
import pickle
import csv
import encoder as EC








def load(path="database.obj"):
    fileout = open(path,"rb")
    Load = pickle.load(fileout) 
    fileout.close()
    return Load
def word_adition_from_a_list(my_list : [str]):
    my_txt = ""
    for pattern in my_list:
        my_txt = my_txt + pattern
    return my_txt
def test_import():
    fileIn = open("text for test.txt","r",encoding="utf-8")
    content = fileIn.readlines()
    fileIn.close()
    return word_adition_from_a_list(content)
def import_txt():
    fileIn = open("text.txt","r",encoding="utf-8")
    content = fileIn.readlines()
    fileIn.close()
    return word_adition_from_a_list(content)







def shearch_patterns(txt : str, i : int, pattern : str):
    return (((i + len(pattern)) <= len(txt)) and (txt[i:i + len(pattern)] == pattern))
def get_sentence_list(my_txt=test_import()):
    assert(len(my_txt) > 1)
    coder = EC.EncodeAutomate({"\n" : " ","--" : "","_" : "","«" : "" , "»" : "" ,"," : "", ";" : "", ":" : ""})
    accept_dict = {"." : None, "!" : None, "?" : None}
    initialize_list = []
    head_play = 0
    in_stand = True
    for i in range(1,len(my_txt)):
        if (my_txt[i] != (my_txt[i].lower())) and (not shearch_patterns(my_txt,i,"M. ")) and (not in_stand):
            head_play = i
            in_stand = True
        elif (my_txt[i] in accept_dict) and (my_txt[i-1] != "M") and in_stand:
            initialize_list.append(coder.sequence(my_txt[head_play:i]))
            in_stand = False
        elif i == (len(my_txt) - 1):
            initialize_list.append(coder.sequence(my_txt[head_play:i]))
    return initialize_list
def get_space_words():
    fileIn = open("liste_francais.txt","r")
    content = [(line[:len(line) - 1]) for line in fileIn.readlines() if (" " in line[:len(line) - 1])]
    fileIn.close()
    return content
def sub_analyse(word : str, work_list : [str] , word_dict : dict):
    if work_list == []:
        return (word,[])
    elif (word + " " + work_list[0]) not in word_dict:
        return (word,work_list)
    else:
        return sub_analyse(word + " " + work_list[0],work_list[1:],word_dict)
def init_analyse(work : [str], non_list : [str], words_with_space : dict):
    if work == []:
        return non_list
    else:
        results = sub_analyse(work[0],work[1:],words_with_space)
        return init_analyse(results[1],non_list + [results[0]],words_with_space)
def get_words_list_of_a_sentence(sentence : str, words_with_space : dict):
    my_stock = sentence.split()
    return init_analyse(my_stock, [], words_with_space)
    pass
def encapsule(n : int , file_procc : [str]):
    if len(file_procc) <= n:
        return [file_procc]
    else:
        return [file_procc[:n]] + encapsule(n,file_procc[n:])
def multi_thread_analyse(my_txt : str, number_of_thread : int):
    automate_dict_sequence = {}
    words_functions = load()
    my_sentences_list = get_sentence_list(my_txt)
    space_words_dict = get_space_words()
    threading_list = encapsule(number_of_thread,my_sentences_list)







    #body of the function
    def initializeRegister(key : (str)):
        if key in automate_dict_sequence:
            automate_dict_sequence[key] = automate_dict_sequence[key] + 1
        else:
            automate_dict_sequence[key] = 1
        pass
    def get_the_path(word : str):
        if (word[0] != (word[0].lower())) or word.isdigit():
            return "nom"
        else:
            for func in words_functions.keys():
                if word in words_functions[func]:
                    return func
            return "unknow"
    def get_list_recompiler(my_list : [str]):
        new_list = []
        for path in my_list:
            if new_list == []:
                new_list.append(path)
            elif (new_list[-1] == "nom") and (path == "nom"):
                pass
            elif (new_list[-1] == "unknow") and (path == "unknow"):
                pass
            else:
                new_list.append(path)
        return new_list




    #Multithread
    class ThreadAnalyze(threading.Thread):
        def __init__(self, sentence : str):
            threading.Thread.__init__(self)
            self.sentence = sentence
        def run(self):
            words_list = get_words_list_of_a_sentence(self.sentence,space_words_dict)
            my_list = []
            for word in words_list:
                my_list.append(get_the_path(word))
            initializeRegister(tuple(get_list_recompiler(my_list)))
    i = 0
    for sequ in threading_list:
        Multi_Thread = [ThreadAnalyze(sentence) for sentence in sequ]
        for th in Multi_Thread:
            th.start()
        for th in Multi_Thread:
            th.join()
        print(i)
        i = i + 1
    return automate_dict_sequence 
#test = multi_thread_analyse(import_txt(),40)
#test = multi_thread_analyse(test_import(),40)







def Norme_2_Distance(vect_1 : (int) , vect_2 : (int)):
    assert (len(vect_1) != len(vect_2))
    return sum([(vect_1[i] - vect_2[i])**2 for i in range(len(vect_1))])**(1/2)
