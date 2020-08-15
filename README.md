Cascading Levenshtein Distance
==============================

About
-----

This project is a proof-of-concept optimisation of the Levenshtein distance
algorithm for finding a closest-match for a string from a set of candidates. It
was originally designed as a solution to a problem in the 2016 APL Problem
Solving Competition, namely General Computing Problem 3, Task 1, "Match Maker"
(<https://www.dyalog.com/uploads/files/student_competition/2016_problems_phase2.pdf>).

Approach
--------

The cascading Levenshtein distance operates on a prefix tree and reuses tables
generated on prefixes in sub-computations. For example, if computing the
distance between the word "rank" and the set "baby", "bad" and "bank", then the
distance between "rank" and "ba" would be computed once and reused for each
member of the target set.

Results
-------

Informal runs of the `casc_ld.py` solution against the dataset provided with the
original competition have shown up to a 45% reduction in completion time
compared with runs using the `plain_ld.py` solution. Here is a sample output from
a run of `time` on `casc_ld.py`:

    real 15m01.671s
    user 14m51.712s

Compare this with a sample run of `time` on `plain_ld.py` on the same inputs and
in the same environment:

    real 27m55.775s
    user 27m39.172s

Runs with completely random data as generated with `gen_test_data.py 500` have
shown reductions more in the range of 10%. Here is a sample output from
a run of `time` on `casc_ld.py`:

    real 0m24.972s
    user 0m23.948s

Compare this with a sample run of `time` on `plain_ld.py` on the same inputs and
in the same environment:

    real 0m28.545s
    user 0m28.028s

This result may be partly related to the totally random nature of the source
data set, which then doesn't lend itself as readily to optimisation using prefix
trees.

In all, the results from being able to reuse pre-calculated results from
prefixes would likely be surpassed by the results of simply parallelising the
plain approach, unless the source dataset was particularly "prefix-heavy".

Usage
-----

`python3 gen_test_data.py 1000` can be used to generate a test source and target
data file with 1000 lines of random data each. The algorithm implementations can
then be run against these using `python3 casc_ld.py target/actual.txt
target/dirty.txt`.
