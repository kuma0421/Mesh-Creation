import numpy as np

xyrArray = np.arange(24)
RArray = np.arange(8)
xyr_Array = np.array(xyrArray).reshape(-1, 3)
R_Array = np.array(RArray)
xyr_ptsNum = len(xyr_Array)
R_arrayLength = len(R_Array)
numOfPts = len(xyr_Array)

for i in range(0, xyr_ptsNum):
    x1 = xyr_Array[i][0]
    y1 = xyr_Array[i][1]
    z1 = xyr_Array[i][2]

    if i != numOfPts-1:
        j=i+1
        x2 = xyr_Array[j][0]
        y2 = xyr_Array[j][1]
        z2 = xyr_Array[j][2]
    if i == numOfPts-1:
        x2 = xyr_Array[0][0]
        y2 = xyr_Array[0][1]
        z2 = xyr_Array[0][2]
    R = R_Array[i]
    print(x1, y1, z1, x2, y2, z2, R)
    


