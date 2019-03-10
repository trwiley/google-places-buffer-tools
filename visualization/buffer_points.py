# buffer_points.py
# purpose: to create a buffer based on an input feature, an output feature, and a distance.

import arcpy

def set_workspace(workspace):
    arcpy.env.workspace = workspace

def menu():
    print('Enter workspace')
    workspace = input()
    set_workspace(workspace)
    print('Enter the name of your input feature: ')
    input_feature = input()
    print('Enter the name of your output feature: ')
    out_feature = input()
    print('Enter the buffer distance: ')
    distance = input()
    make_buffer(input_feature, out_feature, distance)

def make_buffer(input_feature, out_feature, distance):
    dissolve = 'ALL'
    print('Creating the buffer...')
    arcpy.Buffer_analysis(
        in_features=input_feature, 
        out_feature_class=out_feature, 
        buffer_distance_or_field=distance, 
        dissolve_option=dissolve)
    print('Done.')
