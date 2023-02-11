# DSS-Project-20221
# Dependencies: 
- lxml
- bs4
- selenium
- pandas, numpy
- googlemaps
# Run code
- Run model.ipynb and input users' expected price, users' location and dishes they want to eat
- Topsis ranking algorithm: python topsis.py topsis_data.csv "1,1,1,1" "+,+,+,+" result.csv 
+ "1,1,1,1" is the configurable array of weights
+ "+,+,+,+" is the signs of attributes (Cost attributes are assigned as "-" and benefit attributes are assigned as "+". For example, attribute "Price" is assigned as "-" since we want it to be minimized)
- Recommendation model (Cosine Similarity): Users can choose top k restaurants based on their pass experience
