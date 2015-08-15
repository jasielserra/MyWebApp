#! /usr/bin/python3

import json
from athletemodel import get_names_from_store
import yate

athletes_names = get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(athletes_names)))
