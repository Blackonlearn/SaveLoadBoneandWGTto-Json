import bpy
import json
import pprint

activeArmature = bpy.context.object

#This simple code is mine, and it has already been pushed to github repo as my archive:https://github.com/Blackonlearn/SaveLoadBoneandWGTto-Json

#░░█ █▀ █▀█ █▄░█   █▀▄ ▄▀█ ▀█▀ ▄▀█
#█▄█ ▄█ █▄█ █░▀█   █▄▀ █▀█ ░█░ █▀█

fileName = 'asd.json'
file_path = 'C:/Users/'
file_pathFIX = rf"{file_path}"

filepathReplace = file_pathFIX.replace("/","\\")
jsonPath = filepathReplace+fileName
def WriteToJsonFile(jsonPath):
    bonelist = {}
    for bonelistindex, a in enumerate(bpy.context.selected_pose_bones):
        bonecustomshapedata = {}
        customShapeScale = []
        for index, value in enumerate(a.custom_shape_scale_xyz):
            customShapeScale.append(a.custom_shape_scale_xyz[index])
##            
        customShapeTranslation = []
        for index, value in enumerate(a.custom_shape_translation):
            customShapeTranslation.append(a.custom_shape_translation[index])
            
        customShapeRotation = []    
        for index, value in enumerate(a.custom_shape_rotation_euler):
            customShapeRotation.append(a.custom_shape_rotation_euler[index])
            
        bonecustomshapedata[f"BoneWidget"] = a.custom_shape.name
        bonecustomshapedata[f"customShapeScale"] = customShapeScale
        bonecustomshapedata[f"customShapeTranslation"] = customShapeTranslation
        bonecustomshapedata[f"customShapeRotation"] = customShapeRotation
        if a.custom_shape_transform == None:
            bonecustomshapedata[f"customShapeOverride"] = ""
        if not a.custom_shape_transform == None:
            bonecustomshapedata[f"customShapeOverride"] = a.custom_shape_transform.name
        bonecustomshapedata[f"ScaletoBoneLength"] = a.use_custom_shape_bone_size
        bonecustomshapedata[f"Wireframe"] = activeArmature.data.bones[f'{a.name}'].show_wire
        bonelist[a.name] = bonecustomshapedata 
        
    with open(jsonPath, "w") as ANIMeT_Json:
        json.dump(bonelist, ANIMeT_Json, indent = 4)
        print(ANIMeT_Json)
        
def AssignSavedCustomShape(jsonPath):
    with open(jsonPath, "r") as jsondata:
        LoadedData = json.load(jsondata)
        
    objectMode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode='POSE')
    for index, bone in enumerate(LoadedData):
        a = bpy.context.object.pose.bones[bone]
        a.custom_shape = bpy.data.objects[LoadedData[bone]["BoneWidget"]]
        for i, j in enumerate(LoadedData[bone]["customShapeScale"]):
            a.custom_shape_scale_xyz[i] = j
        for i, j in enumerate(LoadedData[bone]["customShapeTranslation"]):
            a.custom_shape_translation[i] = j
        for i, j in enumerate(LoadedData[bone]["customShapeRotation"]):
            a.custom_shape_rotation_euler[i] = j
        if LoadedData[bone]["customShapeOverride"] == "":
            a.custom_shape_transform = None
        elif not LoadedData[bone]["customShapeOverride"] == "":
            a.custom_shape_transform =  bpy.context.object.pose.bones[LoadedData[bone]["customShapeOverride"]]
        a.use_custom_shape_bone_size = LoadedData[bone]["ScaletoBoneLength"]
        activeArmature.data.bones[f'{a.name}'].show_wire = LoadedData[bone]["Wireframe"]
    return

AssignSavedCustomShape(jsonPath)
#WriteToJsonFile(jsonPath)
