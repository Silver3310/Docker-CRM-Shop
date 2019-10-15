"""
Make migrations for all the applications in the project
"""
import os
from subprocess import call


if __name__ == '__main__':
    dir_path = os.getcwd()

    for i in os.listdir(dir_path + '/crm'):
        if os.path.isdir(os.path.join(dir_path + '/crm', i)):
            print(i)
            call([
                'python',
                '%s/manage.py' % (dir_path + '/crm'),
                'makemigrations',
                '%s' % (i),
                ])

