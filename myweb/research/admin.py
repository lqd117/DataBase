from django.contrib import admin

from .models import User, System_log, Reporter_information, Research_projects, Award_information, \
    Question_identification, Academic_events, Scientific_Papers, Book, Patent

admin.site.register(User)
admin.site.register(System_log)
admin.site.register(Reporter_information)
admin.site.register(Research_projects)
admin.site.register(Award_information)
admin.site.register(Question_identification)
admin.site.register(Academic_events)
admin.site.register(Scientific_Papers)
admin.site.register(Book)
admin.site.register(Patent)
