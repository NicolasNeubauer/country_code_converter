import sys
import sources, source_parsers


# helper methods for parsing and index construction
def create_table(cc):
    """create initial table from Wikipedia country code table"""
    parser = source_parsers.CCParser()
    parser.feed(cc)
    return parser.table


def add_car_signs(table, indexCol, cs):
    """add car signs and German names from another Wikipedia table"""
    parser = source_parsers.CarParser()
    parser.feed(cs)
    cctable = parser.table

    keyToRow = dict([(row[indexCol], row) for row in table])

    for row in cctable:
        # incomplete fields? ignore
        if len(row)<3:
            continue

        # not in country codes? ignore
        if not row[2] in keyToRow:
            continue

        # comment asterisk? remove asterisk
        if row[0][-1] == "*":
            row[0] = row[0][0:-1]

        # get row for ISO-2 value, append German name and car sign
        tablerow = keyToRow[row[2]]
        tablerow.append(row[1])
        tablerow.append(row[0])
    
    for row in table:
        if len(row)==4:
            row.append(None)
            row.append(None)


def create_index(table):
    """create index from searched column and value to corresponding table row"""
    return dict([(column, create_column_index(table, colindex))
                 for colindex, column in enumerate(columns)])


def create_column_index(table, colindex):
    """creates index from column value to corresponding table row"""
    return dict([(row[colindex], row) for row in table])


# initialization
columns = ['name_english', 'iso2', 'iso3', 'numeric', 'name_german', 'car']
column_to_index = dict([(name, index) for index, name in enumerate(columns)])
supported_languages = ['english', 'german']
table = create_table(sources.country_codes)
add_car_signs(table, column_to_index['iso2'], sources.car_signs)
index = create_index(table)


# public interface
def get_cc(from_column, from_value, to_column=None, index=index):
    """get value of to_column (or whole row as dict if to_column unset) where
       from_column == from_value"""
    row = index[from_column][from_value]
    if not to_column:
        return dict([(column, row[colindex])
                     for colindex, column
                     in enumerate (columns)])
    column = column_to_index[to_column]
    return row[column]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Converts between different naming schemes for countries."
        print "Usage: python country_code_converter.py from_standard from_value [to_standard]"
        print
        print "Available naming standards:"
        for column in columns:
            print "  %s" % column
        print 
        print "Examples:"
        print "> python country_code_converter.py name_english Italy car"
        print get_cc('name_english', 'Italy', 'car')
        print
        print "> python country_code_converter.py name_english Italy"
        print get_cc('name_english', 'Italy')

        sys.exit(1)

    to_column = None
    from_column = sys.argv[1]
    from_value = sys.argv[2]
    if len(sys.argv)>3:
        to_column = sys.argv[3]
    print get_cc(from_column, from_value, to_column)
