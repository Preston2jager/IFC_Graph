import ifcopenshell
import ifcopenshell.geom
import re

from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib

def string_to_int(s):
    return int(''.join(str(ord(c)) for c in s))

def get_wall_position(wall):
    # 获取墙体的位置信息
    placement = wall.ObjectPlacement
    # 检查是否存在相对放置
    while placement and not isinstance(placement.RelativePlacement, ifcopenshell.entity_instance):
        placement = placement.PlacementRelTo
    if placement and isinstance(placement.RelativePlacement, ifcopenshell.entity_instance):
        location = placement.RelativePlacement.Location

        return [str(location.Coordinates[0]), str(location.Coordinates[1]), str(location.Coordinates[2])]
    else:
        return None

ifc_file = ifcopenshell.open('./sample.ifc')
walls = ifc_file.by_type('IfcWall')
windows = ifc_file.by_type('IfcWindow')
doors = ifc_file.by_type('IfcDoor')

link_file =  'ifc.link'
entity_file =  'ifc.wall'

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)

############################################################

wall_ids = []
wall_sizes = []
wall_shapes = []
wall_positions = []
window_ids = []
window_sizes = []
window_shapes = []
window_positions = []
door_ids = []
door_sizes = []
door_shapes = []
door_positions = []
    
for wall in walls:
    shape = ifcopenshell.geom.create_shape(settings, wall)
    bbox = Bnd_Box()
    brepbndlib.Add(shape.geometry, bbox)
    wall_shapes.append((shape, bbox))
    x_min, y_min, z_min, x_max, y_max, z_max = bbox.Get()
    length = x_max - x_min
    height = z_max - z_min
    width = y_max - y_min
    wall_sizes.append([str(length), str(height), str(width)])
    wall_id = str(wall.id())
    wall_ids.append(wall_id)
    position = get_wall_position(wall)
    wall_positions.append(position)

for window in windows:
    shape = ifcopenshell.geom.create_shape(settings, window)
    bbox = Bnd_Box()
    brepbndlib.Add(shape.geometry, bbox)
    window_shapes.append((shape, bbox))
    x_min, y_min, z_min, x_max, y_max, z_max = bbox.Get()
    length = x_max - x_min
    height = z_max - z_min
    width = y_max - y_min
    window_sizes.append([str(length), str(height), str(width)])
    window_id = str(window.id())
    window_ids.append(wall_id)
    position = get_wall_position(window)
    window_positions.append(position)

for door in doors:
    shape = ifcopenshell.geom.create_shape(settings, door)
    bbox = Bnd_Box()
    brepbndlib.Add(shape.geometry, bbox)
    door_shapes.append((shape, bbox))
    x_min, y_min, z_min, x_max, y_max, z_max = bbox.Get()
    length = x_max - x_min
    height = z_max - z_min
    width = y_max - y_min
    door_sizes.append([str(length), str(height), str(width)])
    door_id = str(door.id())
    door_ids.append(door_id)
    position = get_wall_position(wall)
    door_positions.append(position)

with open(entity_file, 'w') as file:
    for i in range(len(wall_ids)):
        file.write(wall_ids[i] + '\t' + wall_positions[i][0] + '\t' + wall_positions[i][1] + '\t' + wall_positions[i][2] + '\t' + wall_sizes[i][0] + '\t' + wall_sizes[i][1] + '\t' + wall_sizes[i][2] + '\n')
    for i in range(len(window_ids)):
        file.write(window_ids[i] + '\t' + window_positions[i][0] + '\t' + window_positions[i][1] + '\t' + window_positions[i][2] + '\t' + window_sizes[i][0] + '\t' + window_sizes[i][1] + '\t' + window_sizes[i][2] + '\n')
    for i in range(len(door_ids)):
        file.write(door_ids[i] + '\t' + door_positions[i][0] + '\t' + door_positions[i][1] + '\t' + door_positions[i][2] + '\t' + door_sizes[i][0] + '\t' + door_sizes[i][1] + '\t' + door_sizes[i][2] + '\n')


###############################################################################
#Window door and wall relation
with open(link_file, 'w') as file:
    for i in range(len(wall_shapes)):
        for j in range(i + 1, len(wall_shapes)):
            if wall_shapes[i][1].IsOut(wall_shapes[j][1]):
                continue  
            file.write(wall_ids[i] + '\t' + wall_ids[j] + '\n')
    
fills_elements = ifc_file.by_type('IfcRelFillsElement')

openings = {}
for fills_element in fills_elements:
    opening = fills_element.RelatingOpeningElement
    element = fills_element.RelatedBuildingElement
    openings[element.id()] = opening

voids_elements = ifc_file.by_type('IfcRelVoidsElement')
pattern = r'#(\d+)='

with open(link_file, 'a') as file:
    for voids_element in voids_elements:
        opening = voids_element.RelatedOpeningElement
        wall = voids_element.RelatingBuildingElement
        for element_id, opening_element in openings.items():
            if opening_element.id() == opening.id():
                file.write(str(re.search(pattern, str(wall)).group(1)) + '\t' + str(element_id) + '\n')
##################################################################################

print("Done")

