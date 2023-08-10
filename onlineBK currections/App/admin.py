from django.contrib import admin
from . models import Users, Sender, Message, Receiver, Transfer
# Register your models here.

admin.site.register(Users)
admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(Message)
admin.site.register(Transfer)
