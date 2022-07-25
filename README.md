# Flask Api

## Enviornment
### Create Enviornment
copy below and add your own config to your .env file.
If you do not have a .env file, please create one.
```
DB_HOST= 'your host and port'
DB_USER= 'usernme'
DB_PASS= 'password'
DB_NAME= 'database name'
```

### install Packages
`pip install -r requirements.txt`


## Migration

### INIT DB
`flask db init`

### MIGRATE DB
`flask db migrate`

### UPGRADE DB
`flask db upgrade`

## Run flask
### Run the server
`python main.py`
