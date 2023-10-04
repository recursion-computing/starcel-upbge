import bge
from bge import logic, events
import bpy

def mouse2world():
    cam = logic.getCurrentScene().active_camera
    vec = cam.getScreenVect(*logic.mouse.position)
    camPos = cam.worldPosition
    projectedPos = [0,0,0]
    z = 10      # user-set depth
    projectedPos[0] = camPos[0] - vec[0] * z
    projectedPos[1] = camPos[1] - vec[1] * z
    projectedPos[2] = camPos[2] - vec[2] * z

    return projectedPos

def main():
    scene = logic.getCurrentScene()
    cont = logic.getCurrentController()
    own = cont.owner

    # 'Keyboard' is a keyboard sensor
    sensor = cont.sensors["keyboard"]
    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_click"]
    
    # https://blenderartists.org/t/mouse-over-dont-work-on-text-object/1150815/7
    if mouse_over.positive:
        crosshair = scene.objects["cross_hair"]
        crosshair.worldPosition = mouse2world()
        object, hitpoint, normal = crosshair.rayCast(mouse_over.rayTarget, mouse_over.raySource, 0.0, "isTrackerFloor", 0, 1, 0)
        print(object)
        print(hitpoint)

    for key in sensor.inputs:
        print(key)
        characterValue = bge.events.EventToCharacter(key, True)
        print(characterValue)
        own["userInput"] += characterValue
        
    #for i in own:
    #print(dir(own))
    own["Text"] = own["userInput"]
    if own["userInput"] == "HHII":
        own["Text"] = eval("3*3")
    
#    font_curve = bpy.data.curves.new(type="FONT", name="Font curve")
#    font_curve.body = "testing"
#    font_obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)#bpy.context.scene.collection.objects.link(font_obj)
#    bpy.context.view_layer.objects.active = bpy.data.objects['Font Object'] # Need a reference to an `object`, not `TextCurve`, for this to work
#    bpy.context.object.select_set(True)
#    bpy.ops.object.convert(target='MESH')
    #bpy.context.scene.objects.active = scene.objects["Text"]
    #scene.objects["Text"].select = True
    #bpy.ops.object.convert(target="MESH")
    
#    cont = bge.logic.getCurrentController()
#    own = cont.owner

#    keyboard = bge.logic.keyboard
#    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
#    keyEvents = logic.keyboard.inputs
#    hitKey = [k for k in keyEvents if keyEvents[k] == logic.KX_INPUT_JUST_ACTIVATED]
#    print(hitKey)
    
    #input = own["userInput"]
    
    #if hitKey != []:
        #print(hitKey)
        #characterValue = bge.events.EventToCharacter(hitkey[0], True)
        #print(characterValue)
        #own["userInput"] += characterValue
        
    # own.text = own["userInput"]
main()


