import re, string
from PyDictionary import PyDictionary

words = []
illegal_words = ["it", "a", "is"]
context_words = ["so", "what", "you"]

#check to see if the word is plural
def is_plural(word):
    return False

def process_word(wd):
    wd.lower()
    wd = re.sub(r'[^\w\s]','',wd)
    return wd


def make_word_objs(wordsIn, types):
    for w in wordsIn:
        w = process_word(w)
        print(w)


def main():
    eng_sent = input("Enter your sentence: ")
    words_raw = eng_sent.split()
    types_in = input("Enter the types of words: ")
    types = types_in.split()
    make_word_objs(words_raw, types)

if __name__ == "__main__":
    main()

