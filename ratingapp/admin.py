from django.contrib import admin
from .models import Profile,Project,rating_content_object,rating_design_object,rating_usability_object



admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(rating_content_object)
admin.site.register(rating_design_object)
admin.site.register(rating_usability_object)