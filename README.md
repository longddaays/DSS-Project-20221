# DSS-Project-20221
# Dependencies: 
- lxml
- bs4
- selenium
- pandas, numpy
- googlemaps
# Run code
- Topsis ranking algorithm: python topsis.py topsis_data.csv "1,1,1,1" "+,+,+,+" result.csv 
- "1,1,1,1" is the configurable array of weights
- "+,+,+,+" is the signs of attributes (Cost attributes are assigned as "-" and benefit attributes are assigned as "+". For example, attribute "Price" is assigned as "-" since we want it to be minimized)
