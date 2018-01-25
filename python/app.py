'''
app
===

Demos basic usage of the Onshape API
'''
import pprint as pp
import os
import json


from apikey.client import Client



DOCUMENT_ID = 'ENTER_DOCUMENT_ID_HERE'
WORKSPACE_ID = 'ENTER_WORKSPACE_ID_HERE'
COLOR_SORTING_METHOD = 'boundingBoxVolume' # You can replace this with maxPlanarArea if you'd like.


def read_color_palette(color_palette='color_palette.json'):

    if not os.path.isfile(color_palette):
        raise IOError('{} is not a file'.format(color_palette))

    with open(color_palette) as f:
        try:
            details = json.load(f)


            if "default_rotation" not in details:
                raise ValueError('Default rotation not in file')

            default_rotation = details.get("default_rotation")

            ordered_colors = list()

            for color in default_rotation:
                ordered_colors.append(details.get(color))

            pp.pprint(ordered_colors)

            return ordered_colors

        except TypeError:
            raise ValueError('%s is not valid json' % color_palette)

def get_volume_of_bounding_box(bounding_box_map):

    xLen = bounding_box_map.get('highX', 0.0) - bounding_box_map.get('lowX', 0.0)
    yLen = bounding_box_map.get('highY', 0.0) - bounding_box_map.get('lowY', 0.0)
    zLen = bounding_box_map.get('highZ', 0.0) - bounding_box_map.get('lowZ', 0.0)

    volume = xLen * yLen * zLen

    return volume

def get_max_planar_area(bounding_box_map):

    xLen = bounding_box_map.get('highX', 0.0) - bounding_box_map.get('lowX', 0.0)
    yLen = bounding_box_map.get('highY', 0.0) - bounding_box_map.get('lowY', 0.0)
    zLen = bounding_box_map.get('highZ', 0.0) - bounding_box_map.get('lowZ', 0.0)

    max_planar_surface_area = max(xLen*yLen, xLen*zLen, yLen*zLen)

    return max_planar_surface_area


# stacks to choose from
stacks = {
    'cad': 'https://cad.onshape.com'
}

# create instance of the onshape client; change key to test on another stack
c = Client(stack=stacks['cad'], creds='/Users/noaflaherty/Documents/Development/Repos/apikey/python/creds.json', logging=True)


# get the document details
parts = c.list_parts(DOCUMENT_ID, WORKSPACE_ID)

ordered_colors = read_color_palette('/Users/noaflaherty/Documents/Development/Repos/apikey/python/color_palette.json')


part_dict = dict()

for part in parts:
    element_id = part.get('elementId')
    part_id = part.get('partId')

    bounding_box_map = c.get_part_bounding_box(DOCUMENT_ID, WORKSPACE_ID, element_id, part_id)
    bounding_box_volume = get_volume_of_bounding_box(bounding_box_map)
    max_planar_area = get_max_planar_area(bounding_box_map)

    part_dict[part_id] = {
        'elementId' : element_id,
        'boundingBoxVolume' : bounding_box_volume,
        'maxPlanarArea' : max_planar_area
    }


ordered_part_list = sorted(part_dict, key=part_dict.get(COLOR_SORTING_METHOD), reverse=True)


part_index = 0

for part_id in ordered_part_list:

    color_index = part_index % len(ordered_colors)
    appearance = ordered_colors[color_index]

    c.update_part_color(DOCUMENT_ID, WORKSPACE_ID, part_dict[part_id].get('elementId'), part_id, appearance)

    part_index += 1
    
    

