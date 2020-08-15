#!/usr/bin/env python3

# Copyright 2020 Sean Kelleher. All rights reserved.
# Use of this source code is governed by a MIT
# licence that can be found in the LICENCE file.

# `$0 <src-file> <tgt-file>` outputs each line in `tgt-file` and the line in
# `src-file` that most closely matches it.

import sys


def main():
    if len(sys.argv) != 3:
        print("usage: {0} <src-file> <tgt-file>".format(sys.argv[0]))
        sys.exit(1)

    src_file, tgt_file = sys.argv[1:]

    trie = {}
    with open(src_file) as f:
        trie = new_dict_trie([ln.rstrip() for ln in f])

    with open(tgt_file) as f:
        for ln in f:
            tgt_line = ln.rstrip()
            closest = closest_match(tgt_line, trie)
            print('{0}: {1}'.format(tgt_line, closest))


def new_dict_trie(lines):
    """
    `new_dict_trie` returns a new trie, encoded as a dictionary, containing
    `lines`.
    """
    trie = {}
    for line in lines:
        node = trie
        for char in line:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[-1] = True
    return trie


def closest_match(tgt, trie):
    """
    `closest_match` returns the line from `trie` that has the shortest
    Levenshtein distance to `tgt`.
    """
    return sub_closest_match(tgt, trie, range(len(tgt)+1), 1)[0]


def sub_closest_match(tgt, trie, prev_row, row_num):
    """
    `sub_closest_match` returns the line from `trie` that has the shortest
    Levenshtein distance to `tgt`, assuming that `num_rows` of the distance
    have already been computed and `prev_row` is the most recent row to have
    been computed.
    """
    closest = None

    for (char, sub_trie) in trie.items():
        dist = ('', prev_row[-1])
        if char != -1:
            this_row = [row_num]
            for j in range(1, len(prev_row)):
                this_row.append(min(
                    this_row[-1]+1,
                    prev_row[j]+1,
                    prev_row[j-1] + (tgt[:1] != char),
                ))

            (s, d) = sub_closest_match(tgt[1:], sub_trie, this_row, row_num+1)
            dist = (char + s, d)

        if closest is None or dist[1] < closest[1]:
            closest = dist

    return closest


if __name__ == '__main__':
    main()
