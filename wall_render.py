import ifcopenshell
import ifcopenshell.geom

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeShape
from OCC.Core.BRep import BRep_Tool

display, start_display, add_menu, add_function_to_menu = init_display()

ifc_file = ifcopenshell.open('./sample.ifc')

walls = ifc_file.by_type('IfcWall')

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)

# 创建形状
for wall in walls:
    shape = ifcopenshell.geom.create_shape(settings, wall)
    display.DisplayShape(shape.geometry, update=False)

display.FitAll()

# 开始图形界面循环
start_display()
