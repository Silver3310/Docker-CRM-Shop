import sys
import os

import django

projecthome = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if projecthome not in sys.path:
    sys.path.append(projecthome)

sys.path.append('/data/shop')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()

import django.apps
from django.db.models import ImageField, FileField

IMAGE_LOCATION = '/data/shop/media/sample.jpg'


for model in django.apps.apps.get_models():
    for field in model._meta.get_fields():
        if isinstance(field, ImageField) or isinstance(field, FileField):
            model_file_field = str(field).split('.')[-1]
            for obj in model.objects.all():
                getattr(obj, model_file_field).save(
                    IMAGE_LOCATION,
                    open(IMAGE_LOCATION, 'rb')
                )
                obj.save()
