from django.contrib import admin
from .models import Questions, Hints, ParadoxUser, Profile, ExeMembers, UserHintLevel, Referral, ExeGallery

# Register your models here.

admin.site.register([
    Questions,
    Hints,
    ParadoxUser,
    Profile,
    ExeMembers,
    UserHintLevel,
    Referral,
    ExeGallery
])
