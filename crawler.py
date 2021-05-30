import sys, shlex, subprocess, time, binascii, os, random
from bs4 import BeautifulSoup

t = None
c = None
if len(sys.argv) > 1:
    t = sys.argv[1]
    if t.isnumeric():
        t = int(t)
        c = 0
    else:
        t = None

cmd = "curl 'http://programmingexcuses.com/' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: zh-TW,en-US;q=0.8,en;q=0.5,ja;q=0.3' --compressed -H 'Referer: http://programmingexcuses.com/' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache'"
cmd_args = shlex.split(cmd)

while 1:
    process = subprocess.Popen(cmd_args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    ret = stdout.decode("UTF-8")

    if len(ret) < 1:
        time.sleep(random.uniform(3, 10))
        continue
    else:
        soup = BeautifulSoup(ret, "html.parser")
        line = soup.find("div", {"class": "wrapper"}).find("a").get_text()
        crc = hex(binascii.crc32(line.encode()))[2:].rjust(8, "0")

        filepath = "./data/" + crc + ".txt"
        if not os.path.exists(filepath):
            with open(filepath, "w") as fh:
                fh.write(line)
            print(crc, "\t", line)
        else:
            print("*********************************************************************************")

    if t:
        c += 1
        if c >= t:
            exit()

    time.sleep(random.uniform(2, 5))
