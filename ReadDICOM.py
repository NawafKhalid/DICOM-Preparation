import pydicom as di
import os
from os import listdir
import numpy as np

PathDicom = "Path/to/DICOM/folders/"
DCMFiles = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            DCMFiles.append(os.path.join(dirName,filename))
print("Number of (.dcm) files =", len(DCMFiles))