import rasterio
import matplotlib.pyplot as plt

img3 = rasterio.open('LE07_L2SP_099023_20010409_20200917_02_T1_SR_B3.TIF')
img4 = rasterio.open('LE07_L2SP_099023_20010409_20200917_02_T1_SR_B4.TIF')

img3_read = img3.read(1)
img4_read = img4.read(1)

red = img3_read.astype('float32')
nir = img4_read.astype('float32')

ndvi = (nir - red) / (nir + red)

ndviImage = rasterio.open('ndvi.tiff','w',driver='Gtiff',
                          width=img3.width,
                          height=img3.height,
                          count=1, crs=img3.crs,
                          transform=img3.transform,
                          dtype='float32')
ndviImage.write(ndvi,1)
ndviImage.close()

ndvi = rasterio.open("ndvi.tiff").read(1)
fig = plt.figure(figsize=(15, 15))

plt.imshow(ndvi)
plt.show()
