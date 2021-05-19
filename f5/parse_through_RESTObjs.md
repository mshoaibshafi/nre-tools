# Parse Through BigIP REST Objects

## F5 REST API URI

- F5 GUI : https://\<f5-mgmt-ip\>/mgmt/tm/ltm/

## Persistence Profile
- https://\<f5-mgmt-ip\>/mgmt/tm/ltm/persistence/

## Cookie Persistence Profile
- https://\<f5-mgmt-ip\>/mgmt/tm/ltm/persistence/cookie

```python
  >>> from bigrest.bigip import BIGIP
  >>> b = BIGIP(ip, username, password)
  >>> cookie_profiles = b.load(f"/mgmt/tm/ltm/persistence/cookie")
  >>> type(cookie_profiles)
  <class 'list'>
  >>>
```

### LIST -  check <item>[0]
### dir() - ????

```python
  >>> dir(cookie_profiles[0])
    ['__class__', '__delattr__', '__dict__',  '__dir__',   '__doc__', '__eq__', '__format__',  '__ge__',  '__getattribute__', '__gt__',   '__hash__', '__init__',  '__init_subclass__',   '__le__', '__lt__',   '__module__', '__ne__',   '__new__', '__reduce__',  '__reduce_ex__',  '__repr__', '__setattr__',  '__sizeof__',  '__str__', '__subclasshook__',   '__weakref__',  'asdict', 'properties']
```
### PROPERTIES - check its type

```python
  >>> type(cookie_profiles[0].properties)
      <class 'dict'>
  >>>
```

### DICT
### Display whole dict ( both key / value )

```python
    >>> cookie_profiles[0].properties
      {'kind':  'tm:ltm:persistence:cookie:cookiestate',       'name': 'client-auto.company.info-cookie',       'partition': 'Common', 'fullPath': '/Common/      client-auto.company.info-cookie', 'generation':  1,     'selfLink': 'https://localhost/mgmt/tm/ ltm/   persistence/cookie/~Common~client-auto. company.  info-cookie?ver=13.1.3.4',  'alwaysSend': 'disabled',     'appService':  'none', 'cookieEncryption': 'disabled',      'cookieName': 'none', 'defaultsFrom': '/Common/    cookie', 'defaultsFromReference': {'link':   'https://  localhost/mgmt/tm/ltm/persistence/ cookie/    ~Common~cookie?ver=13.1.3.4'},  'description': 'none',       'encryptCookiePoolname': 'disabled',  'expiration':    '0', 'hashLength': 0,   'hashOffset': 0, 'httponly':    'enabled',  'matchAcrossPools': 'disabled',    'matchAcrossServices': 'disabled',       'matchAcrossVirtuals': 'disabled', 'method':      'insert', 'mirror': 'disabled',     'overrideConnectionLimit': 'enabled',   'secure':    'enabled', 'timeout': '180'}
    >>>
```

### All Keys

```python
  >>> cookie_profiles[0].properties.keys()
    dict_keys(['kind', 'name', 'partition', 'fullPath',   'generation',   'selfLink', 'alwaysSend', 'appService',   'cookieEncryption',   'cookieName', 'defaultsFrom',   'defaultsFromReference',  'description',  'encryptCookiePoolname', 'expiration',  'hashLength',  'hashOffset', 'httponly', 'matchAcrossPools',    'matchAcrossServices', 'matchAcrossVirtuals', 'method',   'mirror',  'overrideConnectionLimit', 'secure', 'timeout'])
  >>>

```


### Display all values

```python
  >>> cookie_profiles[0].properties.values()
    dict_values(['tm:ltm:persistence:cookie:cookiestate',   'client-auto. paciolan.info-cookie', 'Common', '/Common/  client-auto.paciolan.  info-cookie', 1, 'https://localhost/mgmt/  tm/ltm/persistence/cookie/ ~Common~client-auto.paciolan.  info-cookie?ver=13.1.3.4',  'disabled', 'none', 'disabled',   'none', '/Common/cookie', {'link':   'https://localhost/mgmt/tm/  ltm/persistence/cookie/~Common~cookie? ver=13.1.3.4'}, 'none',  'disabled', '0', 0, 0, 'enabled',  'disabled', 'disabled',   'disabled', 'insert', 'disabled',  'enabled', 'enabled', '180'])
  >>>
```

### Display one key-value pair

```python
  >>> cookie_profiles[0].properties['name']
    'client-auto.company.info-cookie'
  >>>
```


### dir() - definition

```python
  >>> dir(cookie_profiles)
  ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
