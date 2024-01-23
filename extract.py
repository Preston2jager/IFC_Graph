import ifcopenshell
import ifcopenshell.geom
import math



#walls = ifc_file.by_type('IfcWall')
#for wall in walls:
#    print(wall)

def get_wall_position(wall):
    # 获取墙体的位置信息
    placement = wall.ObjectPlacement
    # 检查是否存在相对放置
    while placement and not isinstance(placement.RelativePlacement, ifcopenshell.entity_instance):
        placement = placement.PlacementRelTo

    if placement and isinstance(placement.RelativePlacement, ifcopenshell.entity_instance):
        location = placement.RelativePlacement.Location
        return (location.Coordinates[0], location.Coordinates[1], location.Coordinates[2])
    else:
        return None

ifc_file = ifcopenshell.open('./sample.ifc')
walls = ifc_file.by_type('IfcWall')

for wall in walls:
    position = get_wall_position(wall)
    if position:
        print(f"Wall ID: {wall.GlobalId}, Position: {position}")
    else:
        print(f"Wall ID: {wall.GlobalId} has no position information")