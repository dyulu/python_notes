#!/usr/bin/python3

from pprint import pprint
import requests

pprint(requests.__version__)
pprint(dir(requests))
'''
'2.28.0'
['ConnectTimeout',
 'ConnectionError',
 'DependencyWarning',
 'FileModeWarning',
 'HTTPError',
 'JSONDecodeError',
 'NullHandler',
 'PreparedRequest',
 'ReadTimeout',
 'Request',
 'RequestException',
 'RequestsDependencyWarning',
 'Response',
 'Session',
 'Timeout',
 'TooManyRedirects',
 'URLRequired',
 '__author__',
 '__author_email__',
 '__build__',
 '__builtins__',
 '__cached__',
 '__cake__',
 '__copyright__',
 '__description__',
 '__doc__',
 '__file__',
 '__license__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '__title__',
 '__url__',
 '__version__',
 '_check_cryptography',
 '_internal_utils',
 'adapters',
 'api',
 'auth',
 'certs',
 'chardet_version',
 'charset_normalizer_version',
 'check_compatibility',
 'codes',
 'compat',
 'cookies',
 'delete',
 'exceptions',
 'get',
 'head',
 'hooks',
 'logging',
 'models',
 'options',
 'packages',
 'patch',
 'post',
 'put',
 'request',
 'session',
 'sessions',
 'ssl',
 'status_codes',
 'structures',
 'urllib3',
 'utils',
 'warnings']
'''

resp1 = requests.request(method = 'GET', url = 'https://api.github.com/users/dyulu')
resp2 = requests.get('https://api.github.com/users/dyulu')

pprint(resp1.status_code)
pprint(resp1.text)
pprint(resp2.status_code)
pprint(resp2.json())

# With sessions, the underlying TCP connection will be reused, resulting in significant performance boost when making multiple requests
s = requests.Session()
resp_repo = s.get('https://api.github.com/users/dyulu/repos')
resp_followers = s.get('https://api.github.com/users/dyulu/followers')
resp_following = s.get('https://api.github.com/users/dyulu/following')
s.close()
pprint(resp_repo.json())
pprint(resp_followers.json())
pprint(resp_following.json())

