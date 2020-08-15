#!/usr/bin/env python3

# Copyright 2020 Sean Kelleher. All rights reserved.
# Use of this source code is governed by a MIT
# licence that can be found in the LICENCE file.

# `$0 <num-lines>` generates test data files containing `num-lines` random lines
# to `target` for use with `naiveld.py` and `distld.py`.

import os
import random
import string
import sys


def main():
    if len(sys.argv) != 2:
        print("usage: {0} <num_lines>".format(sys.argv[0]))
        sys.exit(1)

    num_lines = int(sys.argv[1])

    tgt_dir = 'target'
    os.makedirs(tgt_dir, exist_ok=True)
    for fname in ['actual', 'dirty']:
        with open(tgt_dir + '/' + fname + '.txt', 'w') as f:
            for _ in range(num_lines):
                cs = [random.choice(string.ascii_uppercase) for _ in range(10)]
                f.write(''.join(cs) + '\n')


if __name__ == '__main__':
    main()
