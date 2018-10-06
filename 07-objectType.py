from maya import cmds

list_of_selected = cmds.ls(selection=True)

if len(list_of_selected) == 0:
    print "These are all the dag objects"
    list_of_selected = cmds.ls(dag=True, long=True)
    
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
    if objType == "mesh":
        suffix = "geo"
    elif objType == "joint":
        suffix = "jnt"
    elif objType == "camera":
        print "Do not rename cameras"
        continue
    else:
        suffix = "grp"
        
    new_name = short_name + "_" + suffix
    print new_name      
    
    cmds.rename(obj, new_name) 
        