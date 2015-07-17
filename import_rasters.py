import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA=[]  


for file in os.listdir(r'E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters'):
    if fnmatch.fnmatch(file, '*.tif'):
        #print file
        LISTA.append(file)
        
          

os.chdir(r'E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters')
for i in LISTA:
    out=i.replace('.tif',"_tif")
    grass.run_command('r.in.gdal',input=i,out=out,overwrite=True)
    
    
    