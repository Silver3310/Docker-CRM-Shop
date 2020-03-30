"""
Aliases for the shop project
"""

import sys
from subprocess import call


def build():
    # build the project
    call('docker-compose -f local.yml build'.split())


def migrate():
    # migrate  migrations
    call('docker-compose -f local.yml run --rm web python shop/manage.py migrate'.split())


def make_migrations():
    # make migrations
    call('docker-compose -f local.yml run --rm web python shop/manage.py makemigrations'.split())


def load_data():
    # load data
    call('docker-compose -f local.yml run --rm web python loaddata.py'.split())


def create_super_user():
    # create super user
    call('docker-compose -f local.yml run --rm web python shop/manage.py createsuperuser'.split())


def run_server():
    # run server
    call('docker-compose -f local.yml up'.split())


def restart_db():
    # restart db
    call('docker-compose -f local.yml stop db'.split())
    call('docker-compose -f local.yml rm db'.split())


def remove_migrations():
    # remove migrations
    call('docker-compose -f local.yml run --rm web find . -path "./shop/*/migrations/*.py" -not -name "__init__.py" -delete'.split())


def change_admin_password():
    # change admin password
    call('docker-compose -f local.yml run --rm web python shop/manage.py changepassword admin'.split())


def make_apps_migrations():
    # make migrations for all apps
    call('docker-compose -f local.yml run --rm web python makeappsmigrations.py'.split())


def remove_images():
    # remove images for all apps
    call('docker-compose -f local.yml run --rm web python remove_images.py'.split())


def shell_plus():
    # shell plus
    call('docker-compose -f local.yml run --rm web python shop/manage.py shell_plus'.split())


def show_help():
    # show help
    print(
        """\n        python alias_cli.py build - build the project (docker-compose build)\n
        python alias_cli.py migrate - migrate all migrations\n
        python alias_cli.py makeappsmigrations - make migrations for all apps\n
        python alias_cli.py makemigrations - make migrations\n
        python alias_cli.py loaddata - load data from xmls that are in the dump folder\n
        python alias_cli.py createsuperuser - create super user\n
        python alias_cli.py runserver - run the server\n
        python alias_cli.py help - show some help about commands\n
        python alias_cli.py all - run commands in the following order: build, migrate, makemigrations, migrate, loaddata, changeadminpassword, runserver.\n 
        python alias_cli.py changeadminpassword - change the admin password\n
        python alias_cli.py removemigrations - remove all the migrations in the project\n
        python alias_cli.py restartdb - restart the database\n
        python alias_cli.py shell_plus - restart the database\n
        """
    )


if __name__ == "__main__":
    command = sys.argv[1]

    if command == 'build':
        # build the project
        build()

    elif command == 'migrate':
        # migrate  migrations
        migrate()

    elif command == 'makemigrations':
        # make migrations for all apps
        make_migrations()

    elif command == 'loaddata':
        # load data
        load_data()

    elif command == 'createsuperuser':
        # create super user
        create_super_user()

    elif command == 'runserver':
        # run the project
        run_server()

    elif command == 'changeadminpassword':
        # change admin password
        change_admin_password()

    elif command == 'removemigrations':
        # remove migrations
        remove_migrations()

    elif command == 'restartdb':
        # restart the database
        restart_db()

    elif command == 'help' or command == '--help' or command == '-h':
        # show help
        show_help()

    elif command == "shell_plus":
        # shell plus
        shell_plus()

    elif command == "makeappsmigrations":
        # make apps migrations
        make_apps_migrations()

    elif command == "removeimages":
        # remove images
        remove_images()

    elif command == 'all':
        # run all commands to start a project
        build()
        migrate()
        make_apps_migrations()
        migrate()
        load_data()
        remove_images()
        change_admin_password()
        run_server()

