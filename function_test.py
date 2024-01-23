import os
import multiprocessing
import ifcopenshell
import ifcopenshell.geom
#import ifcopenshell.util.shape

from utilities import draw_split_line, clear_screen
from ifc_utilities import Ifc_tree_building

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeShape
from OCC.Core.BRep import BRep_Tool

current_directory = os.getcwd()
file_path = './sample7.ifc'

#Loading file
clear_screen()
draw_split_line()
print("Start loading ifc file:" + current_directory + file_path)
ifc_file = ifcopenshell.open(file_path)
print("Loading successful")
draw_split_line()
#End of loading

spaces = ifc_file.by_type('IfcSpace')

def get_space_bounds(space):
    representation = space.Representation.Representations[0]  # Adjust as needed
    # You would write the logic here to extract the bounding box from the representation
    # For the sake of this example, let's assume a simple rectangular space
    return (0, 0, 0), (1000, 1000, 3000) 



#display, start_display, add_menu, add_function_to_menu = init_display()

#settings = ifcopenshell.geom.settings()
#settings.set(settings.USE_PYTHON_OPENCASCADE, True)

#for space in spaces:
    #shape = ifcopenshell.geom.create_shape(settings, space)
    #display.DisplayShape(shape.geometry, update=False)


#display.FitAll()

# 开始图形界面循环
#start_display()

IFC_tree = Ifc_tree_building(ifc_file)
draw_split_line()



for space in spaces:
    elements = IFC_tree.select(space)
    for element in elements:
        #if element.is_a('IfcWall'):
        print(element)
        
        





