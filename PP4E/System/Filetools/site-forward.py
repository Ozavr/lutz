"""
############################################################################## 
Создает страницы со ссылками переадресации на перемещенный веб-сайт.
Генерирует по одной странице для каждого существующего на сайте файла html; 
сгенерированные файлы нужно выгрузить на ваш старый веб-сайт. 
Смотрите описание ftplib далее в книге, где представлены приемы реализации 
выгрузки файлов в сценариях после или в процессе создания файлов страниц. 
##############################################################################
"""


import os


servername = 'learning-python.com'
homedir = 'books'
sitefilesdir = r'/Users/Ozavr/Desktop/projects/lutz/temp/public_html'
uploaddir = r'/Users/Ozavr/Desktop/projects/lutz/temp/isp_forward'
templatename = 'template.html'


try: 
    os.mkdir(uploaddir)
except OSError:
    pass

template = open(templatename).read()
sitefiles = os.listdir(sitefilesdir)

count = 0
for filename in sitefiles:
    if (filename.endswith('.html')) and (filename.endswith('.htm')):
        fwdname = os.path.join(uploaddir, filename)
        print('creating', filename, 'as', fwdname)
        filetext = template.replace('$server$', servername)
        filetext = filetext.replace('$home$', homedir)
        filetext = filetext.replace('$file$', filename)
        open(fwdname, 'w').write(filetext)
        count += 1

print('Last file =>\n', filetext, sep='')
print('Done:', count, 'forward files created.')