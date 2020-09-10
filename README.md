# DICOM-Preparation
DICOM format contains a lot of information and sometimes we only need the images, either because the information is private or we need to reduce the size even though the information not as big as the image itself. And this might help anyone how work with deep learning, either to read the (.dcm) files and remove the private data within the files. 

Here a codes to read DICOM organized as shown in the bottom and extracting images pixel array(the image itself) without the metadata.

NOTE: The Files must be organized as
my_directory/ 
| ├── Unnamed_154159/ 
|                   └── IM-0005-0001.dcm 
|                   └── IM-0005–0002.dcm
| ├── Unnamed_136281/ 
|                   └── IM-0001-0001.dcm 
| ├── Unnamed_190381/
|                   └── IM-0002-0001.dcm
|                   └── IM-0002-0001.dcm 
| ├── Unnamed_102430/ 
|                   └── IM-0001-0002.dcm 
.
.
.
.
.


