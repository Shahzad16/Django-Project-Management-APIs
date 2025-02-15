from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Project, Task

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Role", {"fields": ("role",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role", "is_staff", "is_active")}
        ),
    )
    search_fields = ("username", "email")
    ordering = ("username",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','description','creator']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','description','status','project']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
