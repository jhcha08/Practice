import zipfile
         
fantasy_zip = zipfile.ZipFile('/home/hallasan/junghun/BSR/trainsets/trainH_flikr/Flickr2K.zip')
fantasy_zip.extractall('/home/hallasan/junghun/BSR/trainsets/trainH_flikr')
 
fantasy_zip.close()