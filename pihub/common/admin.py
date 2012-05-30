from django.conf import settings

if "kombu.transport.django" in settings.INSTALLED_APPS:
    from kombu.transport.django.models import Message, Queue
    from django.contrib import admin
    
    admin.site.register(Message)
    admin.site.register(Queue)
