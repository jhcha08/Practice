import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('/root/images/train/warped.zip', 'w')
 
for folder, subfolders, files in os.walk('/root/images/train/warped'):
 
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '/root/images/train/warped'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()
