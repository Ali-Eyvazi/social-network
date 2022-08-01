from django.contrib import admin

# Register your models here.
from .models import Relation,UserDetails
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from django.contrib.auth.models import User


class UserDetailInline(admin.StackedInline):
    model=UserDetails
    can_delete=False

class ExtendedUserAdmin(BaseUSerAdmin):
    inlines=(UserDetailInline,)



admin.site.unregister(User)
admin.site.register(User,ExtendedUserAdmin)

admin.site.register(Relation)


