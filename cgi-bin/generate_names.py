#! /usr/bin/python3

import json
from athletemodel import get_namesID_from_store
import yate

names = get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))
