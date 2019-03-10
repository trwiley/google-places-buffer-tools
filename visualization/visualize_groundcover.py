# visualize_groundcover.py
# purpose: to visualize the extent that buffers created in a previous step covers of a polygon.

import arcpy

def menu():
    print("Enter the feature class you want to erase.")
    erase_input = input() #clippin the map
    erase_ref = input() # the result of the previous analysis is being used to clip the basemap. 
    erase_out = input()
    erase(erase_input, erase_ref, erase_out)

def erase(erase_input, erase_ref, erase_out):
    print('Erasing...')
    arcpy.Erase_analysis(erase_input, erase_ref, erase_out)
    print('Done.')