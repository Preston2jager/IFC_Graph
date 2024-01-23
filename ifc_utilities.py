import ifcopenshell
import ifcopenshell.geom
#import ifcopenshell.util.shape
import multiprocessing

#Tree building
def Ifc_tree_building(ifc_file):
    print("Building IFC tree now")
    element_count=0
    tree = ifcopenshell.geom.tree()
    settings = ifcopenshell.geom.settings()
    iterator = ifcopenshell.geom.iterator(settings, ifc_file, multiprocessing.cpu_count())
    if iterator.initialize():
        while True:
            tree.add_element(iterator.get_native())
            element_count =+1
            print("Element count:" + element_count, end='\r')
            if not iterator.next():
                break
    print("IFC tree built")

#Display
    