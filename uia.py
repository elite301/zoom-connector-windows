
def filterControl(control, name, controlType):
  for ctrl in control.GetChildren():
    if ctrl.Name == name and ctrl.ControlTypeName == controlType:
      return ctrl
  return None

def clickControl(control, name, controlType):
  ctrl = filterControl(control, name, controlType)
  
  if ctrl:
    print("Clicked the '", name, "' button.")
    ctrl.Click(simulateMove = False, waitTime = 2)
  else:
    print("Can't find the '", name, "' button.")