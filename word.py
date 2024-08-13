def print_upper_words(words):
    """Print words uppercase on seperate lines
        
        print_upper_words(["mardo", "jake"])
        MARDO
        JAKE
    """
    for word in words:
        print(word.upper())

def print_upper_word2(words):
    """Print word on seperate line, uppercase and if they start with E or e.
        
        print_upper_word2(["earth", "Marco", "Ernie", "marty"])
        EARTH
        ERNIE
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words(words, must_start_with):
    """Print words uppercase, start with first letters uppercase.
        
        print_upper_words(["Batman", "Superman", "wildcat"], must_start_with=["B", "S"])
        BATMAN
        SUPERMAN
    """
    for word in words:
        for letters in must_start_with:
            if word.startswith(letters):
                print(word.upper())       