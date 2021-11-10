'''
网站备份文件泄露
目前需要手动更改变量 target，因为我还不会用sys库传参，见凉
背景：CTFHub =》 技能树 =》 信息泄露 =》 网站备份文件
'''
import requests

# 常用备份文件名
fileNames = ['web', 'website', 'backup', 'back', 'www', 'wwwroot', 'temp']

# 常用备份文件类型
suffixes = ['tar', 'tar.gz', 'zip', 'rar']


for fileName in fileNames:
    for suffix in suffixes:
        target = ''
        bak = fileName + '.' + suffix
        url = target + bak
        # print(url)
        resp = requests.get(url=url)
        print(bak, ' : ', resp.status_code)
        resp.close()
