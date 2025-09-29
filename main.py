import ifcopenshell

from external.BIManalyst_g_29.rules import BeamClassifications
from external.BIManalyst_g_29.rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = BeamClassifications.checkRule(model)

doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
