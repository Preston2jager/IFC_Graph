import os
import ifcopenshell
import ifcopenshell.geom

current_directory = os.getcwd()
page_split = "==================================================================="
file_path = './sample3.ifc'

print(page_split)
print("Start loading ifc file:" + current_directory + file_path)
ifc_file = ifcopenshell.open(file_path)
print("Loading successful")
stories = ifc_file.by_type('IfcBuildingStorey')
total_stories  = len(stories)
print("Accquired " + str(total_stories) + " stories.")
print(page_split)


for story in stories:
    relation_info = ifc_file.get_inverse(story)
    story_name = story.Name
    print('For: ' + str(story_name))
    for entry in relation_info:
        if entry.is_a('IfcRelContainedInSpatialStructure'):
            building_elements = entry.RelatedElements
            for building_element in building_elements:
                representation = building_element.Representation
                if representation is not None:
                    print(representation[2])
                else:
                    print("This representations is None")
    print(page_split)

#for door in doors:
    # 获取与门相关联的所有关系实体
    #rels = ifc_file.get_inverse(door)
    #print(rels)
    # 筛选 IfcRelSpaceBoundary 实体 
    #space_boundaries = [rel for rel in rels if rel.is_a('IfcRelSpaceBoundary')]

    # 处理每个 IfcRelSpaceBoundary 实体
    #for sb in space_boundaries:
        # 这里可以获取关联的空间实体等信息
        # 例如: sb.RelatingSpace 或 sb.RelatedBuildingElement
        #print(sb)


