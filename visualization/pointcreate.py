# pointcreate.py
# purpose: to create a new point feature class based on longitudes and latitudes provided in a CSV file

import arcpy

def set_workspace(workspace):
    arcpy.env.workspace = workspace

def make_table(input_table, featureclass, xcoord, ycoord):
    print('Creating table...')
    arcpy.management.XYTableToPoint(input_table, featureclass, xcoord, ycoord)
    print('Done.')

def menu():
    print('Enter workspace')
    workspace = input()
    set_workspace(workspace)
    print('Enter the file path of your input table: ')
    input_table = input()
    print('What do you want to name your feature class?')
    fc = input()
    print('In your input table, which column is your X?')
    x = input()
    print('In your input table, which column is your Y?')
    y = input()
    make_table(input_table, fc, x, y)

menu()