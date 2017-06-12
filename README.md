this script will initialize your kinit and run ssh connect

## Installation

``` shell
pip install -r requirements.txt
```

## Parameter

Setup your parameter

``` yaml
# User used to make call
user: cifren
server:
  grouper:
    name: host.com
```

## Usage

```
  python ssh_connect.py serverName

ex:
  python ssh_connect.py grouper
```

## Add to your environment

Make sure your file has permission 775

``` bash
sudo chmod 775 ssh_connect.py
```

Create your symlink

``` bash
cd /usr/bin
# Replace with your file path
sudo ln -s ~/ssh_connect/ssh_connect.py ssh_connect
```
