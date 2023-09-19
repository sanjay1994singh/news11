# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news11.settings')
#
# application = get_wsgi_application()



import os
from static_ranges import Ranges
from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news11.settings')


application = Ranges(Cling(MediaCling(get_wsgi_application())))
