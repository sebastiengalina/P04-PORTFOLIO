from django.contrib import admin

from models import Project
from models import ProjectBlock
from models import Tag


class TagInline(admin.TabularInline):
    model = Tag
    extra = 3


class ProjectBlockInline(admin.StackedInline):
    model = ProjectBlock
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectBlockInline]
admin.site.register(Project, ProjectAdmin)


admin.site.register(ProjectBlock)
admin.site.register(Tag)
