import csv
import io
import sys
import re
# scenarios which need to be handled:
# - field is escaped by quotes, and the quoted string contains quotes and
# semicolon the delimiter of the csv is semicolon as well
# - field which is supposed to be inserted as a number to database contains
# spaces and eurocurrency sign. For example "1 000 000 €". Processing is
# needed in order to extract numeric value without whitespaces and euro sign.
# - field which is saved as number to database contains " - € "


def cleanup(path_to_file):
    """Process a file."""
    with open(path_to_file, newline='', encoding='windows-1252') as csvfile:
        for line in csvfile:
            result = clean_line(line)
            print(result)


def clean_line(input_string):
    """Clean csv file in order to load it to PostgreSQL database."""
    with io.StringIO(input_string) as csvfile:
        linereader = csv.reader(csvfile, delimiter=';')
        for row in linereader:
            if row[0].find('"') > 0 or row[0].find(';') > 0:
                row[0] = row[0].replace('"', '""')
                row[0] = "\""+row[0]+"\""
            row[3] = _trim_whitespace(row[3])
            row[3] = _symbol_removal(row[3])
            row[7] = _trim_whitespace(row[7])
            row[7] = _symbol_removal(row[7])
            if row[9].find(';') > 0:  # if row contains semicolon, the field will be double quoted, so we will add the double quotes back
                row[9] = "\""+row[9]+"\""
            if row[11].find(';') > 0:  # if row contains semicolon, the field will be double quoted, so we will add the double quotes back
                row[11] = "\""+row[11]+"\""

            line = ';'.join((row))
            return line


def _symbol_removal(input_string):
    if input_string != '-€':
        return _remove_euro(input_string)
    if input_string == '-€':
        return ''


def _remove_euro(input_string):
    return input_string.replace('€', '')


def _trim_whitespace(input_string):
    # Remove all whitespace from string
    return ''.join(map(str.strip,
                       re.split(' ', input_string)))


def _test_trimming1():
    if not "12345" == _trim_whitespace("123 4 5"):
        print("test_trimming1 failed")


if __name__ == '__main__':
    cleanup(sys.argv[1])
