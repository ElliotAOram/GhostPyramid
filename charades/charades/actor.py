"""
Module for the Actor class
"""

class Actor(object):

    current_phrase = None
    current_phrase_word_list = None
    current_word = None
    current_word_index = None
    completed_words = []

    def set_phrase(self, phrase):
        self.current_phrase = phrase
        self.current_phrase_word_list = phrase.split()

    def set_word(self, word_index):
        if self.current_phrase is None:
            raise RuntimeError('Can not call set_word before \
                                current_phrase has been set.')
        if word_index >= len(self.current_phrase_word_list):
            raise RuntimeError('word_index %d is more than last list \
                                index for current word %s.' % (word_index, self.current_phrase))
        else:
            self.current_word = self.current_phrase_word_list[word_index]
            self.current_word_index = word_index

    def complete_word(self):
        if self.current_word is None:
            raise RuntimeError('complete_word called with no current_word selected.')
        if self.current_word_index not in self.completed_words:
            self.completed_words.append(self.current_word_index)
