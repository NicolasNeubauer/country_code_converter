import unittest
import country_code_converter, sources

table = [
    ['Austria', 'Oesterreich', 'AT', 'AUT', '040', 'A']
    ]

class TestIndexCreation(unittest.TestCase):

    def testColIndexCreation(self):
        index = country_code_converter.create_column_index(table, 0)
        self.assertEqual(index['Austria'][2], table[0][2])


    def testIndexCreation(self):
        index = country_code_converter.create_index(table)
        self.assertEqual(index['name_english']['Austria'][2], table[0][2])


    def testGetCC(self):
        index = country_code_converter.create_index(table)

        row = country_code_converter.get_cc('name_english', 'Austria', index=index)
        self.assertEqual(table[0], row)

        col = country_code_converter.get_cc('name_english', 'Austria', 'car', index=index)
        self.assertEqual(table[0][5], col)
        
        
    def testCCParser(self):
        table = country_code_converter.create_table(sources.country_codes)
        lengths = set([len(row) for row in table])
        self.assertEqual(len(lengths), 1)


    def testOutput(self):
        self.assertEqual(country_code_converter.get_cc('name_english', 'Italy', 'alpha-2'), 'IT')
        self.assertEqual(country_code_converter.get_cc('name_german', 'Deutschland', 'car'), 'D')