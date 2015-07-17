import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math

lista_vects=grass.mlist_grouped ('vect', pattern='*semdissolv*') ['PERMANENT']
for i in lista_vects:
    out=i.replace('shp','_rast')
    grass.run_command('g.region',vect=i,res=10)
    grass.run_command('v.to.rast',input=i, out=out,use='attr',column='id')
    
    