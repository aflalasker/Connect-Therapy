from django.contrib import admin
from django.contrib.auth.models import Group

from connect_therapy.models import Practitioner


@admin.register(Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    first_name = lambda x: x.user.first_name
    first_name.short_description = "First Name"
    last_name = lambda x: x.user.last_name
    last_name.short_description = "Last Name"
    email = lambda x: x.user.email
    email.short_description = "Email"
    list_display = (first_name, last_name, email, 'is_approved')


admin.site.unregister(Group)
