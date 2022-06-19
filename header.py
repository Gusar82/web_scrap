# https://pypi.org/project/fake-headers/
from fake_headers import Headers
HEADERS = Headers(
    browser='chrome',
    os='win',
    headers=True,
).generate()

if __name__ == '__main__':
    from requests import get
    # print(HEADERS)
    r = get('http://whatismyheader.com/', headers=HEADERS)
    print(r.text)