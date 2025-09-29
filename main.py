import ifcopenshell

from external.BIManalyst_g_29.rules import Dimensions

model = ifcopenshell.open("models/25-16-D-STR.ifc")

BeamClassifications = Dimensions.beam_dimensions(model)

print("Beam result:", BeamClassifications)


