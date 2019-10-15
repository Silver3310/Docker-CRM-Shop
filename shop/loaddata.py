"""
Load all the xmls
"""
import os
from subprocess import call
from subprocess import check_output


if __name__ == '__main__':

    dir_path = os.getcwd()

    na_dump_dir_path = dir_path + '/shop/dump'

    res = check_output([
        'python',
        '%s/shop/dumpapp/sort_app_models.py' % dir_path,
        na_dump_dir_path
    ])
    # print(res)
    res = res.decode('utf-8')
    # print(res)
    app_list = res.split(':')
    print(app_list)

    for i in app_list:
        # print(i)
        xml_file_path = os.path.join(na_dump_dir_path, '%s.xml' % (i))
        # print(xml_file_path)
        call([
            'python3',
            '%s/shop/manage.py' % dir_path,
            'loaddata',
            '-v', '3',
            '--format=xml',
            xml_file_path,
        ])

