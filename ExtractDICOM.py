import pydicom as di
Images1 = []
for k in DCMFiles:
    Images = di.read_file(k,force=True)
    Images1.append(Images.pixel_array)