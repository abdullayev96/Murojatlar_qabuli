from django.contrib import admin
from .models import *


# class TestAdmin(admin.ModelAdmin):
#     list_display = ("id", "id_number", "file", "posted_at")
#     list_display_links = ("id", "id_number")
#     search_fields = ("id_number", "posted_at")



admin.site.register(User)
admin.site.register(User_test)
admin.site.register(Comment)
admin.site.register(Murojat)
#admin.site.register(Information)
admin.site.register(About)
admin.site.register(New)

# admin.site.register(Test_result, TestAdmin)

