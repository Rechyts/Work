# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy, os, zipfile, smtplib, mimetypes, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from datetime import date

d = date.today()
folder_data = d.strftime("%d.%m.%y")
data = r'd:\D\!shp_2_export\TOR\{0}'.format(folder_data)
if not os.path.exists(data):
    os.makedirs(data)

region_brest = r'{0}\brest'.format(data)
if not os.path.exists(region_brest):
    os.makedirs(region_brest)

region_vitebsk = r'{0}\vitebsk'.format(data)
if not os.path.exists(region_vitebsk):
    os.makedirs(region_vitebsk)

region_gomel = r'{0}\gomel'.format(data)
if not os.path.exists(region_gomel):
    os.makedirs(region_gomel)

region_grodno = r'{0}\grodno'.format(data)
if not os.path.exists(region_grodno):
    os.makedirs(region_grodno)

region_minsk = r'{0}\minsk'.format(data)
if not os.path.exists(region_minsk):
    os.makedirs(region_minsk)

region_mogilev = r'{0}\mogilev'.format(data)
if not os.path.exists(region_mogilev):
    os.makedirs(region_mogilev)

brest1 = r'{0}\SK63(1)'.format(region_brest)
if not os.path.exists(brest1):
    os.makedirs(brest1)

brest2 = r'{0}\SK63(2)'.format(region_brest)
if not os.path.exists(brest2):
    os.makedirs(brest2)

vitebsk2 = r'{0}\SK63(2)'.format(region_vitebsk)
if not os.path.exists(vitebsk2):
    os.makedirs(vitebsk2)

vitebsk3 = r'{0}\SK63(3)'.format(region_vitebsk)
if not os.path.exists(vitebsk3):
    os.makedirs(vitebsk3)

gomel2 = r'{0}\SK63(2)'.format(region_gomel)
if not os.path.exists(gomel2):
    os.makedirs(gomel2)

gomel3 = r'{0}\SK63(3)'.format(region_gomel)
if not os.path.exists(gomel3):
    os.makedirs(gomel3)

grodno1 = r'{0}\SK63(1)'.format(region_grodno)
if not os.path.exists(grodno1):
    os.makedirs(grodno1)

grodno2 = r'{0}\SK63(2)'.format(region_grodno)
if not os.path.exists(grodno2):
    os.makedirs(grodno2)

minsk2 = r'{0}\SK63(2)'.format(region_minsk)
if not os.path.exists(minsk2):
    os.makedirs(minsk2)

mogilev2 = r'{0}\SK63(2)'.format(region_mogilev)
if not os.path.exists(mogilev2):
    os.makedirs(mogilev2)

mogilev3 = r'{0}\SK63(3)'.format(region_mogilev)
if not os.path.exists(mogilev3):
    os.makedirs(mogilev3)


#УКАЗАТЬ ПУТЬ К ШЕЙПУ!!!!!!!!
# Script arguments
rb_shp = r'd:\rb.shp'

#Brest
# Local variables:
brest_shp = r'{0}\brest.shp'.format(region_brest)
brest_city_shp = r'{0}\brest_city.shp'.format(region_brest)
brest_snp_shp = r'{0}\brest_snp.shp'.format(region_brest)
brest_ss_shp = r'{0}\brest_ss.shp'.format(region_brest)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
brest1__2_ = brest1
arcpy.env.outputCoordinateSystem__2_ = "PROJCS['CK1963(c)1',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',1250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',24.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
brest2__2_ = brest2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, brest_shp, "\"SOATO\" LIKE'1%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(brest_shp, brest_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(brest_shp, brest_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(brest_shp, brest_ss_shp, "\"CATEGORY\" =103")

# Process: Класс пространственных объектов в шейп-файл (несколько)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)1',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',1250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',24.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
brest_city1 = r'{0}\brest_city.shp'.format(region_brest)
brest_snp1 = r'{0}\brest_snp.shp'.format(region_brest)
brest_ss1 = r'{0}\brest_ss.shp'.format(region_brest)
arcpy.FeatureClassToShapefile_conversion([brest_city1, brest_snp1, brest_ss1], brest1__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
brest_city2 = r'{0}\brest_city.shp'.format(region_brest)
brest_snp2 = r'{0}\brest_snp.shp'.format(region_brest)
brest_ss2 = r'{0}\brest_ss.shp'.format(region_brest)
arcpy.FeatureClassToShapefile_conversion([brest_city2, brest_snp2, brest_ss2], brest2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0




#Vitebsk
# Local variables:
vitebsk_shp = r'{0}\vitebsk.shp'.format(region_vitebsk)
vitebsk_city_shp = r'{0}\vitebsk_city.shp'.format(region_vitebsk)
vitebsk_snp_shp = r'{0}\vitebsk_snp.shp'.format(region_vitebsk)
vitebsk_ss_shp = r'{0}\vitebsk_ss.shp'.format(region_vitebsk)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
vitebsk2__2_ = vitebsk2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
vitebsk3__2_ = vitebsk3
arcpy.env.outputCoordinateSystem__2_ = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, vitebsk_shp, "\"SOATO\" LIKE'2%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(vitebsk_shp, vitebsk_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(vitebsk_shp, vitebsk_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(vitebsk_shp, vitebsk_ss_shp, "\"CATEGORY\" =103")


# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
vitebsk_city2 = r'{0}\vitebsk_city.shp'.format(region_vitebsk)
vitebsk_snp2 = r'{0}\vitebsk_snp.shp'.format(region_vitebsk)
vitebsk_ss2 = r'{0}\vitebsk_ss.shp'.format(region_vitebsk)
arcpy.FeatureClassToShapefile_conversion([vitebsk_city2, vitebsk_snp2, vitebsk_ss2], vitebsk2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Класс пространственных объектов в шейп-файл (несколько)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
vitebsk_city3 = r'{0}\vitebsk_city.shp'.format(region_vitebsk)
vitebsk_snp3 = r'{0}\vitebsk_snp.shp'.format(region_vitebsk)
vitebsk_ss3 = r'{0}\vitebsk_ss.shp'.format(region_vitebsk)
arcpy.FeatureClassToShapefile_conversion([vitebsk_city3, vitebsk_snp3, vitebsk_ss3], vitebsk3__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0



#Gomel
# Local variables:
gomel_shp = r'{0}\gomel.shp'.format(region_gomel)
gomel_city_shp = r'{0}\gomel_city.shp'.format(region_gomel)
gomel_snp_shp = r'{0}\gomel_snp.shp'.format(region_gomel)
gomel_ss_shp = r'{0}\gomel_ss.shp'.format(region_gomel)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
gomel2__2_ = gomel2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
gomel3__2_ = gomel3
arcpy.env.outputCoordinateSystem__2_ = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, gomel_shp, "\"SOATO\" LIKE'3%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(gomel_shp, gomel_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(gomel_shp, gomel_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(gomel_shp, gomel_ss_shp, "\"CATEGORY\" =103")


# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
gomel_city2 = r'{0}\gomel_city.shp'.format(region_gomel)
gomel_snp2 = r'{0}\gomel_snp.shp'.format(region_gomel)
gomel_ss2 = r'{0}\gomel_ss.shp'.format(region_gomel)
arcpy.FeatureClassToShapefile_conversion([gomel_city2, gomel_snp2, gomel_ss2], gomel2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Класс пространственных объектов в шейп-файл (несколько)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
gomel_city3 = r'{0}\gomel_city.shp'.format(region_gomel)
gomel_snp3 = r'{0}\gomel_snp.shp'.format(region_gomel)
gomel_ss3 = r'{0}\gomel_ss.shp'.format(region_gomel)
arcpy.FeatureClassToShapefile_conversion([gomel_city3, gomel_snp3, gomel_ss3], gomel3__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0



#Grodno
# Local variables:
grodno_shp = r'{0}\grodno.shp'.format(region_grodno)
grodno_city_shp = r'{0}\grodno_city.shp'.format(region_grodno)
grodno_snp_shp = r'{0}\grodno_snp.shp'.format(region_grodno)
grodno_ss_shp = r'{0}\grodno_ss.shp'.format(region_grodno)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
grodno1__2_ = grodno1
arcpy.env.outputCoordinateSystem__2_ = "PROJCS['CK1963(c)1',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',1250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',24.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
grodno2__2_ = grodno2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, grodno_shp, "\"SOATO\" LIKE'4%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(grodno_shp, grodno_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(grodno_shp, grodno_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(grodno_shp, grodno_ss_shp, "\"CATEGORY\" =103")

# Process: Класс пространственных объектов в шейп-файл (несколько)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)1',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',1250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',24.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
grodno_city1 = r'{0}\grodno_city.shp'.format(region_grodno)
grodno_snp1 = r'{0}\grodno_snp.shp'.format(region_grodno)
grodno_ss1 = r'{0}\grodno_ss.shp'.format(region_grodno)
arcpy.FeatureClassToShapefile_conversion([grodno_city1, grodno_snp1, grodno_ss1], grodno1__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
grodno_city2 = r'{0}\grodno_city.shp'.format(region_grodno)
grodno_snp2 = r'{0}\grodno_snp.shp'.format(region_grodno)
grodno_ss2 = r'{0}\grodno_ss.shp'.format(region_grodno)
arcpy.FeatureClassToShapefile_conversion([grodno_city2, grodno_snp2, grodno_ss2], grodno2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0


#Minsk
# Local variables:
minsk_shp = r'{0}\minsk.shp'.format(region_minsk)
minsk_city_shp = r'{0}\minsk_city.shp'.format(region_minsk)
minsk_snp_shp = r'{0}\minsk_snp.shp'.format(region_minsk)
minsk_ss_shp = r'{0}\minsk_ss.shp'.format(region_minsk)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
minsk2__2_ = minsk2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, minsk_shp, "\"SOATO\" LIKE '6%' OR \"SOATO\" LIKE '5%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(minsk_shp, minsk_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(minsk_shp, minsk_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(minsk_shp, minsk_ss_shp, "\"CATEGORY\" =103")


# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
minsk_city2 = r'{0}\minsk_city.shp'.format(region_minsk)
minsk_snp2 = r'{0}\minsk_snp.shp'.format(region_minsk)
minsk_ss2 = r'{0}\minsk_ss.shp'.format(region_minsk)
arcpy.FeatureClassToShapefile_conversion([minsk_city2, minsk_snp2, minsk_ss2], minsk2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0


#Mogilev
# Local variables:
mogilev_shp = r'{0}\mogilev.shp'.format(region_mogilev)
mogilev_city_shp = r'{0}\mogilev_city.shp'.format(region_mogilev)
mogilev_snp_shp = r'{0}\mogilev_snp.shp'.format(region_mogilev)
mogilev_ss_shp = r'{0}\mogilev_ss.shp'.format(region_mogilev)

arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
mogilev2__2_ = mogilev2
arcpy.env.outputCoordinateSystem__3_ = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
mogilev3__2_ = mogilev3
arcpy.env.outputCoordinateSystem__2_ = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"

# Process: Выборка
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
arcpy.Select_analysis(rb_shp, mogilev_shp, "\"SOATO\" LIKE'7%'")
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Выборка (2)
arcpy.Select_analysis(mogilev_shp, mogilev_city_shp, "CATEGORY = 111 OR CATEGORY = 112 OR CATEGORY= 121 OR CATEGORY= 113 OR CATEGORY= 123 OR CATEGORY = 213 OR CATEGORY= 221 OR CATEGORY= 223 OR CATEGORY= 222")

# Process: Выборка (3)
arcpy.Select_analysis(mogilev_shp, mogilev_snp_shp, "\"CATEGORY\" =231 OR \"CATEGORY\"=232 OR \"CATEGORY\"=234 OR \"CATEGORY\"=235 OR \"CATEGORY\"=239")

# Process: Выборка (4)
arcpy.Select_analysis(mogilev_shp, mogilev_ss_shp, "\"CATEGORY\" =103")


# Process: Класс пространственных объектов в шейп-файл (несколько) (2)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
mogilev_city2 = r'{0}\mogilev_city.shp'.format(region_mogilev)
mogilev_snp2 = r'{0}\mogilev_snp.shp'.format(region_mogilev)
mogilev_ss2 = r'{0}\mogilev_ss.shp'.format(region_mogilev)
arcpy.FeatureClassToShapefile_conversion([mogilev_city2, mogilev_snp2, mogilev_ss2], mogilev2__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0

# Process: Класс пространственных объектов в шейп-файл (несколько)
tempEnvironment0 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
mogilev_city3 = r'{0}\mogilev_city.shp'.format(region_mogilev)
mogilev_snp3 = r'{0}\mogilev_snp.shp'.format(region_mogilev)
mogilev_ss3 = r'{0}\mogilev_ss.shp'.format(region_mogilev)
arcpy.FeatureClassToShapefile_conversion([mogilev_city3, mogilev_snp3, mogilev_ss3], mogilev3__2_)
arcpy.env.outputCoordinateSystem = tempEnvironment0


#create zip
def WriteDirectoryToZipFile(namezip, basePath, zipOperation = zipfile.ZIP_DEFLATED ):
    zipHandle = zipfile.ZipFile(os.path.join(basePath, '{0}.zip'.format(namezip)), 'a', zipOperation)
    listdirs = os.listdir(basePath)
    for l in listdirs:
        if l.find('SK')>-1:
            for root, dirs, files in os.walk(os.path.join(basePath, l)):
                zipHandle.write(root, l, zipOperation)
                for f in files:
                    filePath = os.path.join(root, f)
                    fileInZipPath = os.path.join(l, f)
                    zipHandle.write(filePath, fileInZipPath, zipOperation)

#attach info to mail
def getAttachment(path, filename):
    ctype, encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    fp = open(path, 'rb')
    if maintype == 'text':
        attach = MIMEText(fp.read(),_subtype=subtype)
    elif maintype == 'message':
        attach = email.message_from_file(fp)
    elif maintype == 'image':
        attach = MIMEImage(fp.read(),_subtype=subtype)
    elif maintype == 'audio':
        attach = MIMEAudio(fp.read(),_subtype=subtype)
    else:
        attach = MIMEBase(maintype, subtype)
        attach.set_payload(fp.read())
        encoders.encode_base64(attach)
    attach.add_header('Content-Disposition', 'attachment',
filename=filename)
    return attach


#send email
def sendWithAttachmentsZipped(file, directory, recipient):
    msg = MIMEMultipart()
    dir = directory
    for filename in os.listdir(dir):
        if filename.find('zip') > - 1 and filename.find(file) > - 1:
            path = os.path.join(dir, filename)
            attach = getAttachment(path, filename)
            msg.attach(attach)
    FROM = "ate@nca.by"
    TO = recipient
    msg['From'] = FROM
    COMMASPACE = ', '
    msg['To'] = COMMASPACE.join(TO)
    msg['Subject'] = "Обновление  данных Реестра АТЕ И ТЕ"
    text = "Здравствуйте!\nНаправляем Вам  зарегистрированные  границы  АТЕ и ТЕ для обновления  данных NKA_NET и для " \
           "работ по систематическому присвоению адресов."\
           "\nГраницы предоставляются в формате шейп-файла в СК63 с разбивкой по"\
           "\nсельским советам,сельским населённым пунктам,городам и посёлкам городского  типа."\
           "\nС уважением специалист по кадастру и ГИС Речиц Вероника Сергеевна.\nКонтактный телефон 8(017) 284-47-73."
    part1 = MIMEText(text, 'plain', 'utf-8')
    msg.attach(part1)

    server = smtplib.SMTP('cod', 25)
    server.login("login", "password")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
