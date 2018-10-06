''' 08-renameFunction.py

Example of how to create a function and call it from the script editor
'''
from maya import cmds

map_type_to_suffix = {
    "mesh": "geo",
    "joint": "jnt",
    "camera": None,
    "ambientLight": "lgt"
}

DEFAULT_SUFFIX = "grp"

def rename_object(selection=False):
    """ 
    Function to rename objects according to their suffix
    """
    list_of_selected = cmds.ls(selection=selection, dag=True, long=True)

    # if len(list_of_selected) == 0:
        # print "These are all the dag objects"
        # list_of_selected = cmds.ls(dag=True, long=True)
    if selection and not list_of_selected:
        raise RuntimeError("You need to select something")
        
    list_of_selected.sort(key=len, reverse=True)   

    for obj in list_of_selected:
        short_name = obj.split('|')[-1]
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []
        # print("Children: ", children, len(children))
        
        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)
            
        # Renaming using suffixes
        # if objType == "mesh":
            # suffix = "geo"
        # elif objType == "joint":
            # suffix = "jnt"
        # elif objType == "camera":
            # print "Do not rename cameras"
            # continue
        # else:
            # suffix = "grp"
        
        suffix = map_type_to_suffix.get(objType, DEFAULT_SUFFIX)
        
        if not suffix:
            continue
            
        # Avoid renaming objects with suffix
        if obj.endswith("_" + suffix):
            continue
            
        new_name = "%s_%s" % (short_name, suffix)
        print new_name      
        
        cmds.rename(obj, new_name) 
        