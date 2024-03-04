from django.urls import path

from .views import UserHandleApiView, TireApiView, CartApiView

urlpatterns = [
    path("create_user/", UserHandleApiView.as_view()),
    path("tire/", TireApiView.as_view()),
    path("cart/", CartApiView.as_view()),
]
