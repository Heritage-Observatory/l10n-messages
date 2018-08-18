# l10n-messages
Command line utility to generate a JSON expression of the localized names of languages in the World.

## Foreword

The [Heritage Observatory](https://www.heobs.org) non-profit organization maintains a list of the localized names of languages existing in the World.

![Sample of the Common Languages List](language-list-sample-20180818.png)

You can download the content of this list from the online sheet [Language ISO Codes](https://docs.google.com/spreadsheets/d/1BnrNVSsFbgSuP_ERyAPEZ-LFpvKYfGlREsInTjJVvr4/edit#gid=263773231). This material is licensed under the terms of the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

## Language Lists

The [Heritage Observatory](https://www.heobs.org) maintains two lists:

* a [complete list of the languages](https://docs.google.com/spreadsheets/d/1BnrNVSsFbgSuP_ERyAPEZ-LFpvKYfGlREsInTjJVvr4/edit#gid=263773231) in the World (8182);

* a [sub-list of the most common languages](https://docs.google.com/spreadsheets/d/1BnrNVSsFbgSuP_ERyAPEZ-LFpvKYfGlREsInTjJVvr4/edit#gid=893823414) in the World (186).

Each list contains the following columns:

* **ISO Language Name**: commonly used English name of the language;

* **Native Name (endonym)**: name used by the linguistic community to refer their language;

* **Language Family**: group of languages this language is related to;

* **Language Type**: individual languages are identified as being of one of the following [five types](https://iso639-3.sil.org/about/types):

  * `A` (`ancient`): a language is listed as *ancient* if it went extinct in ancient times (e.g. more than a millennium ago). Identifiers are assigned to ancient languages which have a distinct literature and are treated distinctly by the scholarly community. It would be ideal to be able to assign identifiers to ancient languages on the basis of intelligibility, but ancient records rarely contain enough information to make this possible. In order to qualify for inclusion, the language must have an attested literature or be well-documented as a language known to have been spoken by some particular community at some point in history; it may not be a reconstructed language inferred from historical-comparative analysis.

  * `C` (`constructed`): This part of also includes identifiers that denote *constructed* (or artificial) languages. In order to qualify for inclusion the language must have a literature and it must be designed for the purpose of human communication. It must be a complete language, and be in use for human communication by some community long enough to be passed to a second generation of users. Specifically excluded are reconstructed languages and computer programming languages.

  * `E` (`extinct`): a language is listed as *extinct* if it has gone extinct in recent times. (e.g. in the last few centuries). The criteria for identifying distinct languages in these case are based on intelligibility (as defined for individual languages).

  * `H` (`historical`): a language is listed as *historic* when it is considered to be distinct from any modern languages that are descended from it; for instance, Old English and Middle English. Here, too, the criterion is that the language have a literature that is treated distinctly by the scholarly community.;

  * `L` (`living`): a language is listed as *living* when there are people still living who learned it as a first language.

* **Denotation Scope**: [range of language varieties](https://iso639-3.sil.org/about/scope), either individual language or macrolanguage, either collection of languages.

  * `I` (`individual`): distinct *individual* languages, i.e., every distinct human language that has been documented, whether living, extinct, or constructed, and whether its modality is spoken, written or signed;
  
  * `M` (`macrolanguage`): One-to-many grouping of languages also known as *macrolanguages*. They are distinguished from language collections in that the individual languages that correspond to a macrolanguage must be very closely related, and there must be some domain in which only a single language identity is recognized;
  
  * `S` (`special`): other *special* situations.

* **ISO 639-1:2002**: *codes for the representation of names of languages — Part 1: Alpha-2 code*;

* **ISO 639-2:1998/T**: *codes for the representation of names of languages — Part 2: Alpha-3 code*, *bibliographic* codes, which are derived from the native name for the language and resembles the language's two-letter code in ISO 639-1;

* **ISO 639-2:1998/B**: *codes for the representation of names of languages — Part 2: Alpha-3 code*, *terminological* codes, which are derived from the English name for the language and was a necessary legacy feature;

* **ISO 639-3:2007**: *codes for the representation of names of languages – Part 3: Alpha-3 code* for comprehensive coverage of languages.

* Localized names: several columns that provide the name of a language for a various locales (ISO 639-2:1998/T).

## Usage

### Generate a JSON expression on `stdout`

You can easily generate a JSON expression of the language data contain in this sheet by running the following line command:

``` shell
wget -O - "https://docs.google.com/feeds/download/spreadsheets/Export?key=1BnrNVSsFbgSuP_ERyAPEZ-LFpvKYfGlREsInTjJVvr4&exportFormat=csv" \
    | ./make_languages.py \
    | json_pp
```

which, for instance, produces the following result:

```
{
   "aji" : {
      "rus" : "аджиэ",
      "Notes" : "",
      "ISO Language Name" : "Ajië",
      "Native Name (endonym)" : "",
      "spa" : "",
      "Language Type" : "L",
      "fra" : "",
      "ISO 639-2:1998/T" : "",
      "deu" : "",
      "Language Family" : "Austronesian",
      "ISO 639-1:2002" : "",
      "zho" : "",
      "Denotation Scope" : "I",
      "ISO 639-2:1998/B" : "",
      "eng" : "Ajië"
   },
   "yet" : {
      "ISO 639-2:1998/B" : "",
      "eng" : "Yetfa",
      "zho" : "",
      "ISO 639-1:2002" : "",
      "Denotation Scope" : "I",
      "Language Family" : "",
      "deu" : "",
      "ISO 639-2:1998/T" : "",
      "Language Type" : "L",
      "fra" : "",
      "spa" : "",
      "ISO Language Name" : "Yetfa",
      "Native Name (endonym)" : "",
      "rus" : "",
      "Notes" : ""
   },
   (...)
   ```

### Integrate Data into your Application

You will probably need to save the JSON expression into a file, say `languages.json`.  Simply run the following command line:

``` shell
wget -O - "https://docs.google.com/feeds/download/spreadsheets/Export?key=1BnrNVSsFbgSuP_ERyAPEZ-LFpvKYfGlREsInTjJVvr4&exportFormat=csv" \
    | ./make_languages.py > languages.json
```

The following example used the programming language [`Python`](https://www.python.org/). We are using the Python library [`Perseus Common`](https://github.com/dcaune/perseus-lib-python-common) to handle locales:

``` shell
pip install majormode-perseus-common
```

We create a function that returns the name of the languages in the world written in the specified locale:

``` python
import json
import os
import sys

from majormode.perseus.model.locale import DEFAULT_LOCALE


# Default name of the file containing the list of languages and their
# localised names.
DEFAULT_LANGUAGE_NAMES_FILE_NAME = 'languages.json'


def get_localized_language_names(language_locales,
        language_names_file_path_name=None,
        locale=None):
    """
    Return the name of the languages in the world written in the specified
    locale.

    The function relies on a JSON file containing the localised names of
    languages in the world written in various locales.  This JSON file is
    generated by the script ``make_message.py`` that parses the CSV file
    of the Google Sheet "Language ISO Codes" that the Heritage Observatory
    association provides for free.
    

    @param language_locales: a list of instances ``Locale`` representing
        the language to the return the names in the specified locale.

    @param language_names_file_path_name: the absolute path and name of
        the JSON file containing the localised names of the languages in
        the world.  If not defined, the function uses the default file
        provided in this library.

    @param locale: an instance ``Locale`` to return the localised names
        of the specified languages in.


    @return: a dictionary of the localised names of the specified
        languages where a key corresponds to a locale referencing a
        language and the value corresponds to the localised name of this
        language::

            {
              locale:string: language_name:string,
              ...
            }
    """
    if language_names_file_path_name:
        assert os.path.exists(language_names_file_path_name), \
            'The languages names file "%s" does not exist' % language_names_file_path_name
    else:
        language_names_file_path_name = os.path.join(DEFAULT_LANGUAGE_NAMES_FILE_NAME)

    # Load all the languages names in a dictionary.
    with open(language_names_file_path_name) as file:
        languages_names = json.loads(file.read())

    # Retrieve the names of these languages written in the specified
    # locale.
    locale_string = (locale or DEFAULT_LOCALE).to_string()

    return dict([(language_locale,
                  languages_names[language_locale.to_string()].get(locale_string) or language_locale.to_string())
            for language_locale in language_locales])
```

We can use this function as follows:

``` python
>>> from majormode.perseus.model.locale import Locale
>>> print get_localized_language_names([Locale('eng'), Locale('fra'), Locale('vie')])
{eng: u'English', fra: u'French', vie: u'Vietnamese'}
>>> print get_localized_language_names([Locale('eng'), Locale('fra'), Locale('vie')], locale=Locale('fra'))
{eng: u'anglais', fra: u'fran\xe7ais', vie: u'vietnamien'}

```
