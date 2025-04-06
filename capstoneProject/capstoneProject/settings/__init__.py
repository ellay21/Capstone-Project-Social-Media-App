from split_settings.tools import include
from decouple import config
include('base.py')

if 'dev'== config('DJANGO_ENV'):
    include('dev.py')
elif 'prod'== config('DJANGO_ENV'):
    include('prod.py')