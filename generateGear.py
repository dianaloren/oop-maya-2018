""" Funcion: generateGear. Permite crear y modificar una tuerca

Uso en Maya:

import sys

sys.path.append("D:\Diana\Python\Workshop-Maya-Python-Santiago")
import generateGear
reload(generateGear)

#transform, constructor, extrude = generateGear.generar_tuerca(10)
generateGear.modificar_tuerca(constructor, extrude, 40, 0.1)
    
    
"""
from maya import cmds

def generar_tuerca(teeth=10, length=0.3):
    """Funcion que crea una tuerca con los parametros dados
    Args:
        teeth: El numero de dientes de la tuerca
        length: Tamano de cada tuerca
    
    Returns:
        Una tupla con la transformada, el constructor y el nodo que hace la extruccion
    """
    # Teeth (dientes) son cada una de las caras que es extruida
    spans = teeth * 2
    
    transform, constructor = cmds.polyPipe(subdivisionsAxis=spans)
    
    #select -r pPipe1.f[40] pPipe1.f[42] pPipe1.f[44] pPipe1.f[46] pPipe1.f[48] pPipe1.f[50] pPipe1.f[52] pPipe1.f[54] pPipe1.f[56] pPipe1.f[58] ;
    sideFaces = range(spans*2, spans*3, 2)
    
    print(transform, constructor, sideFaces)
    
    cmds.select(clear=True)
    
    for face in sideFaces:
        cmds.select("%s.f[%s]" % (transform, face), add=True)
        
    #polyExtrudeFacet -constructionHistory 1 -keepFacesTogether 1 -pvx -1.192092896e-07 -pvy 0 -pvz 1.788139343e-07 -divisions 1 -twist 0 -taper 1 -off 0 -thickness 0 -smoothingAngle 30 pPipe2.f[40] pPipe2.f[42] pPipe2.f[44] pPipe2.f[46] pPipe2.f[48] pPipe2.f[50] pPipe2.f[52] pPipe2.f[54] pPipe2.f[56] pPipe2.f[58];
    #setAttr "polyExtrudeFace2.localTranslate" -type double3 0 0 0.143625 ;
    extruded_faces = cmds.polyExtrudeFacet(localTranslateZ=length)
    return transform, constructor, extruded_faces
    

def modificar_tuerca(constructor, extruded_faces, teeth=10, length=0.3):
    spans = teeth * 2
    
    cmds.polyPipe(constructor, edit=True, subdivisionsAxis=spans)
    
    side_faces = range(spans*2, spans*3, 2)
    face_names = []
    
    for face in side_faces:
        face_name = 'f[%s]' % (face)
        face_names.append(face_name)
        
    print extruded_faces
    # Cambia el numero de dientes
    cmds.setAttr('%s.inputComponents' % extruded_faces[0], 
                 len(face_names),
                 *face_names,
                 type="componentList")
                 
    # Cambiar la longitud de los dientes
    cmds.polyExtrudeFacet(extruded_faces, edit=True, ltz=length)
     