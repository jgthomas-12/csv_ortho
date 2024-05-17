import pandas as pd
import pygeodesy
from pygeodesy.ellipsoidalKarney import LatLon


ginterpolator = pygeodesy.GeoidKarney("./geoids/egm2008-5.pgm")

sheets_path = "/Users/jessethomas/Desktop/Desktop - Turing (2)/2024_projects/collier/csv_orthometric/230404-4 (2).csv"
data = pd.read_csv(sheets_path)

csv_data = data[["Latitude", "Longitude", "Ellipsoidal height (m)"]]

geoid_heights = []
orthometric_heights_meters = []
orthometric_heights_feet = []

for index, row in csv_data.iterrows():
  lat = row["Latitude"]
  lon = row["Longitude"]
  ellipsoidal_height = row["Ellipsoidal height (m)"]
  single_position = LatLon(lat, lon)
  geoid_height = ginterpolator(single_position)
  orthometric_height_meters = ellipsoidal_height - geoid_height
  geoid_heights.append(geoid_height)
  orthometric_heights_meters.append(orthometric_height_meters)

  orthometric_height_feet = orthometric_height_meters * 3.28084
  orthometric_heights_feet.append(orthometric_height_feet)

data.insert(data.columns.get_loc("Ellipsoidal height (m)") + 1, "Geoid Height (m)", geoid_heights)
data.insert(data.columns.get_loc("Geoid Height (m)") + 1, "Orthometric Height (m)", orthometric_heights_meters)
data.insert(data.columns.get_loc("Orthometric Height (m)") + 1, "Orthometric Height (ft)", orthometric_heights_feet)


# Save the modified DataFrame back to a CSV file
# Specify the desired path for the output CSV file
output_csv_path = "/Users/jessethomas/Desktop/Desktop - Turing (2)/2024_projects/collier/csv_orthometric/230404-4_ortho_jt_test.csv"
data.to_csv(output_csv_path, index=False)


# print(data)