from re import S
from .base import BaseExtractor
from hazm import *

class BaseHazmExtractor(BaseExtractor):
    
    def __init__(self,*args, **kwargs):
        super(BaseExtractor, self).__init__(*args, **kwargs)
        
    def _normalize(self, text):
        if not hasattr(self, 'normalizer'):
            self.normalizer = Normalizer()
        return self.normalizer.normalize(text)

    def _tagger(self, sentence):
        if not hasattr(self, 'tagger'):
            self.tagger = POSTagger(model='resources/postagger.model')
        return self.tagger.tag(word_tokenize(sentence))

    def _sentences(self, text):
        return sent_tokenize(text)

    def stopwords(self):
        return stopwords_list()
