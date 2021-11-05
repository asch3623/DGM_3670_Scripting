import maya.cmds as cmds

def renameSequence(objName, numberPadding, nodeType):
    sels = cmds.ls(selection = True)

    #for i in range(len(sels)):
        #cmds.rename(sels[i], objName + i + 1 + nodeType)

    for count, object in enumerate(sels):
        cmds.rename(object, objName + str(count + 1).zfill(numberPadding) + nodeType)

renameSequence("Leg_", 3, "_Jnt")