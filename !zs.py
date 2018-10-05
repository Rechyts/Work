# encoding: utf8
import arcpy, os, zipfile, smtplib, mimetypes, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from datetime import date

d = date.today()
year = d.year
folder_data = d.strftime("%B")
list_region = ('Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Minsk', 'Mogilev')
list_data = []
for region in list_region:
    data = 'd:\D\!shp_2_export\Zemslizba\{0}\{1}\{2}'.format(region, year, folder_data)
    if not os.path.exists(data):
        os.makedirs(data)
    list_data.append(data)


geogsk = "GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
sk63_1 = "PROJCS['CK1963(c)1',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',1250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',24.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
sk63_2 = "PROJCS['CK1963(c)2',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',2250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',27.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
sk63_3 = "PROJCS['CK1963(c)3',GEOGCS['GCS_Pulkovo_1942',DATUM['D_Pulkovo_1942',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Gauss_Kruger'],PARAMETER['False_Easting',3250000.0],PARAMETER['False_Northing',-12900.568],PARAMETER['Central_Meridian',30.95],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',-0.01666666666],UNIT['Meter',1.0]]"
rb_shp = r'd:\rb.shp'

district = {'Baranovichskij':	('1204%', '1410%'),
 'Brestskij':	('1212%', '1401%'),
 'Gancevichskij':	('1216%', '0'),
 'Ivanovskij':	('1230%', '0'),
 'Kameneckij':	('1240%', '0'),
 'Kobrinskij':	('1243%', '0'),
 'Maloritskij':	('1252%', '0'),
 'Pinskij':	('1254%', '1445%'),
 'Glubokskij':	('2215%', '0'),
 'Lepelskij':	('2227%', '0'),
 'Miorskij':	('2233%', '0'),
 'Orshanskij':	('2236%', '0'),
 'Polockij':	('2238%', '2418%'),
 'Postavskij':	('2240%', '0'),
 'Rossonskij':	('2242%', '0'),
 'Shumilinskij':	('2258%', '0'),
 'Dobrushskij':	('3212%', '0'),
 'Elskij':	('3214%', '0'),
 'Oktyabrskij':	('3240%', '0'),
 'Petrikovskij':	('3243%', '0'),
 'Rechickij':	('3245%', '0'),
 'Svetlogorskij':	('3250%', '0'),
 'Checherskij':	('3256%', '0'),
 'Voronovskij':	('4213%', '0'),
 'Grodnenskij':	('4220%', '4401%'),
 'Ivievskij':	('4229%', '0'),
 'Korelichskij':	('4233%', '0'),
 'Lidskij':	('4236%', '0'),
 'Novogrudskij':	('4243%', '0'),
 'Ostroveckij':	('4246%', '0'),
 'Smorgonskij':	('4256%', '0'),
 'Schuchinskij':	('4258%', '0'),
 'Kopylskij':	('6228%', '0'),
 'Nesvizhskij':	('6242%', '0'),
 'Smolevichskij':	('6248%', '6413%'),
 'Soligorskij':	('6250%', '0'),
 'Starodorozhskij':	('6252%', '0'),
 'Uzdenskij':	('6256%', '0'),
 'Belynichskij':	('7204%', '0'),
 'Klimovichskij':	('7228%', '0'),
 'Kruglyanskij':	('7242%', '0'),
 'Slavgorodskij':	('7250%', '0'),
 'Shklovskij':	('7258%', '0')}

sk = {'Baranovichskij':	sk63_1,
 'Brestskij':	sk63_1,
 'Gancevichskij':	sk63_2,
 'Ivanovskij':	sk63_1,
 'Kameneckij':	sk63_1,
 'Kobrinskij':	sk63_1,
 'Maloritskij':	sk63_1,
 'Pinskij':	sk63_1,
 'Glubokskij':	sk63_2,
 'Lepelskij':	sk63_2,
 'Miorskij':	sk63_2,
 'Orshanskij':	sk63_3,
 'Polockij':	sk63_2,
 'Postavskij':	sk63_2,
 'Rossonskij':	sk63_2,
 'Shumilinskij':	sk63_3,
 'Dobrushskij':	sk63_3,
 'Elskij':	sk63_2,
 'Oktyabrskij':	sk63_2,
 'Petrikovskij':	sk63_2,
 'Rechickij':	sk63_3,
 'Svetlogorskij':	sk63_3,
 'Checherskij':	sk63_3,
 'Voronovskij':	sk63_1,
 'Grodnenskij':	sk63_1,
 'Ivievskij':	sk63_1,
 'Korelichskij':	sk63_1,
 'Lidskij':	sk63_1,
 'Novogrudskij':	sk63_1,
 'Ostroveckij':	sk63_1,
 'Smorgonskij':	sk63_1,
 'Schuchinskij':	sk63_1,
 'Kopylskij':	sk63_2,
 'Nesvizhskij':	sk63_2,
 'Smolevichskij':	sk63_2,
 'Soligorskij':	sk63_2,
 'Starodorozhskij':	sk63_2,
 'Uzdenskij':	sk63_2,
 'Belynichskij':	sk63_3,
 'Klimovichskij':	sk63_3,
 'Kruglyanskij':	sk63_3,
 'Slavgorodskij':	sk63_3,
 'Shklovskij':	sk63_3}


def select_region(region, startwith):
    for d in list_data:
        if d.find(region) > - 1:
            for key in district.keys():
                if district[key][0].startswith(startwith):
                    shp = '{0}/{1}1.shp'.format(d, key)
                    shp_sk = '{0}/{1}.shp'.format(d, key)
                    tempEnvironment0 = arcpy.env.outputCoordinateSystem
                    arcpy.env.outputCoordinateSystem = geogsk
                    arcpy.Select_analysis(rb_shp, shp, "\"SOATO\" LIKE '{0}' OR \"SOATO\" LIKE '{1}'".format(district[key][0], district[key][1]))
                    arcpy.env.outputCoordinateSystem = tempEnvironment0
                    arcpy.Project_management(shp, shp_sk, sk[key], "", geogsk)
        for file in os.listdir(d):
            if file.find('1') > - 1:
                os.remove('{0}/{1}'.format(d, file))


#zip
def WriteDirectoryToZipFile(zipOperation = zipfile.ZIP_DEFLATED ):
    for basePath in list_data:
        for region in list_region:
            if basePath.find(region) > - 1:
                for root, dirs, files in os.walk(basePath):
                    for file in files:
                        for key in district.keys():
                            if file.find(key) > - 1 and not file.find("zip") > - 1:
                                zip_name = file.split('.')[0]
                                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(basePath, zip_name), 'a', zipOperation)
                                myzip.write(os.path.join(root, file), arcname=file)
                                myzip.close()



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


def sendWithAttachmentsZipped(file, recipient):
    msg = MIMEMultipart()
    for basePath in list_data:
        for region in list_region:
            if basePath.find(region) > - 1:
                dir = os.path.join(basePath)
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
    msg['Subject'] = 'Предоставление информации от ГУП "Национальное кадастровое агентство"'
    text = "Здравствуйте!\nНаправляем Вам информацию из единого реестра АТЕ и ТЕ" \
            "\nСообщите о прочтении настоящего письма, спасибо!"\
           "\nС уважением специалист по кадастру и  геоинформационным системам Речиц Вероника Сергеевна.\nКонтактный телефон 8(017) 284-47-73."
    part1 = MIMEText(text, 'plain', 'utf-8')
    msg.attach(part1)

    server = smtplib.SMTP('cod', 25)
    server.login("login", "password")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
