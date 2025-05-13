
import numpy as np
import pyvista as pv  # Delete for non-Pro version
# from pyvistaqt import BackgroundPlotter  # Delete for non-Pro version

plotter = pv.Plotter()
# plotter = BackgroundPlotter()
plotter.enable_parallel_projection()


deg_1 = 261.37307344132137
deg_2 = 278.62692655867863
deg_3 = 441.37307344132137
deg_4 = 458.62692655867863
deg_5 = 621.3730734413214
deg_array = np.array([deg_1, deg_2, deg_3, deg_4, deg_5])
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
sokoitaTop_offsetFromR = 7.5
sokoitaBottom_offsetFromR = 7.75
upperTagaHeight = 42.67
lowerTagaHeight = 10.0
tagaWidth = 5.0
tagaThickness = 1.0

startDeg = deg_array[0]
endDeg = deg_array[len(deg_array) - 1]
degree = np.arange(startDeg, endDeg, deg_step, dtype=float).tolist()

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

# 底板縁-上側
x_array = []
y_array = []
z_array = []
for i in degree:  # 底板の頂点座標を計算する
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - sokoitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - sokoitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - sokoitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - sokoitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - sokoitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - sokoitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - sokoitaTop_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - sokoitaTop_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
sokoita_Top_array = np.reshape(temp_a, (3, len(degree)))

# 底板縁-下側
x_array = []
y_array = []
z_array = []
for i in degree:
    # print("θ = ",i)
    if deg_1 <= i < deg_2:
        x_array.append(X_12 + (R_12 - sokoitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_12 + (R_12 - sokoitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_2 <= i < deg_3:
        x_array.append(x_2 + (r_2 - sokoitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_2 + (r_2 - sokoitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_3 <= i < deg_4:
        x_array.append(X_21 + (R_21 - sokoitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(Y_21 + (R_21 - sokoitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)
    if deg_4 <= i <= deg_5:
        x_array.append(x_1 + (r_1 - sokoitaBottom_offsetFromR) * np.cos(np.radians(i)))
        y_array.append(y_1 + (r_1 - sokoitaBottom_offsetFromR) * np.sin(np.radians(i)))
        z_array.append(sokoitaHeight - sokoitaThickness)

new_array = x_array + y_array + z_array
temp_a = np.array(new_array)
sokoita_Bottom_array = np.reshape(temp_a, (3, len(degree)))

deg_count = len(degree)
faces_array = []

# 側板（外面）
for i in range(deg_count):
    if i == deg_count - 1:
        faces_array.append(4)
        faces_array.append(4 * i)
        faces_array.append(4 * i + 1)
        faces_array.append(1)
        faces_array.append(0)
    else:
        faces_array.append(4)
        faces_array.append(4 * i)
        faces_array.append(4 * i + 1)
        faces_array.append(4 * (i + 1) + 1)
        faces_array.append(4 * (i + 1))

# 側板（内面-上から底板上面まで）
for i in range(deg_count):
    if i == deg_count - 1:
        faces_array.append(4)
        faces_array.append(4 * i + 3)
        faces_array.append(3)
        faces_array.append(2)
        faces_array.append(4 * i + 2)
    else:
        faces_array.append(4)
        faces_array.append(4 * i + 3)
        faces_array.append(4 * (i + 1) + 3)
        faces_array.append(4 * (i + 1) + 2)
        faces_array.append(4 * i + 2)

# 側板（上小口面）
for i in range(deg_count):
    if i == deg_count - 1:
        faces_array.append(4)
        faces_array.append(4 * i)
        faces_array.append(0)
        faces_array.append(3)
        faces_array.append(4 * i + 3)
    else:
        faces_array.append(4)
        faces_array.append(4 * i)
        faces_array.append(4 * (i + 1))
        faces_array.append(4 * ( i + 1) + 3)
        faces_array.append(4 * i + 3)

# 側板（下小口面）
for i in range(deg_count):
    if i == deg_count - 1:
        faces_array.append(4)
        faces_array.append(4 * i + 1)
        faces_array.append(4 * i + 2)
        faces_array.append(2)
        faces_array.append(1)
    else:
        faces_array.append(4)
        faces_array.append(4 * i + 1)
        faces_array.append(4 * i + 2)
        faces_array.append(4 * ( i + 1) + 2)
        faces_array.append(4 * ( i + 1) + 1)

mesh_1 = gawaita_array.T
mesh_2 = sokoita_Top_array.T
mesh_3 = sokoita_Bottom_array.T
vertices = np.vstack([mesh_1, mesh_2, mesh_3])
faces_temp = np.array(faces_array)
faces = np.reshape(faces_temp, ((deg_count) * 4, 5))
surf = pv.PolyData(vertices, faces)
# surf = pv.PolyData(vertices,)

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

plotter.add_mesh(surf, color="tan", show_edges=False)
plotter.add_mesh(surf1, color="tan", show_edges=False)
plotter.add_mesh(surf2, color="tan", show_edges=False)
# plotter.add_mesh(surf3, color="gray")

plotter.reset_camera()
plotter.show()
surfAll = surf + surf1 + surf2
surfAll.save('小判型桶.stl')
