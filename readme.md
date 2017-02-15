# ACMI Collection Data - starter kit for Data Vis

This is a small kit of data extracted from the ACMI Collection data release at:
https://github.com/ACMILabs/collection/

While the main collection repo contains a single TSV file of the whole collection data release, and individual JSON files for each object, it might not be immediately clear how to extract useful aggregate information from that data.

This repo provides some simple aggregate data on the ACMI Collection along with a Python script that was used to generate that data, as an example of one of many approaches to working with the collection data.

## What's in this repo?

* `/acmi_generate_stats.py` - a Python (2.7) script for generating a set of JSON and TSV stats files
* `/src/collections_data.tsv` - a copy of the source TSV file of the collection, from https://github.com/ACMILabs/collection/
* `/dist/json/` - a set of JSON files - `collections_data_complete.json` contains all objects, and generated indexes and stats, and could be uploaded to [Firebase](https://firebase.google.com/) or other NoSQL data stores that play well with large JSON files.
* `/dist/tsv/` - a set of TSV files of simple aggregate counts by category, showing the number of records by sub-category

## Where to begin?

We actively encourage messing with, manipulating, joining, and querying the collection dataset in all sorts of creative ways. The example here is just to look at the total number of records in the dataset, calculated based on category or sub-category.

In `/dist/tsv/` there is a set of TSV files for the main categories of each object record. Each table lists a column of sub-categories, and a column for the number of records matching that sub-category.

The TSV files in this repo can be opened directly in Excel or uploaded to tools like [Datawrapper](https://www.datawrapper.de/) to create charts without dealing with code or a spreadsheet directly.

## Using the provided Python script

The script to generate the target JSON and TSV stats is included in the repo. The provided source TSV file for the ACMI collection data includes fields where multiple values are entered into a single column. These multiple values are separated by a pipe or vertical bar character `|`.

The included Python script `acmi_generate_stats.py` splits these strings into separate values before performing a count.

1. Download the repo to a local environment running Python 2.7
2. From a terminal, run `python acmi_generate_stats.py` in the repo directory
3. The script will parse the collections data at `src/collections_data.tsv` and write all JSON and TSV files to `dist/`

If you just want to play with the generated data in this repo, there is no need to run the Python script. But this script could be a good starting point for developing deeper work.

Alternately, if you are working with this data in Google Sheets, follow the instructions on [separating cell text into columns](https://support.google.com/docs/answer/6325535?hl=en).

## Further reading on data visualisation for cultural data:

* [Florian Krautli's PhD thesis on visualising cultural data](http://www.kraeutli.com/index.php/2016/04/15/visualising-cultural-data/)
* [Tim Sherratt's digital tools for digital historians](https://timsherratt.org/digital-heritage-handbook/courses/digital-tools-and-techniques-for-the-adventurous-historian/)
* [Davenport's 'shape of the Tate'](http://www.ifweassume.com/2013/11/the-dimensions-of-art.html)
* [Mitchell Whitelaw's Representing Digital Collections](http://mtchl.net/representing-digital-collections/)
* [George Oates on building a 'spelunker' for MOMA](https://goodformandspectacle.wordpress.com/2017/01/26/new-work-moma-exhibition-spelunker/)
* [George Oates on a four week sprint making an earlier spelunker for the Wellcome Collection](https://whatsinthelibrary.wordpress.com)

## Further links on data visualisation tools:
* [The Next Web top 14 data vis tools](https://thenextweb.com/dd/2015/04/21/the-14-best-data-visualization-tools/)
* [D3.js - Javascript library for visualising data](https://d3js.org/)

## Further links on coding topics:
* Learn Python - [Code School](https://www.codeschool.com/courses/try-python), [Codecademy](https://www.codecademy.com/learn/python)
* Learn JavaScript - [Codecademy](https://www.codecademy.com/learn/javascript)
* Learn jQuery - [Code School](https://www.codeschool.com/courses/try-jquery)

## Instructions on opening TSV files

TSV files use tab-separated values, similar to a comma separated values file (CSV), and can be opened in most spreadsheet software.

### Opening TSV files in Google Sheets

1. Create a new Google Sheet at sheets.google.com
2. Go to File > Import
3. Select the .TSV file to upload
4. In the File Import window, under Separator Character select Tab
5. Click Import

### Opening TSV files in Excel

The TSV provided is in the following structure:

- Tab delimited
- Multi value columns use a pipe (or vertical bar) character to separate string values.
- The file is encoded in UTF-8
- The file does _not_ include a BOM (byte order mask) so that it is slightly easier to use with some scripting languages.
- This means when you open the TSV, you will likely need to set the encoding format to UTF-8.

If you are using Excel 2010, try the following steps to open the TSV file:

1. Go to _File > Open_, and browse for _All Files (*.*)_
2. Select the _.tsv_ file, this will open up the Text Import Wizard.
3. Set _Original data type_ to __Delimited__
4. Set _File origin_ to __650001 : Unicode (UTF-8)__ (on Mac, this might just say Unicode UTF-8)
5. Click Next
6. Set the Delimiter to Tab, leave the others unchecked
7. Set the Text qualifier to double quotes __"__
8. Leave _Column data format_ as __General__

If titles appear with strange characters displaying, double check that you have imported the file as __Unicode (UTF-8)__

Further information on the structure of the ACMI collection data can be found at: https://github.com/ACMILabs/collection/

***

## Creative Commons License

# CC0 1.0 Universal

```
CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER.
```

### Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights (defined below) upon the creator and subsequent owner(s) (each and all, an "owner") of an original work of authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for the purpose of contributing to a commons of creative, cultural and scientific works ("Commons") that the public can reliably and without fear of later claims of infringement build upon, modify, incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes. These owners may contribute to the Commons to promote the ideal of a free culture and the further production of creative, cultural and scientific works, or to gain reputation or greater distribution for their Work in part through the use and efforts of others.

For these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.

1. __Copyright and Related Rights.__ A Work made available under CC0 may be protected by copyright and related or neighboring rights ("Copyright and Related Rights"). Copyright and Related Rights include, but are not limited to, the following:

    i. the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work;

    ii. moral rights retained by the original author(s) and/or performer(s);

    iii. publicity and privacy rights pertaining to a person's image or likeness depicted in a Work;

    iv. rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below;

    v. rights protecting the extraction, dissemination, use and reuse of data in a Work;

    vi. database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and

    vii. other similar, equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.

2. __Waiver.__ To the greatest extent permitted by, but not in contravention of, applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer's Copyright and Related Rights and associated claims and causes of action, whether now known or unknown (including existing as well as future claims and causes of action), in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each member of the public at large and to the detriment of Affirmer's heirs and successors, fully intending that such Waiver shall not be subject to revocation, rescission, cancellation, termination, or any other legal or equitable action to disrupt the quiet enjoyment of the Work by the public as contemplated by Affirmer's express Statement of Purpose.

3. __Public License Fallback.__ Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer's express Statement of Purpose. In addition, to the extent the Waiver is so judged Affirmer hereby grants to each affected person a royalty-free, non transferable, non sublicensable, non exclusive, irrevocable and unconditional license to exercise Affirmer's Copyright and Related Rights in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "License"). The License shall be deemed effective as of the date CC0 was applied by Affirmer to the Work. Should any part of the License for any reason be judged legally invalid or ineffective under applicable law, such partial invalidity or ineffectiveness shall not invalidate the remainder of the License, and in such case Affirmer hereby affirms that he or she will not (i) exercise any of his or her remaining Copyright and Related Rights in the Work or (ii) assert any associated claims and causes of action with respect to the Work, in either case contrary to Affirmer's express Statement of Purpose.

4. __Limitations and Disclaimers.__

    a. No trademark or patent rights held by Affirmer are waived, abandoned, surrendered, licensed or otherwise affected by this document.

    b. Affirmer offers the Work as-is and makes no representations or warranties of any kind concerning the Work, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law.

    c. Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof, including without limitation any person's Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work.

    d. Affirmer understands and acknowledges that Creative Commons is not a party to this document and has no duty or obligation with respect to this CC0 or use of the Work.
