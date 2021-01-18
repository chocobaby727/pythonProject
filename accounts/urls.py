from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

CACHE_TIMEOUT = 60 * 60 * 3

app_name = 'accounts'
urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("signup/validate_user_name_ajax/", views.ValidateUsernameAjaxView.as_view(), name="validate_user_name_ajax"),
    path("signup/validate_email_ajax/", views.ValidateEmailAjaxView.as_view(), name="validate_email_ajax"),
    # path("signup/validate_user_name_ajax/", cache_page(CACHE_TIMEOUT)(views.ValidateUsernameAjaxView.as_view()), name="validate_user_name_ajax"),
    # path("signup/validate_email_ajax/", cache_page(CACHE_TIMEOUT)(views.ValidateEmailAjaxView.as_view()), name="validate_email_ajax"),
]
