import arcpy
from arcpy import env
import os
import fnmatch
env.workspace=r'E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19'


LISTA2=arcpy.ListFeatureClasses()
env.workspace=r'E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters'
for i in LISTA2:
            inpu=i.replace('.shp','')
            out=inpu+'_rast.tif'
            print inpu, out
            
            arcpy.PolygonToRaster_conversion(inpu,"land_use",out,"CELL_CENTER","NONE",10)

