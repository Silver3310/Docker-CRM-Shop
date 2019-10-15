## Start project with Docker

Now it is possible to start a project with Docker, it is easy to set up and you do not mess up with a database. In order to install project this way you have to go through following steps:

### 0) Prepare your existing git repository 
Copy the content of this folder (except for 'exclude' and 'README.md') to your CRM repository (path/to/your/crm/, to the folder containing 'crm' and 'etc')
Copy the content of the 'exclude' file to your git exclude ```path/to/your/crm/.git/info/exclude```

### 1) Install docker and docker-compose

There is a great tutorial for this over there. Check it out: 
for docker (you may do only the first two steps): https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 
for docker-compose: https://docs.docker.com/compose/install/

### 2) Configure docker-compose.yml

The docker-compose.yml contains the volume and port sections:
```
                ports:
                        - 8300:8000
                volumes:
                        - .:/data
                        - /path/to/your/dump:/data/crm/dump
                        - /path/to/your/media:/data/crm/media
```

Change the port ```8300``` to whatever you like, this is the port your project will be using. Replace ```/path/to/your/dump``` and ```/path/to/your/media``` with the folders containing your media and dump for this project

### 3) Copy local settings

In the crm/dj/settings_local.py set the database settings (remove previous DB settings):
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}
```

### 4) How to use alias_cli.py

For your convenience, the file called alias_cli.py is created, it contains shortcuts for docker-compose commands so you don't have to worry about all the stuff behind it.

```
python alias_cli.py all - run commands in the following order: build, migrate, makemigrations, migrate, loaddata, changeadminpassword, runserver.
python alias_cli.py build - build the project (docker-compose build)
python alias_cli.py migrate - migrate all migrations
python alias_cli.py makemigrations - make migrations for all apps
python alias_cli.py loaddata - load data from xmls that are in the dump folder
python alias_cli.py createsuperuser - create super user
python alias_cli.py runserver - run the server
python alias_cli.py help - show some help about commands
python alias_cli.py changeadminpassword - change the admin password
python alias_cli.py removemigrations - remove all the migrations in the project
python alias_cli.py restartdb - restart the database
python alias_cli.py shell_plus - restart the database
```

### 5) Start building the project

```bash
python alias_cli.py all
```

### Hint: don't write always python alias_cli.py

If you don't want to write python alias_cli.py everytime you execute a command, you can make it a shortcut (replace /home/alexey/Documents/projects/crmdocker/crm/alias_cli.py with the absolute path to your alias_cli.py):
```bash
echo "\nalias crmcli='python /path/to/your/crm/alias_cli.py'" >> ~/.bashrc
```
now restart the terminal by writing bash
```bash
bash
```
Now you can just write
```bash
crmcli build
crmcli migrate
crmcli all
...
```
If you are using zsh:

```bash
"\nalias crmcli='python /path/to/your/crm/alias_cli.py'" >> ~/.zshrc
```
now restart the terminal by writing zsh
```bash
zsh
```
