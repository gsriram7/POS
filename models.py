from utils import split_word_from_tag


class Sentence(str):
    def __init__(self, raw):
        self.raw = raw
        self.words = []
        for token in raw.split(" "):
            (word, tag) = split_word_from_tag(token)
            self.words.append(Word(word, tag))


class Word(object):
    def __init__(self, word, tag):
        self.word = word
        self.tag = tag
