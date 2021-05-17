from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Creates a list of words from a text file
    
        >>> wf = WordFinder("words.txt")
        235889 words read

        >>> wf2 = WordFinder("simple.txt")
        3 words read

        >>> wf2.random() in ["apple", "banana", "grape"]
        True

        >>> wf2.random() in ["apple", "banana", "grape"]
        True

        >>> wf2.random() in ["apple", "banana", "grape"]
        True

    """

    def __init__(self, filepath):
        """store filepath, run populate_word_and_print_num"""
        self.filepath = filepath
        self.populate_words_and_print_num()
        
    def populate_words_and_print_num(self):
        """access file, create list of words, print out num of words"""
        word_list = open(f"{self.filepath}", "r")

        self.words = word_list.readlines()

        word_list.close()

        print(f"{len(self.words)} words read")
      
    def random(self):
        """Gets random word from stored list of words and prints it"""
        return choice(self.words).strip('\n')


class SpecialWordFinder(WordFinder):
    """Word finder that works with unusual fileline arrangement
    
        >>> swf = SpecialWordFinder("words.txt")
        235886 words read

    """

    def populate_words_and_print_num(self):
        """
        Access file, create list of words, print out num of words.
        Ignores blanks and comments.
        """

        word_list = open(f"{self.filepath}", "r")

        temp_lst = word_list.readlines()

        self.words = []

        for item in temp_lst:
            if not item.startswith('\n') and not item.startswith('#'):
                self.words.append(item) 

        word_list.close()

        print(f"{len(self.words)} words read")
