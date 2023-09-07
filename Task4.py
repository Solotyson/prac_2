import arcpy

arcpy.env.workspace = r"D:\Sem 3\Prog_3\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
input_layer = "Wilson_Zoning"
output_layer = "Wilson_Zoning_Feature_To_Points"

arcpy.management.FeatureToPoint(input_layer, output_layer, "CENTROID")
print("process completed")
