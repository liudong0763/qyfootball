from django.contrib import admin
from .models import User,Team

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'last_login', 'phone', 'is_active')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'leader_name')

	def leader_name(self, obj):
		# print(obj.leader.values_list('username', flat=True))
		return obj.leader.values_list('username').get()
		
	leader_name.short_description = '领队'

admin.site.register(User,UserAdmin)
admin.site.register(Team,TeamAdmin)
