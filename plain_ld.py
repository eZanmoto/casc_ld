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

    with open(src_file) as f:
        src_lines = [ln.rstrip() for ln in f]

    with open(tgt_file) as f:
        for ln in f:
            tgt_line = ln.rstrip()
            closest = closest_match(tgt_line, src_lines)
            print('{0}: {1}'.format(tgt_line, closest))


def closest_match(tgt, lines):
    """
    `closest_match` returns the first line from `lines` that has the shortest
    Levenshtein distance to `tgt`.
    """
    closest = None
    for src in lines:
        dist = ld(tgt, src)
        if closest is None or dist < closest[1]:
            closest = (src, dist)
    return closest[0]


def ld(w1, w2):
    """
    `ld` returns the Levenshtein distance between `w1` and `w2`.
    """
    this_row = range(len(w1)+1)
    for row_num in range(1, len(w2)+1):
        prev_row = this_row
        this_row = [row_num]
        for j in range(1, len(prev_row)):
            this_row.append(min(
                this_row[-1]+1,
                prev_row[j]+1,
                prev_row[j-1] + (w1[row_num-1:row_num] != w2[j-1:j]),
            ))
    return this_row[-1]


if __name__ == '__main__':
    main()
