import bpy
import json
import pprint

activeArmature = bpy.context.object


#░░█ █▀ █▀█ █▄░█   █▀▄ ▄▀█ ▀█▀ ▄▀█
#█▄█ ▄█ █▄█ █░▀█   █▄▀ █▀█ ░█░ █▀█

fileName = 'asd.json'
file_path = 'C:/'
file_pathFIX = rf"{file_path}"

filepathReplace = file_pathFIX.replace("/","\\")
jsonPath = filepathReplace+fileName
def WriteToJsonFile(jsonPath):
    bonelist = {}
    for bonelistindex, a in enumerate(bpy.context.selected_pose_bones):
        bonelist.update({a.name: a.custom_shape.name})
        
    with open(jsonPath, "w") as ANIMeT_Json:
        json.dump(bonelist, ANIMeT_Json, indent = 4)
        print(ANIMeT_Json)
        
def AssignSavedCustomShape(jsonPath):
    with open(jsonPath, "r") as jsondata:
        LoadedData = json.load(jsondata)
        
    objectMode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode='POSE')
    for index, bone in enumerate(LoadedData):
        bpy.context.object.pose.bones[bone].custom_shape = bpy.data.objects[LoadedData[bone]]
    return



AssignSavedCustomShape(jsonPath)
WriteToJsonFile(jsonPath)
