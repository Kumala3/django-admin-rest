from django.urls import path

from .views import UserHandleApiView

urlpatterns = [
    path("create_user/", UserHandleApiView.as_view()),
]
