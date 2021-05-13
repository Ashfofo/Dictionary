from PyDictionary import PyDictionary

class Dictionary(object):
    def  __init__(self):
        #dictionary = PyDictionary()
        pass


    @staticmethod
    def get_synonyms(word):
        dictionary = PyDictionary
        return dictionary.synonym(word)


    @staticmethod
    def get_meaning(word):
        dictionary = PyDictionary
        return dictionary.meaning(word)


    @staticmethod
    def get_noun(word):
        '''
        gets a word and return a list of meanings corresponding to a noun
        '''
        try :
            noun = Dictionary.get_meaning(word)['Noun']
            return noun
        except (Exception) :
            return False


    @staticmethod
    def get_verb(word):
        '''
        gets a word and return a list of meanings corresponding to a verb
        '''
        try:
            verb = Dictionary.get_meaning(word)['Verb']
            return verb
        except (Exception):
            return False










