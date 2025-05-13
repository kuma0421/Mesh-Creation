import numpy as np
# import pprint


xy_Array = np.array([[0, 0],
              [2, 0],
              [1, 3],
              [0, 2],
              [2, 2]])

numOfPts = len(xy_Array)
print("numOfPts: ", numOfPts)
temp=np.array([0] * numOfPts)
print("temp: ", temp)
temp = np.reshape(temp, (numOfPts, 1))
pts_Array=np.append(xy_Array, temp, axis=1)
print("original pts_Array: ", pts_Array)
for i in range(numOfPts-2):
    u = pts_Array[1]-pts_Array[0]
    v = pts_Array[i+2]-pts_Array[0]
    print("u: ", u)
    print("v: ", v)
    dt = np.dot(u, v)
    print("dot product: ", dt)
    crs = np.cross(u, v)  # uとvの外積を計算
    print("cross product: ", crs)
    n = np.linalg.norm(u) * np.linalg.norm(v)
    c = dt / n
    print("u.v: ", c)
    deg = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))
    print('{}x{}のはさむ角度は: {}'.format(i, i + 1, deg))
    pts_Array[i+2][2] = deg
print("pts_Array: ", pts_Array)
pts_Array = sorted(pts_Array, key=lambda x: x[2])
print("sorted pts_Array: ", pts_Array)
new_pts_Array = np.delete(pts_Array, 2, axis=1)  # 角度の列を削除
print("new_pts_Array: ", new_pts_Array)
"""
x=pts_Array[0]-pts_Array[1]
print("pts_Array[0]", pts_Array[0])
print("pts_Array[1]", pts_Array[1])
print("x: ", x)
x_array = [[0,3,5],
            [2,1,4],
            [3,4,2]]
y=sorted(x_array, key=lambda x: x[2])
pprint.pprint(y, width=20)

def polyginPtsCheck(self, pts_Array):  # 多角形の座標を与えると、反時計回りに座標点を並べ替える
    u = np.array([x1, y1, 0])
    v = np.array([x2, y2, 0])

    return pts_Array


def vector2Angle(self, x1, y1, x2, y2):  # 半時計回りの順番で2つのベクトルの挟む角を求める（０～３６０°）
    clockWise = False
    u = np.array([x1, y1, 0])
    v = np.array([x2, y2, 0])

    i = np.dot(u, v)
    n = LA.norm(u) * LA.norm(v)

    c = i / n
    a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

    x = np.cross(u, v)
    if x[2] < 0:
        a = 360 - a
        clockWise = True
    # print("Degee is", a)  # 90.0
    # print("Cross Product is", x)
    return a, clockWise

def vec2deg(self, x, y):  # ベクトルの角度を求める（０～３６０°） (x,y)の位置ベクトルがx軸となす角
    if y >= 0:
        deg = np.degrees(np.arccos(x / np.sqrt(x**2 + y**2)))
        return deg
    else:
        deg = 360.0 - np.degrees(np.arccos(x / np.sqrt(x**2 + y**2)))
        return deg
"""
