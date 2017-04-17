"""
Module for the Actor class
"""

class Actor(object):
    """Actor class"""

    current_phrase = None
    current_phrase_word_list = None
    current_word = None
    current_word_index = None
    completed_words = []
    phrase_genre = None

    def __init__(self):
        self.current_phrase = None
        self.current_phrase_word_list = None
        self.current_word = None
        self.current_word_index = None
        self.completed_words = []
        self.phrase_genre = None

    def set_phrase(self, phrase, genre):
        """
        sets the current phrase and splits the words into a list
        @param phrase   :: The new phrase to use
        @param genre    :: The topic of the phrase e.g. Sport
        """
        self.current_phrase = phrase
        if len(phrase.split()) == 1:
            self.current_word_index = 0
            self.current_word = phrase
        self.phrase_genre = genre
        self.current_phrase_word_list = phrase.split()

    def set_word(self, word_index):
        """
        sets the current word to guess by index
        @param word_index   :: The index of the current word in the current_phrase_word_list
        """
        if self.current_phrase is None:
            raise RuntimeError('Can not call set_word before \
                                current_phrase has been set.')

        if word_index in self.completed_words:
            raise RuntimeError('The word at index %d is already in the list of \
                                completed words %s.' % (word_index, str(self.completed_words)))
        if word_index >= len(self.current_phrase_word_list):
            raise RuntimeError('word_index %d is more than last list \
                                index for current word %s.' % (word_index, self.current_phrase))
        else:
            self.current_word = self.current_phrase_word_list[word_index]
            self.current_word_index = word_index

    def complete_word(self):
        """
        completes the word and adds it to the list of words that no longer need to be guessed
        """
        if self.current_word is None:
            raise RuntimeError('complete_word called with no current_word selected.')
        if self.current_word_index not in self.completed_words:
            self.completed_words.append(self.current_word_index)
            self.current_word = None
            self.current_word_index = None

    def phrase_complete(self):
        """
        Called when the phrase has been guessed and is used to reset
        the state of the phrase/word
        """
        self.current_phrase = None
        self.current_phrase_word_list = None
        self.current_word = None
        self.current_word_index = None
        self.completed_words = []
        self.phrase_genre = None

    def phrase_ready(self):
        """
        checks if the phrase and word have been selected
        @return True if phrase is in a guessable state
        """
        if self.current_phrase is not None:
            if self.current_word is not None:
                if self.current_word_index is not None:
                    return True
        return False
