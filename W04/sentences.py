import random

# Lists of possible determiners and nouns for singular and plural quantity
determiners_single = ["a", "the", "this", "that", "one"]
determiners_plural = ["some", "many", "these", "those"]
nouns_single = ["boy", "girl", "dog", "cat", "bird"]
nouns_plural = ["boys", "girls", "dogs", "cats", "birds"]

# Lists of possible verbs for different tenses
verbs_past = ["walked", "ran", "jumped", "talked", "laughed"]
verbs_present = ["walks", "runs", "jumps", "talks", "laughs"]
verbs_future = ["will walk", "will run", "will jump", "will talk", "will laugh"]

# List of possible prepositions
prepositions = ["about", "above", "across", "after", "along", "around",
                "at", "before", "behind", "below", "beyond", "by",
                "despite", "except", "for", "from", "in", "into", "near",
                "of", "off", "on", "onto", "out", "over", "past", "to",
                "under", "with", "without"]

# Returns a random determiner based on singular or plural quantity
def get_determiner(quantity):
    if quantity == "single":
        return random.choice(determiners_single)
    elif quantity == "plural":
        return random.choice(determiners_plural)

# Returns a random noun based on singular or plural quantity
def get_noun(quantity):
    if quantity == "single":
        return random.choice(nouns_single)
    elif quantity == "plural":
        return random.choice(nouns_plural)

# Returns a random verb based on tense
def get_verb(tense):
    if tense == "past":
        return random.choice(verbs_past)
    elif tense == "present":
        return random.choice(verbs_present)
    elif tense == "future":
        return random.choice(verbs_future)

# Returns a random preposition
def get_preposition():
    return random.choice(prepositions)

# Returns a prepositional phrase in the form of "preposition determiner noun"
def get_prepositional_phrase(quantity):
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

# List of possible adjectives
adjectives = ["happy", "sad", "big", "small", "bright"]

# Returns a random adjective
def get_adjective():
    return random.choice(adjectives)

# Generates a sentence based on quantity and tense
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    # Constructs the sentence using the generated parts
    return f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."
# Generates and prints six sentences using different quantities and tenses
def main():
    sentences = []
    sentences.append(make_sentence("single", "past"))
    sentences.append(make_sentence("single", "present"))
    sentences.append(make_sentence("single", "future"))
    sentences.append(make_sentence("plural", "past"))
    sentences.append(make_sentence("plural", "present"))
    sentences.append(make_sentence("plural", "future"))
    for sentence in sentences:
        print(sentence)

main()