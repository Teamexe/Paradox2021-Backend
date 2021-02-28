from django.contrib import admin
from .models import Questions, Hints, ParadoxUser, Profile, ExeMembers

# Register your models here.

admin.site.register([
    Questions,
    Hints,
    ParadoxUser,
    Profile,
    ExeMembers
])
