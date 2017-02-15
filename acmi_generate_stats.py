#
# ACMI Collections - Generate simple stats for ACMI Collection data
#
# This script takes a processed .tsv file of the ACMI collection data release available at:
# https://github.com/ACMILabs/collection/
#
# Place the script at "src/collections_data.tsv" relative to the path of this script
# Run "python acmi_generate_stats.py" and the script will save the following out to a "dist" directory:
#
# JSON format:
# Key names are constructed as lowercase alphanumeric strings, spaces are replaced with underscores
# Keys are prefixed with 'k_' to prevent the script from trying to create keys beginning with a number
#
# /dist/json/categories.json - just the available categories
# /dist/json/indexes.json - a large index listing ids of records for each category
# /dist/json/objects.json - just the individual object records, formatted in JSON, in one large file
# /dist/json/stats.json - just some simple stats of total records for each category
# /dist/json/collections_data_complete.json - a combined JSON file including all of the above
#
# TSV format stats:
# These files contain a list of unsorted counts of each field in a given category, column names are '<field>', 'total'
#
# /dist/tsv/active_carriers_public_types_and_formats_only.tsv
# /dist/tsv/audience_classification.tsv
# /dist/tsv/colour.tsv
# /dist/tsv/creation_date.tsv
# /dist/tsv/form.tsv
# /dist/tsv/genre.tsv
# /dist/tsv/language_keywords.tsv
# /dist/tsv/length.tsv
# /dist/tsv/place_of_production.tsv
# /dist/tsv/sound_audio.tsv
# /dist/tsv/subject_group.tsv


import sys
import csv
import json
import re
import os
import os.path
import collections
import copy

DEFAULT_FILENAME = "src/collections_data.tsv"
DEFAULT_DESTINATION_JSON = "dist/collections_data"
DEFAULT_DESTINATION_JSON_BUCKET = "dist/json"
KEY_PREPEND = "k_"


def get_alpha_num_string(source_string):
    return_string = ""
    match = re.findall(r"\w+", source_string)
    if match:
        return_string = "_".join(match).lower()
    return return_string


def add_or_zero(list_to_check, val):
    return_val = 1
    if val in list_to_check:
        return_val = list_to_check[val]["total"] + 1
    return return_val


def add_indexes(indexes, key_to_check, val, row):
    # Work through building the indexes
    if key_to_check in indexes:
        # Normalise pipe separated values
        if (key_to_check == "genre"
                or key_to_check == "form"
                or key_to_check == "subject_group"
                or key_to_check == "active_carriers_public_types_and_formats_only"
                or key_to_check == "creator_contributor_role"):
            val_list = val.split(" | ")
            for split_val in val_list:
                index_val = KEY_PREPEND + get_alpha_num_string(split_val)
                if not index_val in indexes[key_to_check]:
                    indexes[key_to_check][index_val] = {"name": split_val, "titles": []}
                indexes[key_to_check][index_val]["titles"].append({
                    "id": row[0],
                    "title": row[4],
                    "year": row[8]
                })
        else:
            index_val = KEY_PREPEND + get_alpha_num_string(val)
            if not index_val in indexes[key_to_check]:
                indexes[key_to_check][index_val] = {"name": val, "titles": []}
            indexes[key_to_check][index_val]["titles"].append({
                "id": row[0],
                "title": row[4],
                "year": row[8]
            })
    return indexes


def add_stats(stats, key_to_check, val):
    if key_to_check in stats:
        val_list = val.split(" | ")
        for split_val in val_list:
            parsed_split_val = KEY_PREPEND + get_alpha_num_string(split_val)
            if parsed_split_val not in stats[key_to_check]:
                stats[key_to_check][parsed_split_val] = {
                    "name": "",
                    "total": 0
                }
            stats[key_to_check][parsed_split_val]["name"] = split_val
            stats[key_to_check][parsed_split_val]["total"] = add_or_zero(stats[key_to_check], parsed_split_val)
    return stats


def run_json_convert(filename):
    # open sourcee TSV file
    with open(filename, 'rU') as csvfile:
        # initialise the reader object on the source tsv, using Excel dialect, and specifying that it's tab delimited
        tsv_reader = csv.reader(csvfile, dialect="excel", delimiter="\t")
        # get the first row of the tsv, which is the column header row
        row = next(tsv_reader)
        # cache the first row, as we'll need to refer back to the column headers for generating our JSON keys
        row_zero = row
        # create an empty dictionary where we'll store all the data to be converted to JSON
        huge_json = {}
        # create an empty dictionary for all of the objects in the collection data TSV
        objects = {}
        # create a dictionary for our indexes, with some initial keys for pushing data into later
        categories = {
            "audience_classification": {},
            "colour": {},
            "creation_date": {},
            "active_carriers_public_types_and_formats_only": {},
            "form": {},
            "genre": {},
            "length": {},
            "language_keywords": {},
            "place_of_production": {},
            "sound_audio": {},
            "creator_contributor_role": {},
            "subject_group": {}
        }
        indexes = copy.deepcopy(categories)
        # create a dictionary for our stats, with some initial keys for pushing data into later
        stats = {
            "audience_classification": {},
            "colour": {},
            "creation_date": {},
            "active_carriers_public_types_and_formats_only": {},
            "form": {},
            "genre": {},
            "length": {},
            "language_keywords": {},
            "place_of_production": {},
            "sound_audio": {},
            "subject_group": {}
        }
        # iterate through the rows of the source tsv file
        iterator = 0
        for row in tsv_reader:
            # create empty dictionary for the row of key value pairs we'll be pushing to the object dictionary
            # this also resets the dictionary for each row we go through in this for loop
            row_key_val_pairs = collections.OrderedDict()
            # iterate through each column of the current row of the source tsv
            for idx, val in enumerate(row):
                # construct a key name from the column header (lowercase with dashes instead of spaces)
                key_name = str(row_zero[idx]).lower().replace(" ", "_")
                # add the value for this column to our dictionary of key value pairs for the row

                if (idx == 0):
                    row_key_val_pairs.update({key_name: int(val)})
                elif (idx > 4):
                    row_key_val_pairs.update({key_name: val.split(" | ")})
                # row_key_val_pairs[key_name] = val.split(" | ")
                else:
                    row_key_val_pairs.update({key_name: val})
                # row_key_val_pairs[key_name] = val
                # Work through building the stats for this column
                stats = add_stats(stats, key_name, val)
                # Work through building the indexes for this column
                indexes = add_indexes(indexes, key_name, val, row)
            # add the dictionary of key / value pairs for the row to the objects dictionary, using the Object ID as the key name
            objects[str(row[0])] = row_key_val_pairs

            # Update status in terminal
            iterator += 1
            status = "Parsing row: " + str(iterator)
            sys.stdout.write('%s\r' % status)

        sys.stdout.flush()

        # attach the dictionaries to our huge_json
        huge_json["categories"] = categories
        huge_json["indexes"] = indexes
        huge_json["stats"] = stats
        huge_json["objects"] = objects
        # finally, dump the huge_json dictionary with all our data to JSON!
        # for testing, try adding indent=4 to the json.dump below to see the JSON pretty-printed.
        # Update status in terminal
        sys.stdout.write('Saving to JSON and TSV files\n')
        sys.stdout.flush()

        # Make the directories if they don't already exist
        if not os.path.exists("dist/json"):
            os.makedirs("dist/json")

        if not os.path.exists("dist/tsv"):
            os.makedirs("dist/tsv")

        sys.stdout.write('Saving objects.json\n')
        with open("dist/json/objects.json", 'w') as json_output_file:
            json.dump({"objects": objects}, json_output_file, sort_keys=True)

        sys.stdout.write('Saving categories.json\n')
        with open("dist/json/categories.json", 'w') as json_output_file:
            json.dump({"categories": categories}, json_output_file, sort_keys=True)

        sys.stdout.write('Saving indexes.json\n')
        with open("dist/json/indexes.json", 'w') as json_output_file:
            json.dump({"indexes": indexes}, json_output_file, sort_keys=True)

        sys.stdout.write('Saving stats.json\n')
        with open("dist/json/stats.json", 'w') as json_output_file:
            json.dump({"stats": stats}, json_output_file, sort_keys=True)

        sys.stdout.write('Saving complete collections_data.json\n')
        with open("dist/json/collections_data_complete.json", 'w') as json_output_file:
            json.dump(huge_json, json_output_file, sort_keys=True)
            # Confirm complete!
            sys.stdout.write('Saving complete!\n')
            sys.stdout.flush()

        sys.stdout.write('Saving individual TSV files for each of the stats\n')
        for key, value in stats.items():
            sys.stdout.write('Saving ' + key + '.tsv\n')
            with open("dist/tsv/" + key + ".tsv", 'wb') as tsv_output_file:
                tsv_writer = csv.writer(tsv_output_file, dialect="excel", delimiter="\t")
                tsv_writer.writerow([key, "total"])
                for k, v in stats[key].items():
                    tsv_writer.writerow([v["name"], v["total"]])


def main():
    """
    Accepts a single commmand-line argument to specify the source TSV file. Defaults to DEFAULT_FILENAME
    """
    total = len(sys.argv)
    if total == 2:
        print ("Script name: %s" % str(sys.argv[0]))
        run_json_convert(str(sys.argv[1]))
    elif total == 1:
        print ("Script name: %s" % str(sys.argv[0]))
        run_json_convert(DEFAULT_FILENAME)
    else:
        print("Please enter a single .tsv filename at the command-line.")


if __name__ == "__main__":
    main()
