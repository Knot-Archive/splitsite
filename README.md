## summary
split website, count word, asynchronous, save result into database.

## requirement
**python requirements**
```bash
pip install -r requirements.txt
```
**database with docker: Postgres** 
```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
```bash
docker run --name EngCalc-local-postgres -e POSTGRES_PASSWORD=FeintVeela-Vagrant -d postgress
```
**MQ worker with docker: Redis**
```bash
docker run --name some-redis -v /docker/host/dir:/data -d redis redis-server --appendonly yes
```
**need Download nltk recource**
```bash
python install_nltk_resource
```

## migrations
**database init**
```bash
python manage.py db init
```
**database migrate**
```bash
python manage.py db migrate
```

**database upgrade**
```bash
python manage.py db upgrade
```

## start
**start up MQ worker**
```bash
python worker.py
```
**start web server**
```bash
python manage.py runserver
```
