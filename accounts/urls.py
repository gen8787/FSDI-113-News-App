from django.urls import path
from .views import *

urlpatterns = [
    # S I G N U P
    path("signup/", SignupView.as_view(), name="signup"),
    # H O M E

    # C R E A T E

    # R E A D

    # U P D A T E

    # D E L E T E

    # O T H E R

]
