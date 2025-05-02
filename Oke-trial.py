
import numpy as np
import pyvista as pv  # Delete for non-Pro version
# from pyvistaqt import BackgroundPlotter  # Delete for non-Pro version


deg_1 = 261.37307344132137
deg_2 = 278.62692655867863
deg_3 = 441.37307344132137
deg_4 = 458.62692655867863
deg_5 = 621.3730734413214
deg_step = 1
X_12 = 15.0
Y_12 = 98.86859966642594
X_21 = 15.0
Y_21 = -98.86859966642594
x_1 = 0.0
y_1 = 0.0
x_2 = 30.0
y_2 = 0.0
r_1 = 50.0
r_2 = 50.0
R_12 = 150.0
R_21 = 150.0
gawaitaHeight = 60.0
gawaitaThickness = 5.0
ochi = 3.0
sokoitaHeight = 10.0
sokoitaThickness = 5.0
gawaitaTop_offsetFromR = 7.5
gawaitaBottom_offsetFromR = 7.75
upperTagaHeight = 42.67
lowerTagaHeight = 10.0
tagaWidth = 5.0
tagaThickness = 1.0

deg_temp = np.arange(deg_1, deg_5, deg_step, dtype=float)
degree = deg_temp.tolist()

# 側板の頂点座標を計算する
# 上側縁
x_array = []
y_array = []
z_array = []
for i in degree:
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + R_12 * np.cos(np.radians(i)))
        y_array.append(Y_12 + R_12 * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(X_12 + (R_12 - gawaitaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - gawaitaThickness) * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(X_12 + (R_12 - ochi) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(X_12 + (R_12 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(X_12 + (R_12 - gawaitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - gawaitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
        x_array.append(X_12 + (R_12 - gawaitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - gawaitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + r_2 * np.cos(np.radians(i)))
        y_array.append(y_2 + r_2 * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(x_2 + (r_2 - gawaitaThickness) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - gawaitaThickness) * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(x_2 + (r_2 - ochi) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(x_2 + (r_2 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(x_2 + (r_2 - gawaitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - gawaitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
        x_array.append(x_2 + (r_2 - gawaitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - gawaitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + R_21 * np.cos(np.radians(i)))
        y_array.append(Y_21 + R_21 * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(X_21 + (R_21 - gawaitaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - gawaitaThickness) * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(X_21 + (R_21 - ochi) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(X_21 + (R_21 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(X_21 + (R_21 - gawaitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - gawaitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
        x_array.append(X_21 + (R_21 - gawaitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - gawaitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + r_1 * np.cos(np.radians(i)))
        y_array.append(y_1 + r_1 * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(x_1 + (r_1 - gawaitaThickness) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - gawaitaThickness) * np.sin(np.radians(i)))
        z_array.append(gawaitaHeight)
        x_array.append(x_1 + (r_1 - ochi) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(x_1 + (r_1 - gawaitaThickness - ochi) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - gawaitaThickness - ochi) * np.sin(np.radians(i)))
        z_array.append(0.0)
        x_array.append(x_1 + (r_1 - gawaitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - gawaitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
        x_array.append(x_1 + (r_1 - gawaitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - gawaitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
print("length of new_array = ", len(new_array))
print("degree = ", len(degree))
outer_top_array = np.reshape(temp_a, (3, len(degree) * 6))

x_array = []
y_array = []
z_array = []
deg_count = len(degree)
faces_array = []
mesh_1 = outer_top_array.T

vertices = np.vstack(mesh_1)

# print("vertices = ",vertices)
# 側板（外面）

for i in range(deg_count):
    if i + 1 == deg_count:
        faces_array.append(4)
        faces_array.append(i)
        faces_array.append(deg_count * 2 + i)
        faces_array.append(deg_count * 2)
        faces_array.append(0)
    else:
        faces_array.append(4)
        faces_array.append(i)
        faces_array.append(deg_count * 2 + i)
        faces_array.append(deg_count * 2 + i + 1)
        faces_array.append(i + 1)
# 側板（内面-上から底板上面まで）
for i in range(deg_count):
    if i + 1 == deg_count:
        faces_array.append(4)
        faces_array.append(deg_count + i)
        faces_array.append(deg_count)
        faces_array.append(deg_count * 4)
        faces_array.append(deg_count * 4 + i)
    else:
        faces_array.append(4)
        faces_array.append(deg_count + i)
        faces_array.append(deg_count + i + 1)
        faces_array.append(deg_count * 4 + i + 1)
        faces_array.append(deg_count * 4 + i)
# 側板（内面-底板下面から下まで）
for i in range(deg_count):
    if i + 1 == deg_count:
        faces_array.append(4)
        faces_array.append(deg_count * 5 + i)
        faces_array.append(deg_count * 5)
        faces_array.append(deg_count * 3)
        faces_array.append(deg_count * 3 + i)
    else:
        faces_array.append(4)
        faces_array.append(deg_count * 5 + i)
        faces_array.append(deg_count * 5 + i + 1)
        faces_array.append(deg_count * 3 + i + 1)
        faces_array.append(deg_count * 3 + i)

# 側板（上小口面）
for i in range(deg_count):
    if i + 1 == deg_count:
        faces_array.append(4)
        faces_array.append(i)
        faces_array.append(0)
        faces_array.append(deg_count)
        faces_array.append(deg_count + i)
    else:
        faces_array.append(4)
        faces_array.append(i)
        faces_array.append(i + 1)
        faces_array.append(deg_count + i + 1)
        faces_array.append(deg_count + i)
# 側板（下小口面）
for i in range(deg_count):
    if i + 1 == deg_count:
        faces_array.append(4)
        faces_array.append(deg_count * 2 + i)
        faces_array.append(deg_count * 3 + i)
        faces_array.append(deg_count * 3)
        faces_array.append(deg_count * 2)
    else:
        faces_array.append(4)
        faces_array.append(deg_count * 2 + i)
        faces_array.append(deg_count * 3 + i)
        faces_array.append(deg_count * 3 + i + 1)
        faces_array.append(deg_count * 2 + i + 1)

plotter = pv.Plotter()
# plotter = BackgroundPlotter()
plotter.enable_parallel_projection()
faces_temp = np.array(faces_array)
faces = np.reshape(faces_temp, ((deg_count) * 5, 5))
surf = pv.PolyData(vertices, faces)

# 底板（上面）
sokoita_Top_faces = []
sokoita_Top_faces.append(deg_count)
for i in range(deg_count):
    sokoita_Top_faces.append(deg_count * 4 + i)
sokoita_Top_faces_temp = np.array(sokoita_Top_faces)
surf1 = pv.PolyData(vertices, sokoita_Top_faces_temp)
# 底板（下面）
sokoita_Bottom_faces = []
sokoita_Bottom_faces.append(deg_count)
for i in range(deg_count):
    sokoita_Bottom_faces.append(deg_count * 6 - 1 - i)
sokoita_Bottom_faces_temp = np.array(sokoita_Bottom_faces)
surf2 = pv.PolyData(vertices, sokoita_Bottom_faces_temp)

# タガ描画のために追加
upper_TagaTop_offsetFromR = ochi - upperTagaHeight * ochi / gawaitaHeight
upper_TagaBottom_offsetFromR = ochi - (upperTagaHeight - tagaWidth) * ochi / gawaitaHeight
lower_TagaTop_offsetFromR = ochi - lowerTagaHeight * ochi / gawaitaHeight
lower_TagaBottom_offsetFromR = ochi - (lowerTagaHeight - tagaWidth) * ochi / gawaitaHeight

x_array = []
y_array = []
z_array = []
for i in degree:  # 上タガ上部（内側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - upper_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - upper_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - upper_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - upper_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - upper_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - upper_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - upper_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - upper_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
innerTop_upperTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []

for i in degree:  # 上タガ上部（外側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - upper_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - upper_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - upper_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - upper_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - upper_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - upper_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - upper_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - upper_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
outerTop_upperTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []
for i in degree:  # 上タガ下部（内側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - upper_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - upper_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - upper_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - upper_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - upper_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - upper_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - upper_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - upper_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
innerBottom_upperTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []

for i in degree:  # 上タガ下部（外側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - upper_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - upper_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - upper_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - upper_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - upper_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - upper_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - upper_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - upper_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(upperTagaHeight - tagaWidth)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
outerBottom_upperTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []
for i in degree:  # 下タガ上部（内側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - lower_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - lower_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - lower_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - lower_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - lower_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - lower_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - lower_TagaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - lower_TagaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
innerTop_lowerTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []

for i in degree:  # 下タガ上部（外側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - lower_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - lower_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - lower_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - lower_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - lower_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - lower_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - lower_TagaTop_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - lower_TagaTop_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
outerTop_lowerTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []
for i in degree:  # 下タガ下部（内側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - lower_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - lower_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - lower_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - lower_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - lower_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - lower_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - lower_TagaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - lower_TagaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
innerBottom_lowerTaga_array = np.reshape(temp_a, (3, len(degree)))

x_array = []
y_array = []
z_array = []

for i in degree:  # 下タガ下部（外側）の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - lower_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - lower_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - lower_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - lower_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - lower_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - lower_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - lower_TagaBottom_offsetFromR + tagaThickness) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - lower_TagaBottom_offsetFromR + tagaThickness) * np.sin(np.radians(i)))
        z_array.append(lowerTagaHeight - tagaWidth)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
outerBottom_lowerTaga_array = np.reshape(temp_a, (3, len(degree)))

Taga_faces = []
Tmesh_1 = outerTop_upperTaga_array.T
Tmesh_2 = innerTop_upperTaga_array.T
Tmesh_3 = outerBottom_upperTaga_array.T
Tmesh_4 = innerBottom_upperTaga_array.T
Tmesh_5 = outerTop_lowerTaga_array.T
Tmesh_6 = innerTop_lowerTaga_array.T
Tmesh_7 = outerBottom_lowerTaga_array.T
Tmesh_8 = innerBottom_lowerTaga_array.T
vertices_T = np.vstack([Tmesh_1, Tmesh_2, Tmesh_3, Tmesh_4, Tmesh_5, Tmesh_6, Tmesh_7, Tmesh_8])

# タガ上側（上面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(i)
        Taga_faces.append(0)
        Taga_faces.append(deg_count)
        Taga_faces.append(deg_count + i)
    else:
        Taga_faces.append(4)
        Taga_faces.append(i)
        Taga_faces.append(i + 1)
        Taga_faces.append(deg_count + i + 1)
        Taga_faces.append(deg_count + i)
# タガ上側（下面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 2 + i)
        Taga_faces.append(deg_count * 3 + i)
        Taga_faces.append(deg_count * 3)
        Taga_faces.append(deg_count * 2)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 2 + i)
        Taga_faces.append(deg_count * 3 + i)
        Taga_faces.append(deg_count * 3 + i + 1)
        Taga_faces.append(deg_count * 2 + i + 1)
# タガ上側（外面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(i)
        Taga_faces.append(deg_count * 2 + i)
        Taga_faces.append(deg_count * 2)
        Taga_faces.append(0)
    else:
        Taga_faces.append(4)
        Taga_faces.append(i)
        Taga_faces.append(deg_count * 2 + i)
        Taga_faces.append(deg_count * 2 + i + 1)
        Taga_faces.append(i + 1)

# タガ上側（内面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count + i)
        Taga_faces.append(deg_count * 3 + i)
        Taga_faces.append(deg_count * 3)
        Taga_faces.append(deg_count)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count + i)
        Taga_faces.append(deg_count * 3 + i)
        Taga_faces.append(deg_count * 3 + i + 1)
        Taga_faces.append(deg_count + i + 1)

# タガ下側（上面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 4 + i)
        Taga_faces.append(deg_count * 4)
        Taga_faces.append(deg_count * 5)
        Taga_faces.append(deg_count * 5 + i)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 4 + i)
        Taga_faces.append(deg_count * 4 + i + 1)
        Taga_faces.append(deg_count * 5 + i + 1)
        Taga_faces.append(deg_count * 5 + i)
# タガ下側（下面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 6 + i)
        Taga_faces.append(deg_count * 7 + i)
        Taga_faces.append(deg_count * 7)
        Taga_faces.append(deg_count * 6)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 6 + i)
        Taga_faces.append(deg_count * 7 + i)
        Taga_faces.append(deg_count * 7 + i + 1)
        Taga_faces.append(deg_count * 6 + i + 1)
# タガ下側（外面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 4 + i)
        Taga_faces.append(deg_count * 6 + i)
        Taga_faces.append(deg_count * 6)
        Taga_faces.append(deg_count * 4)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 4 + i)
        Taga_faces.append(deg_count * 6 + i)
        Taga_faces.append(deg_count * 6 + i + 1)
        Taga_faces.append(deg_count * 4 + i + 1)

# タガ下側（内面）
for i in range(deg_count):
    if i + 1 == deg_count:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 5 + i)
        Taga_faces.append(deg_count * 7 + i)
        Taga_faces.append(deg_count * 7)
        Taga_faces.append(deg_count * 5)
    else:
        Taga_faces.append(4)
        Taga_faces.append(deg_count * 5 + i)
        Taga_faces.append(deg_count * 7 + i)
        Taga_faces.append(deg_count * 7 + i + 1)
        Taga_faces.append(deg_count * 5 + i + 1)

Taga_faces_temp = np.array(Taga_faces)
facesT = np.reshape(Taga_faces_temp, ((deg_count) * 8, 5))
surf3 = pv.PolyData(vertices_T, facesT)

plotter.add_mesh(surf, color="tan")
plotter.add_mesh(surf1, color="tan")
plotter.add_mesh(surf2, color="tan")
plotter.add_mesh(surf3, color="gray")

plotter.reset_camera()
plotter.show()
