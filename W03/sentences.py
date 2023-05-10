import random

def main():
    # Generate and print six sentences
    sentences = [
        make_sentence(1, 'past'),
        make_sentence(1, 'present'),
        make_sentence(1, 'future'),
        make_sentence(2, 'past'),
        make_sentence(2, 'present'),
        make_sentence(2, 'future')
    ]
    for sentence in sentences:
        print(sentence)

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.

    Parameters:
        quantity (int): an integer that determines the grammatical
            number of the determiner and noun in the sentence.
        tense (str): a string that determines the grammatical tense
            of the verb in the sentence, either "past", "present"
            or "future".

    Returns:
        str: a sentence with three words, a determiner, a noun, and
            a verb, that follows the grammar rules specified by the
            quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
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

def get_verb(quantity, tense):
    """Return a randomly chosen verb. A verb is a word that
    expresses an action or state of being.

    Parameters
        quantity (int): an integer that determines if the
            returned verb is single or plural.
        tense (str): a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return:
        str: a randomly chosen verb.
    """
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    else:
        words = []
    word = random.choice(words)
    return word


if __name__ == "__main__":
    main()
