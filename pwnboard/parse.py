#!/usr/bin/env python3
from . import r
from . import logger


def saveData(data):
    '''
    Parse updates that come in via POST to the server.

    'victim' and 'application' are required in the data
    '''
    if data.get('victim', '127.0.0.1').lower() in ["127.0.0.1", "none", None, "null"]:
        return
    
    logger.debug("updated beacon for {} from {}".format(data['victim'], data['type']))
    # Fill in default values. Fastest way according to https://stackoverflow.com/a/17501506
    data['message'] if 'message' in data else None
    data['server'] if 'server' in data else None

    # save this to the DB
    r.hmset(data['victim'], {
        'application': data['application'],
        'message': data['message'],
        'last_seen': data['server']
    })