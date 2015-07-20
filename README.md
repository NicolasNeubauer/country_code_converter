# country_code_converter
Converts between different naming schemas for countries (ISO2, ISO3, car plate IDs, numerical, English, German, centroid). 

`country_code_converter.py` exposes the main method `get_cc`. It looks for a country with value `from_value` (e.g. DEU) in the column specified by `from_standard` (e.g. iso3) and returns, for the column defined by `to_standard` (e.g. iso2) the corresponding value (e.g. DE), or the whole row, if `to_standard` is left unspecified. 

Some additional information is included which is not, technically speaking, a country code, like full names or the centroid.

## Command-line usage
python country_code_converter.py from_standard from_value [to_standard]

## Available naming standards
    name_english
    alpha-2
    alpha-3
    numeric
    name_german
    car
    centroid

## Examples
### Command-line 
    python country_code_converter.py name_english Italy car
    > I

    python country_code_converter.py name_english Italy

    > {'name_english': 'Italy', 'car': 'I', 'numeric': '380', 'name_german': 'Italien', 'alpha-2': 'IT', 'alpha-3': 'ITA'}

### Python
    import country_code_converter
    print country_code_converter.get_cc('name_english', 'Italy', 'car')

    > I

## License 
MIT

## Acknowledgements
This code wraps the contents of these pages:
- https://en.wikipedia.org/wiki/ISO_3166-1 for the country codes
- https://de.wikipedia.org/wiki/Liste_der_Kfz-Nationalit%C3%A4tszeichen for the car plate identifiers
- http://gothos.info/resource_files/country_centroids.zip

## TODO
- render JavaScript code
- persist index for faster response