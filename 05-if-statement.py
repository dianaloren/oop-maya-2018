'''Use scene: python_directives.mb
'''

from maya import cmds

#cmds.select('joint4')
list_of_selected = cmds.ls(selection=True)

if len(list_of_selected) == 0:
    print "No hay objetos seleccionados. Muestra todos los objetos en el Outliner:"
    list_of_selected = cmds.ls(dag=True, long=True)
    
list_of_selected.sort(key=len, reverse=True)
print list_of_selected