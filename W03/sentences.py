import random

def main():
    # Generate five sentences and print them.
    for i in range(5):
        print(make_sentence())

def make_sentence():
    """Generate and return a simple English sentence."""
    determiner = get_determiner(random.randint(1, 2))
    noun = get_noun(random.randint(1, 2))
    verb = get_verb()
    sentence = f"{determiner} {noun} {verb}."
    return sentence

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter:
        quantity (int): an integer. If quantity is 1, this
            function will return a determiner for a single
            noun. Otherwise, this function will return a
            determiner for a plural noun.
    Return:
        str: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will return one of these
    ten single nouns:
        "bird", "boy", "car", "cat", "child", "dog", "girl",
        "man", "rabbit", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "birds", "boys", "cars", "cats", "children", "dogs",
        "girls", "men", "rabbits", "women"

    Parameter:
        quantity (int): an integer. If quantity is 1, this
            function will return a single noun. Otherwise,
            this function will return a plural noun.
    Return:
        str: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word

def get_verb():
    """Return a randomly chosen verb. A verb is a word that
    expresses an action or state of being.

    Return:
        str: a randomly chosen verb.
    """
    words = ["laughs", "eats", "thinks", "thought", "runs", "writes"]
    word = random.choice(words)
    return word

if __name__ == "__main__":
    main()
