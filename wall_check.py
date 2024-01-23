import ifcopenshell
import ifcopenshell.geom
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib

ifc_file = ifcopenshell.open('./sample.ifc')
walls = ifc_file.by_type('IfcWall')

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)

wall_shapes = []
for wall in walls:
    shape = ifcopenshell.geom.create_shape(settings, wall)
    bbox = Bnd_Box()
    brepbndlib.Add(shape.geometry, bbox)
    wall_shapes.append((shape, bbox))
    x_min, y_min, z_min, x_max, y_max, z_max = bbox.Get()
    length = x_max - x_min
    height = z_max - z_min

# 检查墙之间的交接
for i in range(len(wall_shapes)):
    for j in range(i + 1, len(wall_shapes)):
        if wall_shapes[i][1].IsOut(wall_shapes[j][1]):
            continue  # 边界框不相交，墙也不会相交
        # 这里可以进行更详细的几何相交测试
        print(f"Wall {i} intersects with Wall {j}")
