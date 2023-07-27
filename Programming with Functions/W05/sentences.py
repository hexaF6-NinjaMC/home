import os
clear = lambda:os.system("cls")
clear()

import random

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if grammatical_number == 1:
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        # Randomly choose and return a verb.
        word = random.choice(words)
        return word

    if tense == "present":
        if grammatical_number == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
            # Randomly choose and return a verb.
            word = random.choice(words)
            return word

        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
            # Randomly choose and return a verb.
            word = random.choice(words)
            return word

    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        # Randomly choose and return a verb.
        word = random.choice(words)
        return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    prep_determiner = get_determiner(quantity)
    object_of_preposition = get_noun(quantity)

    prep_phrase = f"{preposition} {prep_determiner} {object_of_preposition}"
    return prep_phrase

def main():
    # SENTENCE 1
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prep_phrase = get_prepositional_phrase(1)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")

    # SENTENCE 2
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "past")
    prep_phrase = get_prepositional_phrase(2)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")

    # SENTENCE 3
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prep_phrase = get_prepositional_phrase(1)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")

    # SENTENCE 4
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "present")
    prep_phrase = get_prepositional_phrase(2)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")

    # SENTENCE 5
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prep_phrase = get_prepositional_phrase(1)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")

    # SENTENCE 6
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "future")
    prep_phrase = get_prepositional_phrase(2)
    print(f"{determiner.capitalize()} {noun} {verb} {prep_phrase}.")



main()
