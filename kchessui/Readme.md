# SFTP Upload #

## Usage ##
sftp.py --upload/--download --dest <file> --local <file> --host <ip/host> --port <port> --username <name> --password <password>

example:

### Upload a file ###
```
sftp.py --upload --dest remote.py --local local.py --host 10.36.47.99 --port 22 --username dweerapurage --password xxxxx
```

### Download a file ###
```
sftp.py --download --dest remote.py --local local.py --host 10.36.47.99 --port 22 --username dweerapurage --password xxxxx
```

### Inculde configurations in a file ###
--- # Host
   host: 10.36.47.99
   port: 22
--- # User
  username: dweerapurage
  password: "my middle finger do not go down, how do I wave?"


### Use a config file to specify configurations ###
```
sftp.py --upload --dest remote/ --local local/ --config <configfile>
```
