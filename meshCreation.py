import numpy as np


class MeshCreation:
    def __init__(self, degree, height, radius):
        self.degree = degree
        self.height = height
        self.radius = radius

    def create_mesh(self, X_12, Y_12, R_12, X_21, Y_21, R_21, x_1, y_1, r_1, x_2, y_2, r_2, deg_array, deg_step, gawaitaHeight, gawaitaThickness, ochi):

        x_array = []
        y_array = []
        z_array = []
        startDeg = deg_array[0]
        endDeg = deg_array[len(deg_array) - 1]
        degree = np.arange(startDeg, endDeg, deg_step, dtype=float).tolist()
        for i in degree:
            if deg_1 <= i < deg_2:
                x_array.append(X_12 + R_12 * np.cos(np.radians(i)))
                y_array.append(Y_12 + R_12 * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)
                x_array.append(X_12 + (R_12 - ochi) * np.cos(np.radians(i)))
                y_array.append(Y_12 + (R_12 - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(X_12 + (R_12 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
                y_array.append(Y_12 + (R_12 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(X_12 + (R_12 - gawaitaThickness) * np.cos(np.radians(i)))
                y_array.append(Y_12 + (R_12 - gawaitaThickness) * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)

            if deg_2 <= i < deg_3:
                x_array.append(x_2 + r_2 * np.cos(np.radians(i)))
                y_array.append(y_2 + r_2 * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)
                x_array.append(x_2 + (r_2 - ochi) * np.cos(np.radians(i)))
                y_array.append(y_2 + (r_2 - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(x_2 + (r_2 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
                y_array.append(y_2 + (r_2 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(x_2 + (r_2 - gawaitaThickness) * np.cos(np.radians(i)))
                y_array.append(y_2 + (r_2 - gawaitaThickness) * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)

            if deg_3 <= i < deg_4:
                x_array.append(X_21 + R_21 * np.cos(np.radians(i)))
                y_array.append(Y_21 + R_21 * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)
                x_array.append(X_21 + (R_21 - ochi) * np.cos(np.radians(i)))
                y_array.append(Y_21 + (R_21 - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(X_21 + (R_21 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
                y_array.append(Y_21 + (R_21 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(X_21 + (R_21 - gawaitaThickness) * np.cos(np.radians(i)))
                y_array.append(Y_21 + (R_21 - gawaitaThickness) * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)

            if deg_4 <= i <= deg_5:
                x_array.append(x_1 + r_1 * np.cos(np.radians(i)))
                y_array.append(y_1 + r_1 * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)
                x_array.append(x_1 + (r_1 - ochi) * np.cos(np.radians(i)))
                y_array.append(y_1 + (r_1 - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(x_1 + (r_1 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
                y_array.append(y_1 + (r_1 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
                z_array.append(0.0)
                x_array.append(x_1 + (r_1 - gawaitaThickness) * np.cos(np.radians(i)))
                y_array.append(y_1 + (r_1 - gawaitaThickness) * np.sin(np.radians(i)))
                z_array.append(gawaitaHeight)

        new_array = x_array + y_array + z_array
        temp_a = np.array(new_array)
        gawaita_array = np.reshape(temp_a, (3, len(degree) * 4))
        return gawaita_array

    def PolygonPtsCalc(self, xyrArray, RArray):  # 多角形の小円1,2と外接円の半径Rから外接円の中心座標と絶対角度degを求める
        xyrArray = np.arange(24)
        RArray = np.arange(8)
        xyr_Array = np.array(xyrArray).reshape(-1, 3)
        R_Array = np.array(RArray)
        xyr_ptsNum = len(xyr_Array)
        R_arrayLength = len(R_Array)
        numOfPts = len(xyr_Array)
        X_Array = []
        Y_Array = []
        p_Array = []
        q_Array = []
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
            X, Y, p1, q1, p2, q2 = self.circlePtDx(x1, y1, r1, x2, y2, r2, R)
            X_Array.append(X)
            Y_Array.append(Y)
            deg = [R_arrayLength]
        for k in range(0, R_arrayLength):

            deg[k] = self.vec2deg(x1 - X12, y1 - Y12)
            deg2 = deg1 + self.Pt2Angle(p1_12, q1_12, X12, Y12, p2_12, q2_12)
            deg3 = deg2 + self.Pt2Angle(p2_12, q2_12, x2, y2, p1_21, q1_21)
            deg4 = deg3 + self.Pt2Angle(p1_21, q1_21, X21, Y21, p2_21, q2_21)
            deg5 = deg4 + self.Pt2Angle(p2_21, q2_21, x1, y1, p1_12, q1_12)
            X = [X12, X21]
            Y = [Y12, Y21]
            deg = [deg1, deg2, deg3, deg4, deg5]
            _, clockWise12 = self.vector2Angle(x2 - x1, y2 - y1, x1 - x2, y1 - y2)
            _, clockWise21 = self.vector2Angle(x1 - x2, y1 - y2, x2 - x1, y2 - y1)
            if clockWise12 and clockWise21:
                return X, Y, deg, True
            else:
                return X, Y, deg, False

    def digonPtsCalc(self, x1, y1, r1, x2, y2, r2, R12, R21):  # 小判型の小円1,2と外接円の半径Rから外接円の中心座標と絶対角度degを求める
        X12, Y12, p1_12, q1_12, p2_12, q2_12 = self.circlePtDx(x1, y1, r1, x2, y2, r2, R12)  # p1,P2は小円の番号ではない
        X21, Y21, p1_21, q1_21, p2_21, q2_21 = self.circlePtDx(x2, y2, r2, x1, y1, r1, R21)
        deg1 = self.vec2deg(x1 - X12, y1 - Y12)
        deg2 = deg1 + self.Pt2Angle(p1_12, q1_12, X12, Y12, p2_12, q2_12)
        deg3 = deg2 + self.Pt2Angle(p2_12, q2_12, x2, y2, p1_21, q1_21)
        deg4 = deg3 + self.Pt2Angle(p1_21, q1_21, X21, Y21, p2_21, q2_21)
        deg5 = deg4 + self.Pt2Angle(p2_21, q2_21, x1, y1, p1_12, q1_12)
        X = [X12, X21]
        Y = [Y12, Y21]
        deg = [deg1, deg2, deg3, deg4, deg5]
        _, clockWise12 = self.vector2Angle(x2 - x1, y2 - y1, x1 - x2, y1 - y2)
        _, clockWise21 = self.vector2Angle(x1 - x2, y1 - y2, x2 - x1, y2 - y1)
        if clockWise12 and clockWise21:
            return X, Y, deg, True
        else:
            return X, Y, deg, False

    def circlePtDx(self, x1, y1, r1, x2, y2, r2, R):  # 二つの円に外接する半径Rの円の中心座標を求める

        if round(x1, 5) == round(x2, 5) and round(y1, 5) != round(y2, 5):
            Y1 = ((r2 - r1) * (2 * R - r2 - r1) + y2**2 - y1**2) / 2 / (y2 - y1)
            X1 = np.sqrt((R - r1)**2 - (Y1 - y1)**2) + x1
            Y2 = Y1
            X2 = -np.sqrt((R - r1)**2 - (Y1 - y1)**2) + x1

        if round(x1, 5) != round(x2, 5) and round(y1, 5) == round(y2, 5):
            X1 = ((r2 - r1) * (2 * R - r2 - r1) + x2**2 - x1**2) / 2 / (x2 - x1)
            Y1 = np.sqrt((R - r1)**2 - (X1 - x1)**2) + y1
            X2 = X1
            Y2 = -np.sqrt((R - r1)**2 - (X1 - x1)**2) + y1

        if round(x1, 5) != round(x2, 5) and round(y1, 5) != round(y2, 5):
            a = (y1 - y2) / (x2 - x1)
            b = ((r2 - r1) * (2 * R - r2 - r1) + (x2**2 - x1**2) + (y2**2 - y1**2)) / 2 / (x2 - x1)
            Y1 = (-2 * (a * b - y1 - x1 * a) + np.sqrt(4 * (a * b - y1 - x1 * a)**2 - 4 * (a**2 + 1) * (b**2 + y1**2 + x1**2 - 2 * b * x1 - (R - r1)**2))) / 2 / (a**2 + 1)
            X1 = a * Y1 + b
            Y2 = (-2 * (a * b - y1 - x1 * a) - np.sqrt(4 * (a * b - y1 - x1 * a)**2 - 4 * (a**2 + 1) * (b**2 + y1**2 + x1**2 - 2 * b * x1 - (R - r1)**2))) / 2 / (a**2 + 1)
            X2 = a * Y2 + b

        u = np.array([x1 - X1, y1 - Y1, 0])
        v = np.array([x2 - X1, y2 - Y1, 0])
        x = np.cross(u, v)

        if x[2] > 0:
            # print("z=positive")
            X = X1
            Y = Y1
        else:
            # print("z=negative")
            X = X2
            Y = Y2
        D = np.sqrt((x1 - X)**2 + (y1 - Y)**2)
        p1 = R * (x1 - X) / D + X
        q1 = R * (y1 - Y) / D + Y

        D = np.sqrt((x2 - X)**2 + (y2 - Y)**2)
        p2 = R * (x2 - X) / D + X
        q2 = R * (y2 - Y) / D + Y

        return X, Y, p1, q1, p2, q2