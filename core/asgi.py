import os
from django.core.asgi import get_asgi_application
from channels.routing import PtotocolTypeRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = PtotocolTypeRouter({
  'http': get_asgi_application()
})
