import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(whoToGreet):
    greeting = "Hello, {}".format(whoToGreet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

