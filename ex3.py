import pyvista as pv

grid = pv.ImageData(dimensions=(10, 10, 10), spacing=(2, 1, 5), origin=( 0, 0, 0),)
ugrid = grid.cast_to_unstructured_grid()

pl = pv.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
label_coords = ugrid.points + [0, 0, 0.02]
point_labels = [f'Point {i}' for i in range(ugrid.n_points)]
pl.add_point_labels(
    label_coords, point_labels, font_size=10, point_size=5
)
cell_labels = [f'Cell {i}' for i in range(ugrid.n_cells)]
pl.add_point_labels(ugrid.cell_centers(), cell_labels, font_size=10)
pl.camera_position = 'xy'
pl.show()
