# country_code_converter
Converts between different naming schemas for countries (ISO2, ISO3, car plate IDs, numerical, english, German). 

`country_code_converter.py` exposes the main method `get_cc` which looks for a country with value `from_value` in the column for `from_standard` and returns the column for `to_standard` or the whole row, if `to_standard` is left unspecified.

## Command-line usage
python country_code_converter.py from_standard from_value [to_standard]

## Available naming standards
    name_english
    alpha-2
    alpha-3
    numeric
    name_german
    car

## Command-line examples
    python country_code_converter.py name_english Italy car
I

    python country_code_converter.py name_english Italy
{'name_english': 'Italy', 'car': 'I', 'numeric': '380', 'name_german': 'Italien', 'alpha-2': 'IT', 'alpha-3': 'ITA'}

## Code examples
    import country_code_converter
    print country_code_converter.get_cc('name_english', 'Italy', 'car')

I

## License 
MIT

## Acknowledgements
This code wraps the contents of two Wikipedia pages:
- https://en.wikipedia.org/wiki/ISO_3166-1 for the country codes
- https://de.wikipedia.org/wiki/Liste_der_Kfz-Nationalit%C3%A4tszeichen for the car plate identifiers

