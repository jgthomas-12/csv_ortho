import pandas as pd
import pygeodesy
from pygeodesy.ellipsoidalKarney import LatLon

ginterpolator = pygeodesy.GeoidKarney("./geoids/egm2008-5.pgm")

excel_path = "/Users/jessethomas/Desktop/Desktop - Turing (2)/2024_projects/collier/csv_orthometric/230404-1_ortho.xlsx"

data_too = pd.read_excel(excel_path)

latitude = data_too["Latitude"]
longitude = data_too["Longitude"]
ellipsoidal_height_meters = data_too["Ellipsoidal height (m)"]
ellipsoidal_height_feet = data_too["Ellipsoidal height (ft)"]

for lat, lon, ell_height in zip(latitude, longitude, ellipsoidal_height_feet):
  single_position = LatLon(lat, lon)

  geoid_height = ginterpolator(single_position)

  orthometric_height = ell_height - geoid_height

  print(f"At lattidude {lat}, longitude {lon}, the orthometric height is: {orthometric_height}")
