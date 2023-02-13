import getpass
import urllib.parse
import sys

tempOut = sys.stdout
sys.stdout = sys.stderr

proxy = input('Proxy: ')
comp = urllib.parse.urlsplit(proxy)

user = input('Username: ')
passwd = getpass.getpass()
enc = urllib.parse.quote_plus(passwd)

url = f"{comp.scheme}://{user}:{enc}@{comp.hostname}:{comp.port}"

sys.stdout = tempOut

print(f"export http_proxy='{url}'")
print(f"export https_proxy='{url}'")
#print(f"export http_proxy='http://{user}:{enc}@{proxy}'")
#print(f"export https_proxy='http://{user}:{enc}@{proxy}'")

