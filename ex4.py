# import numpy as np
"""
xyrArray = np.arange(24)
print("original xyrArray: ", xyrArray)
RArray = np.arange(8)
print("original RArray: ", RArray)
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
"""
print("1 % 2=", 1 % 2)
numOfXyzPts = 3
for k in range(0, numOfXyzPts*2+1):
    if k == 0:
        print("k=",k)
    elif k != 0 and k // 2 == 1:  # 奇数の時
        print("k=",k)
    elif k != 0 and k // 2 == 0 and k != numOfXyzPts*2:  # 偶数の時
        print("k=",k)
    else:  # 最後の偶数の時
        print("k=",k)
