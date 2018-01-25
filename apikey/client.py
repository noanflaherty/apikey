'''
client
======

Functions needed for updating part colors in an Onshape document
'''

from onshape import Onshape

import mimetypes
import random
import string
import os
import pprint as pp


class Client():


    def __init__(self, stack='https://cad.onshape.com', creds='./creds.json', logging=True):
        '''
        Instantiates a new Onshape client.

        Args:
            - stack (str, default='https://cad.onshape.com'): Base URL
            - logging (bool, default=True): Turn logging on or off
        '''
        print creds
        self._stack = stack
        self._api = Onshape(stack=stack, creds=creds, logging=logging)


    def list_parts(self, did, wid):

        return self._api.request('get', '/api/parts/d/{0}/w/{1}/'.format(did, wid)).json()


    def get_part_bounding_box(self, did, wid, eid, pid):

        return self._api.request('get', '/api/parts/d/{0}/w/{1}/e/{2}/partid/{3}/boundingboxes'.format(did, wid, eid, pid)).json()


    def update_part_color(self, did, wid, eid, pid, appearance):

        body = {'appearance' : appearance}

        self._api.request('post', '/api/parts/d/{0}/w/{1}/e/{2}/partid/{3}/metadata'.format(did, wid, eid, pid), body=body)

        return
