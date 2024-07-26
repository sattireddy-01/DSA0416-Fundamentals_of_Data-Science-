import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5, 6],
    'location': ['A', 'A', 'B', 'B', 'C', 'C'],
    'number_of_bedrooms': [3, 5, 4, 2, 6, 3],
    'area_sq_ft': [1500, 2500, 1800, 1200, 3000, 1600],
    'listing_price': [500000, 750000, 600000, 400000, 850000, 550000]
}

property_data = pd.DataFrame(data)
average_listing_price = property_data.groupby('location')['listing_price'].mean().reset_index()
print("Average listing price in each location:")
print(average_listing_price)
properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4].shape[0]
print("\nNumber of properties with more than four bedrooms:")
print(properties_more_than_four_bedrooms)
property_with_largest_area = property_data.loc[property_data['area_sq_ft'].idxmax()]
print("\nProperty with the largest area:")
print(property_with_largest_area)
