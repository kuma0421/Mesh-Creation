import numpy as np

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
    x1 = xyr_Array[i][0]
    if 4 // 2 == 1:
        print("奇数")
    else:
        print("偶数")
    deg = []
    deg.append(i)

print(deg)

"""
deg0 = self.vec2deg(x1 - X12, y1 - Y12)
deg1 = deg0 + self.Pt2Angle(x1, y1, X12, Y12, x2, y2)
deg2 = deg1 + self.Pt2Angle(X12, Y12, x2, y2, X21, Y21)
deg3 = deg2 + self.Pt2Angle(x2, y2, X21, Y21, x1, y1)
deg4 = deg3 + self.Pt2Angle(X21, Y21, x1, y1, X12, Y12)

deg0 = self.vec2deg(x1 - X12, y1 - Y12)
deg1 = deg0 + self.Pt2Angle(x1, y1, X12, Y12, x2, y2)
deg2 = deg1 + self.Pt2Angle(X12, Y12, x2, y2, X23, Y23)
deg3 = deg2 + self.Pt2Angle(x2, y2, X23, Y23, x3, y3)
deg4 = deg3 + self.Pt2Angle(X23, Y23, x3, y3, X31, Y31)
deg5 = deg4 + self.Pt2Angle(x3, y3, X31, Y31, x1, y1)
deg6 = deg5 + self.Pt2Angle(X31, Y31, x1, y1, X12, Y12)

deg0 = self.vec2deg(x1 - X12, y1 - Y12)
deg1 = deg0 + self.Pt2Angle(x1, y1, X12, Y12, x2, y2)
deg2 = deg1 + self.Pt2Angle(X12, Y12, x2, y2, X23, Y23)
deg3 = deg2 + self.Pt2Angle(x2, y2, X23, Y23, x3, y3)
deg4 = deg3 + self.Pt2Angle(X23, Y23, x3, y3, X34, Y34)
deg5 = deg4 + self.Pt2Angle(x3, y3, X34, Y34, x4, y4)
deg6 = deg5 + self.Pt2Angle(X34, Y34, x4, y4, X41, Y41)
deg7 = deg6 + self.Pt2Angle(x4, y4, X41, Y41, x1, y1)
deg8 = deg7 + self.Pt2Angle(X41, Y41, x1, y1, X12, Y12)

deg0 = self.vec2deg(x1 - X12, y1 - Y12)
deg1 = deg0 + self.Pt2Angle(p1_12, q1_12, X12, Y12, p2_12, q2_12)
deg2 = deg1 + self.Pt2Angle(X12, Y12, x2, y2, X23, Y23)
deg3 = deg2 + self.Pt2Angle(x2, y2, X23, Y23, x3, y3)
deg4 = deg3 + self.Pt2Angle(X23, Y23, x3, y3, X34, Y34)
deg5 = deg4 + self.Pt2Angle(x3, y3, X34, Y34, x4, y4)
deg6 = deg5 + self.Pt2Angle(X34, Y34, x4, y4, X45, Y45)
deg7 = deg6 + self.Pt2Angle(x4, y4, X45, Y45, x5, y5)
deg8 = deg7 + self.Pt2Angle(X45, Y45, x5, y5, X51, Y51)
deg9 = deg8 + self.Pt2Angle(x5, y5, X51, Y51, x1, y1)
deg10 = deg9 + self.Pt2Angle(X51, Y51, x1, y1, X12, Y12)

xyrArray = []
deg0 = self.vec2deg(x1 - X12, y1 - Y12)
deg1 = deg0 + self.Pt2Angle(x1, y1, X12, Y12, x2, y2)
deg2 = deg1 + self.Pt2Angle(X12, Y12, x2, y2, X23, Y23)
deg3 = deg2 + self.Pt2Angle(x2, y2, X23, Y23, x3, y3)
deg4 = deg3 + self.Pt2Angle(X23, Y23, x3, y3, X34, Y34)
deg5 = deg4 + self.Pt2Angle(x3, y3, X34, Y34, x4, y4)
deg6 = deg5 + self.Pt2Angle(X34, Y34, x4, y4, X45, Y45)
deg7 = deg6 + self.Pt2Angle(x4, y4, X45, Y45, x5, y5)
deg8 = deg7 + self.Pt2Angle(X45, Y45, x5, y5, X56, Y56)
deg9 = deg8 + self.Pt2Angle(x5, y5, X56, Y56, x6, y6)
deg10 = deg9 + self.Pt2Angle(X56, Y56, x6, y6, X61, Y61)
deg11 = deg10 + self.Pt2Angle(x6, y6, X61, Y61, x1, y1)
deg12 = deg11 + self.Pt2Angle(X61, Y61, x1, y1, X12, Y12)
"""
