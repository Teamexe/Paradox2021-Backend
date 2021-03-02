from rest_framework.urls import path
from .views import UserView, LeaderBoardView, ProfileDetailsView, QuestionView, \
    HintsView, ReferralView, ExeMemberView, ExeMemberPositionsView, \
    UpdateUserCoinsView, UserPresentView, CheckAnswerView, AvailHintsView, stats

urlpatterns = [
    path('user/', UserView.as_view()),
    path('leaderboard/', LeaderBoardView.as_view()),
    path('userProfile/<str:google_id>/', ProfileDetailsView.as_view()),
    path('questions/', QuestionView.as_view()),
    path('hints/', HintsView.as_view()),
    path('refferral/', ReferralView.as_view()),
    path('exe-members/', ExeMemberView.as_view()),
    path('exe-members-positions/', ExeMemberPositionsView.as_view()),
    path('update-coins/', UpdateUserCoinsView.as_view()),
    path('user-present-or-not/<str:google_id>/', UserPresentView.as_view()),
    path('check-answer/', CheckAnswerView.as_view()),
    path('avail-hints/', AvailHintsView.as_view()),
    path('stats/', stats)
]
