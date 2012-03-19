# 01 - Basic text processing

## Regular expressions

1. Disjunctions

    * [wW]oodchuck matches (=>) woodchuck and Woodchick.
    * [1234567890] is equal to [0-9] => any digit.

2. Negation in Disjunctions

    * [^Ss] => all but S and s.
    * ^ has only special meaning when first in [].

3. More Disjunction

    * groundhog|woodchuck
    * a|b|c is equal to [abc]
    * [gG]roundhog|[Ww]oodchuck => groundhog, Groundhog, woodchuck and Woodchuck.

4. Special characters

    * optional previous char: ?
    ** colou?r => color and colour
    * 0 or more of previous char: * (Kleene)
    ** oo*h! => ooh! => oooh! => oooooooooh!
    * 1 or more of previous char: + (Kleene)
    ** o+h! => oh! => ooh! => oooooooh!
    * matches any character: .
    ** beg.n => begin => began => beg3n

5. Anchors

    * match begin of line: ^
    * match end of line:   $

6. Errors

    * matching strings that we should not have matched: *false positives (Type
    I)*
    * not matching things that we should have matched: *false negatives (Type
    II)*

    In NLP we are always dealing with these kindes of errors.

    Reducing the error rate for an application often involves two antagonistic
    efforts:

    * increasing accuracy or precision (minimizing false positives)
    * increasing coverage or recall (minimizing false negatives)

7. Summary

    * regular expressions play a surprisingly large role
    * for many hard tasks, we use machine learning classifiers
    ** but regular expressions are used as features in the classifiers
    ** can be very useful in capturing generalizations

## Word tokenization

1. Every NLP task needs to do text normalization:

    1. Segmenting / tokenizing words in running text
    2. Normalizing word formats
    3. Segmenting sentences in running text

2. Definitions

Lemma
        same stem, part of speech, rough word sense: cat and cats = same lemma

Wordform
        the full inflected surface form: cat and cats = different wordforms

Type
        an element of the vocabulary

Token
        an instance of that type in running text

N = Number of tokens
V = vocabulary = set of types
|V| is the size of the vocabulary

3. Issues

    * Finland's capital    => Finland Finlands Finland's
    * what're, I'm, isn't  => What are, I am, is not
    * Hewlett-Packard      => Hewlett Packard?
    * state-of-the-art     => state of the art? (one word becomes four,
    destroying the meaning)
    * Uppercase, Lowercase => make all words either lowercase or upperacse
    * San Francisco        => One token or two?
    * m.p.h., PhD.         => ?

4. Word segmentation:

    Donaudampfschifffahrtsgesellschaft => donau dampf schifffahrt gesellschaft

## Word normalization and stemming

    input USA (U.S.A) should both find: U.S.A and USA 

1. Lemmatization

    Reduce inflections or variant forms to base form: am,
        are, is                 => be
        car, cars, car's, cars' => car

2. Stemming

    * reduce terms to their stems in information retrieval
    * stemming is crude chopping of affixes
    ** language dependent
    ** e. g., automate(s), automatic, automation all reduced to automat.

3. Porter's algorithm

    The most common English stemmer.

## Sentence Segmentation and Decision Trees

    * !, ? are relatively unambiguous
    * period . is quite ambiguous
    ** sentence boundary
    ** abbreviations
    ** numbers lik .02 %
    * build a binary classifier
    ** Looks at a .
    ** decides EndOfSentence / NotEndOfSentence
    ** Classifiers: hand-written rules, regular expressions, or
    machine-learning


