import ifcopenshell
import ifcopenshell.geom
import re
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib

model = ifcopenshell.open('./sample.ifc')

fills_elements = model.by_type('IfcRelFillsElement')

openings = {}
for fills_element in fills_elements:
    opening = fills_element.RelatingOpeningElement
    element = fills_element.RelatedBuildingElement
    openings[element.id()] = opening

voids_elements = model.by_type('IfcRelVoidsElement')
pattern = r'#(\d+)='

for voids_element in voids_elements:
    opening = voids_element.RelatedOpeningElement
    wall = voids_element.RelatingBuildingElement
    #match = re.search(pattern, str(wall))
    extracted_number = re.search(pattern, str(wall)).group(1)
    print(extracted_number)
    for element_id, opening_element in openings.items():
        if opening_element.id() == opening.id():
            print(f'Element ID {element_id} is in wall {wall}')

