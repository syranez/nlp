# 02 - Edit distance

## Definition of minimum edit distance

Edit distance
        Is the minimum number of editing (Insertion, Deletion, Substitution) operations needed to transform one into the other.

Cost of each operation: 1

Levenshtein:
        Substitutions cost 2

Minimum Edit Distance

        Is String X of length n
        Is String Y of length m
        Then the minimum edit distance is D(n, m)

## Computing minimum edit distance

Solve problem by combining solutions to subproblems.

Bottom-up:
    * compute D(i, j) from small i,j
    * and compute larger D(i, j) based on previously computed smaller values

1. Initialization

    D(i, 0) = i
    D(0, j) = j
2. Recurrence Relation:

    For each i = 1...m
        For each j = 1...n
                          | D(i-1, j) + 1
            D(i, j) = min | D(i, j-1) + 1
                          | D(i-1, j-1) + 2 | if x(i) != y(i)
                                          0 | otherwise
3. Termination:

    D(n, m) is distance

## Backtrace for Computing Alignments

    * edit distance is not sufficient
    ** we often need to *align* each character of the two strings to each other
    * keeping a backtrace
    * every time we enter a cell, remember where we came from
    * when we reach the end,
    ** trace back the path from the upper right corner to read off the alignment

    For each i = 1...m
        For each j = 1...n
                          | D(i-1, j) + 1 **deletion**
            D(i, j) = min | D(i, j-1) + 1 **insertion**
                          | D(i-1, j-1) + 2 | if x(i) != y(i) **ksubstitution**
                                          0 | otherwise

                          | LEFT **insertion**
            ptr(i, j)  =  | DOWN **deletion**
                          | DIAG **substitution**

1. Performance

    * Time:      O(nm) (string x of length n * string y of length m)
    * Space:     O(nm) (table)
    * Backtrace: O(n+m)
