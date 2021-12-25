import numpy as np
from PIL import Image

mtl_text = open("LE07_L2SP_099023_20010409_20200917_02_T1_MTL.txt", "r")

corners = ['CORNER_UL_LAT_PRODUCT', 'CORNER_UL_LON_PRODUCT', 'CORNER_UR_LAT_PRODUCT', 'CORNER_UR_LON_PRODUCT',
'CORNER_LL_LAT_PRODUCT', 'CORNER_LL_LON_PRODUCT', 'CORNER_LR_LAT_PRODUCT', 'CORNER_LR_LON_PRODUCT']

coordinates = []
lines = mtl_text.readlines()

for line in lines:
    line = line.strip()
    if line[0:21] in corners:
        coordinates.append(float(line[24:]))
#print(coordinates)
array_coord = np.array([coordinates[0::2], coordinates[1::2]])
print(array_coord)


delta_y = abs(coordinates[0] - coordinates[4])
delta_x = abs(coordinates[1] - coordinates[3])
print(delta_x, delta_y)

x = 4035
y = 4035

density_x = delta_x/x
density_y = delta_y/y
print(density_x, density_y)

buz_lat = 53.02
buz_lon = 158.39

ul_dif_lat = coordinates[0] - buz_lat
ul_dif_lon = coordinates[1] - buz_lon
print(ul_dif_lat, ul_dif_lon)

pixel_lat = ul_dif_lat / density_y
pixel_lon = ul_dif_lon / density_x
print(pixel_lat, pixel_lon)

point_buz_x = 4035 - 150
point_buz_y = 4035 - 150
point_lr_x = 4035 + 150
point_lr_y = 4035 + 150

image = Image.open('LE07_L2SP_099023_20010409_20200917_02_T1_SR_B4.TIF')
cropped = image.crop((point_buz_x, point_buz_y, point_lr_x, point_lr_y))
cropped.save('C:\\Users\\Константин\\PycharmProjects\\pythonProject10\\cropped.TIF')
