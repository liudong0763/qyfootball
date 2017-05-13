from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team

# Register your models here.


class MyUserAdmin(UserAdmin):
    list_display = ('username', )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader_name', )

    def leader_name(self, obj):
        # print(obj.leader.values_list('username', flat=True))
        return obj.leader.values_list('username').get()

    leader_name.short_description = '领队'

admin.site.register(User,MyUserAdmin)
admin.site.register(Team,TeamAdmin)
