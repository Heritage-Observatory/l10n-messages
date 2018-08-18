#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Heritage Observatory.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY,# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import collections
import csv
import json
import os
import sys


# Name of the column identifying the ISO 639-3 code of each language.
CSV_FIELD_ISO_639_3 = 'ISO 639-3:2007'


def build_languages_localized_names():
    """
    Build the localized names of the languages defined in the given CSV
    content read from the standard input.


    @return: a dictionary for each language identified with a ISO 639-3
        code (the key) and which values corresponds to a dictionary of the
        names of this languages given in several locales, each identified
        wia ISO 639-3 code::

            {
              "<<language-iso-639-3-code>>": {
                "<<locale-iso-639-3-code>>": "<<language-localized-name>>",
                (...)
              },
              (...)
            }
    """
    languages_localized_names = collections.defaultdict(dict)

    for row in csv.DictReader(sys.stdin):
        languages_localized_names[row[CSV_FIELD_ISO_639_3]] = dict([(label_iso_code, label)
                for (label_iso_code, label) in row.iteritems()
                    if label_iso_code != CSV_FIELD_ISO_639_3])

    return languages_localized_names


def main():
    """
    Convert the content CSV file--read from the standard input--containing
    a list of languages and their localized names, into a JSON expression
    printed to the standard output.
    """
    print json.dumps(build_languages_localized_names())


if __name__ == '__main__':
    main()

