# encoding: utf8
import arcpy
from datetime import date
import os
import zipfile
import smtplib
import mimetypes
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart


d = date.today()
folder_data = d.strftime("%B")
data = r'd:\D\!shp_2_export\Giprozem\{0}'.format(folder_data)
if not os.path.exists(data):
    os.makedirs(data)


s = date.today()
year = s.year
soato_data = s.strftime("%d.%m.%Y")



#УКАЗАТЬ ПУТЬ к ШЕЙПУ!!!!!!!!!
# Local variables:
rb_shp = r'd:\rb.shp'

def select_region():
    brest_shp = r'{0}\brest.shp'.format(data)
    vitebsk_shp = r'{0}\vitebsk.shp'.format(data)
    gomel_shp = r'{0}\gomel.shp'.format(data)
    grodno_shp = r'{0}\grodno.shp'.format(data)
    minsk_shp = r'{0}\minsk.shp'.format(data)
    mogilev_shp = r'{0}\mogilev.shp'.format(data)

    arcpy.Select_analysis(rb_shp, brest_shp, "\"SOATO\" LIKE'1%'")
    arcpy.Select_analysis(rb_shp, vitebsk_shp, "\"SOATO\" LIKE'2%'")
    arcpy.Select_analysis(rb_shp, gomel_shp, "\"SOATO\" LIKE'3%'")
    arcpy.Select_analysis(rb_shp, grodno_shp, "\"SOATO\" LIKE'4%'")
    arcpy.Select_analysis(rb_shp, minsk_shp, "\"SOATO\" LIKE '6%' OR \"SOATO\" LIKE '5%'")
    arcpy.Select_analysis(rb_shp, mogilev_shp, "\"SOATO\" LIKE'7%'")



def zip_file():
    for root, dirs, files in os.walk(data):
        for file in files:
            if file.find("brest") > -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
                myzip.write(os.path.join(root, file), arcname=file)
                myzip.close()
            elif file.find("vitebsk")> -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
                myzip.write(os.path.join(root, file), arcname=file)
                myzip.close()
            elif file.find("grodno")> -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
                myzip.write(os.path.join(root, file), arcname=file)
                myzip.close()
            elif file.find("gomel")> -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
                myzip.write(os.path.join(root, file), arcname=file)
                myzip.close()
            elif file.find("minsk")> -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
                myzip.write(os.path.join(root, file), arcname=file)
                myzip.close()
            elif file.find("mogilev")> -1 and not file.find("zip") > - 1:
                zip_name = file.split(".")[0]
                myzip = zipfile.ZipFile('{0}/{1}.zip'.format(data, zip_name), 'a', zipfile.ZIP_DEFLATED)
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
    dir = os.path.join(data)
    for filename in os.listdir(dir):
        if filename.find('zip') > - 1 and filename.find(file) > - 1:
            path = os.path.join(dir, filename)
            attach = getAttachment(path, filename)
            msg.attach(attach)
        if filename.find('te') > - 1 and filename.find(file) > - 1:
            path = os.path.join(dir, filename)
            attach = getAttachment(path, filename)
            msg.attach(attach)
        elif filename.find('minsk.zip') > - 1 and filename.find(file) > - 1:
            path = os.path.join(dir, 'SOATO_{0}.xlsx'.format(soato_data))
            attach = getAttachment(path, 'SOATO_{0}.xlsx'.format(soato_data))
            msg.attach(attach)
        # Открываются раз в квартал, т.к. Бресту классификатор представляется ежеквартально!!!
        elif filename.find('brest.zip') > - 1 and filename.find(file) > - 1:
            path = os.path.join(dir, 'SOATO_{0}.xlsx'.format(soato_data))
            attach = getAttachment(path, 'SOATO_{0}.xlsx'.format(soato_data))
            msg.attach(attach)


    FROM = "ate@nca.by"
    TO = recipient
    msg['From'] = FROM
    COMMASPACE = ', '
    msg['To'] = COMMASPACE.join(TO)
    msg['Subject'] = 'Предоставление информации от ГУП "Национальное кадастровое агентство"'
    text = "Здравствуйте!\nНаправляем Вам информацию из Единого реестра АТЕ и ТЕ." \
            "\nСообщите о прочтении настоящего письма, спасибо!"\
           "\nС уважением специалист по кадастру и  геоинформационным системам Речиц Вероника Сергеевна.\nКонтактный телефон 8(017) 284-47-73."
    part1 = MIMEText(text, 'plain', 'utf-8')
    msg.attach(part1)

    server = smtplib.SMTP('cod', 25)
    server.login("login", "password")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
