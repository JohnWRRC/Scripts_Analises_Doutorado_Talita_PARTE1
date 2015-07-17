import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch

def txt(mapa,txtname):
    grass.run_command('g.region',rast=mapa)
    os.chdir(r'C:\_data\talitha\Mapas_classificados_final')
    os.chdir(r'C:\_data\talitha\Mapas_classificados_final')
    x=grass.read_command('r.stats',flags='a',input=mapa)
    y=x.split('\n')
    #print y
    
    listapoio=[]
    for a in y:
        if ('*' in a):
            print a
            continue
        else:
            listapoio.append(a)
    print listapoio 
    del listapoio[-1]
        #print listapoio
    
    fd = open(txtname,'w')
    myCsvRow="cod"",""areaM2" ",""Area_ha\n"
    fd.write(myCsvRow)
    for i in listapoio:
        temp1=i.split(' ')
        cod=int(temp1[0])
        
        aream2=float(temp1[1])
        area_HA=round(aream2/10000,2)
        fd.write(`cod`+','+`aream2`+','+`area_HA`+'\n')
    fd.close()
txt('buffer_1984_semdissolv1000rast_img', 'teste.csv')