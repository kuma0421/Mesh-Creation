import pyvista as pv


pv.CylinderStructured(
        center=(0.0, 0.0, 0.0), 
        direction=(1.0, 0.0, 0.0), 
        radius=[2, 2.5], 
        height=3.0
    ).plot(show_edges=True)
