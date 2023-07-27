import os
clear = lambda:os.system("cls")
clear()

from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    # This loop will repeat the statements inside it 10 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):
        word = get_noun(1)

        # Verify that the word returned from get_noun is
        # one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # 1. Test the past verbs.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 10 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs list.
        assert word in past_verbs

    # 2-a. Test the present tense single verbs.

    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_single_verbs list.
        assert word in present_single_verbs
        
    # 2-b. Test the present tense plural verbs.

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_plural_verbs list.
        assert word in present_plural_verbs

    # 3. Test the future verbs.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 10 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs list.
        assert word in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    for _ in range(30):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    singlar_gram_number_prep_phrase = get_prepositional_phrase(1)
    plural_gram_number_prep_phrase = get_prepositional_phrase(2)

    prep_phrase_parts = singlar_gram_number_prep_phrase.split(" ")
    assert prep_phrase_parts.__len__() == 3

    prep_phrase_parts = plural_gram_number_prep_phrase.split(" ")
    assert prep_phrase_parts.__len__() == 3



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
