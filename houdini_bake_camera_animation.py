import hou

selectedNode = hou.selectedNodes()[0]

bakingNode = hou.node('/obj').createNode('cam', selectedNode.name() + '_bake')


hou.setFrame(int(hou.playbar.playbackRange()[0]))

for f in range(int(hou.playbar.playbackRange()[0]), int(hou.playbar.playbackRange()[1])+1):
    hou.setFrame(f)
    
    bakingNode.setWorldTransform(selectedNode.worldTransform())
    bakingNode.parm("tx").setKeyframe(hou.Keyframe(bakingNode.parm("tx").eval()))
    bakingNode.parm("ty").setKeyframe(hou.Keyframe(bakingNode.parm("ty").eval()))
    bakingNode.parm("tz").setKeyframe(hou.Keyframe(bakingNode.parm("tz").eval()))
    bakingNode.parm("rx").setKeyframe(hou.Keyframe(bakingNode.parm("rx").eval()))
    bakingNode.parm("ry").setKeyframe(hou.Keyframe(bakingNode.parm("ry").eval()))
    bakingNode.parm("rz").setKeyframe(hou.Keyframe(bakingNode.parm("rz").eval()))
    
    
    bakingNode.parm('focal').setKeyframe(hou.Keyframe(selectedNode.parm('focal').eval()))
    bakingNode.parm('aperture').setKeyframe(hou.Keyframe(selectedNode.parm('aperture').eval()))
    bakingNode.parm('near').setKeyframe(hou.Keyframe(selectedNode.parm('near').eval()))
    bakingNode.parm('far').setKeyframe(hou.Keyframe(selectedNode.parm('far').eval()))
    bakingNode.parm('resx').setKeyframe(hou.Keyframe(selectedNode.parm('resx').eval()))
    bakingNode.parm('resy').setKeyframe(hou.Keyframe(selectedNode.parm('resy').eval()))
    bakingNode.parm('winsizex').setKeyframe(hou.Keyframe(selectedNode.parm('winsizex').eval()))
    bakingNode.parm('winsizey').setKeyframe(hou.Keyframe(selectedNode.parm('winsizey').eval()))
    bakingNode.parm('shutter').setKeyframe(hou.Keyframe(selectedNode.parm('shutter').eval()))
    bakingNode.parm('aspect').setKeyframe(hou.Keyframe(selectedNode.parm('aspect').eval()))
