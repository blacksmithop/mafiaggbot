from utils.client import Mafia
from sys import exit

m = Mafia()
try:
    m.run()
except KeyboardInterrupt:
    exit(1)
