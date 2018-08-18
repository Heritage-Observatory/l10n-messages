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

import argparse
import collections
import csv
import json
import os


# Name of the column identifying the ISO 639-3 code of each language.
CSV_FIELD_ISO_639_3 = 'ISO 639-3:2007'


def build_languages_localized_names(language_csv_file_path_name):
    """
    Build the localized names of the languages defined in the given CSV
    file.


    @param language_csv_file_path_name: absolute path and name of the
        Comma-Separated Values (CSV) file that contains the localized
        names of languages identified with ISO 639-3 codes.


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

    with open(language_csv_file_path_name, 'rb') as file:
        for row in csv.DictReader(file):
            languages_localized_names[row[CSV_FIELD_ISO_639_3]] = dict([(label_iso_code, label)
                    for (label_iso_code, label) in row.iteritems()
                        if label_iso_code != CSV_FIELD_ISO_639_3])

    return languages_localized_names


def main():
    """
    Read the arguments passed within the command line and convert the
    specified CSV file containing a list of languages and their localized
    names, into a JSON expression printed to the standard output.
    """
    arguments = parse_arguments()

    print json.dumps(build_languages_localized_names(os.path.expanduser(arguments.language_csv_file_path_name)))


def parse_arguments():
    """
    Convert argument strings to objects and assign them as attributes of
    the namespace.


    @return: an instance ``argparse.Namespace`` corresponding to the
        populated namespace.
    """
    parser = argparse.ArgumentParser(description='Build the localized names of languages')

    parser.add_argument('-i', '--language-csv-file', dest='language_csv_file_path_name', metavar='FILE', required=True,
            help='absolute path of the CSV file containing the localized names of languages')

    return parser.parse_args()


if __name__ == '__main__':
    main()

