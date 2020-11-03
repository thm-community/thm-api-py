<p align="center"><img src="https://assets.tryhackme.com/img/THMlogo.png" width="350" title="TryHackMe Logo"></p>
<p align="center">API Py</p>


[![PyPI version](https://badge.fury.io/py/thmapi.svg)](https://badge.fury.io/py/thmapi)  
Python wrapper for TryHackMe public API  
Officially sponsored and affiliated with [TryHackMe](https://tryhackme.com/)

## Installation
```sh
pip install thmapi
```

## Usage
```python
from thmapi import THM

creds = {
    'username': '<USERNAME>',
    'password': '<PASSWORD'
}

thm = THM(credentials=creds) # Logging in is optional

thm.get_stats() # {'publicRooms': 203, 'totalUsers': 88017, 'cloneableRooms': 967}
```

## Contributing
You're welcome to create Issues/Pull Requests with features you'd want to see

## License
[MIT LICENSE](https://github.com/szymex73/py-thmapi/blob/master/LICENSE)
