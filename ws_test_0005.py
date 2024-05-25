import requests
import unicodedata
from bs4 import BeautifulSoup
import os
import io
import pickle
import csv
import threading










def save(Dictionnaire : dict ,path="database.obj"):
    fileIn = open(path,"wb")
    pickle.dump(Dictionnaire,fileIn)
    fileIn.close()
def load(path="database.obj"):
    fileout = open(path,"rb")
    Load = pickle.load(fileout) 
    fileout.close()
    return Load
def MultiThreadFragmentation():
    Words_Functions = {}
    Interupt_Dict = {'conjonction de coordination' : None,'conjonction' : None,"adverbe" : None,'proverbe': None,'interjection' : None,"adjectif" : None,
                     "article" : None,"préposition" : None,'préfixe' : None,"nom" : None,"verbe" : None,"Participe" : None,"pronom" : None,"locution" : None}
    register_list = ['conjonction de coordination','conjonction',"adverbe",'proverbe','interjection',"adjectif","article","préposition",'préfixe',"nom","verbe","Participe","pronom","locution"]
    def initializeRegister(word_path : str , word : str):
        if word_path != None:
            if word_path in Words_Functions:
                Words_Functions[word_path][word] = None
            else:
                Words_Functions[word_path] = {word : None}
        else:
            initializeRegister("nom",word)
    def three_activation(word_path : str, word : str, pattern_list : [str]):
        if word_path in Interupt_Dict:
            initializeRegister(word_path,word)
        else:
            if word_path != None:
                for pattern in pattern_list:
                    if pattern in word_path:
                        initializeRegister(pattern,word)
                        return None
                initializeRegister("nom",word)
                pass
    def fundamental(word : str):
        """obtenir la fonction d'un mot"""
        url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
        soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
        if soup.select('p') != []:
            return unicodedata.normalize("NFKD", soup.select('p')[0].text)
        else:
            return None
    def encapsule(n : int , file_procc : [str]):
        """craie des ramifications d'une meme liste par paquet de n valeurs"""
        if len(file_procc) <= n:
            return [file_procc]
        else:
            return [file_procc[:n]] + encapsule(n,file_procc[n:])
    class MyThread(threading.Thread):
        def __init__(self, words : [str]):
            threading.Thread.__init__(self)
            self.words = words
        def run(self):
            for word in self.words:
                path = fundamental(word)
                three_activation(path,word,register_list)
            pass
    class MyThreadRelation(threading.Thread):
        def __init__(self, words : [str]):
            threading.Thread.__init__(self)
            self.words = words
        def run(self):
            i = 0
            for word in self.words:
                print(str(i) + "%")
                path = fundamental(word)
                i = i + 1
                three_activation(path,word,register_list)
            pass
    fileIn = open("liste_francais.txt","r")
    content = [line[:len(line) - 1].lower() for line in fileIn.readlines()]
    fileIn.close()
    partition = encapsule(100,content)
    Multi_Thread = [MyThreadRelation(partition[0])] + [MyThread(partition[j]) for j in range(1,len(partition))]
    for th in Multi_Thread:
        th.start()
    for th in Multi_Thread:
        th.join()
    save(Words_Functions)




"""
class MyProcess(threading.Thread):
    def __init__(self , words : [str]):
        threading.Thread.__init__(self)
    def run(self):
        pass


pass
def proc1():
    pass
def proc2():
    pass
th1 = threading.Thread(target=proc1)
th2 = threading.Thread(target=proc2)
th1.start()
th2.start()



th1.join()
th2.join()
"""
