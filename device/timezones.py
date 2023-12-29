#!/usr/bin/env python3
#
# Get current timezone (IANA format) and all the valid keys for IANA time zones
# -----------------------------------------------------------------------------
#
import json
import sys

# Get all IANA time zones
# -----------------------
#
# We check first the version to decide whether to use pytz or the built-in zoneinfo,
# since Panhandler is still on Python 3.8 as of writing.
#
timezone_names = []
if sys.version_info >= (3,9):
  import zoneinfo
  timezone_names = sorted(zoneinfo.available_timezones())
else:
  import pytz
  timezone_names = pytz.all_timezones
timezone_dict_list = []
for timezone_name in timezone_names:
  timezone_dict_list.append({ 'name': timezone_name })

timezones = { 'timezone_names': timezone_dict_list }
print(json.dumps(timezones, indent=2))
