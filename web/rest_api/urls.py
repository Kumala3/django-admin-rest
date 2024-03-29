from django.urls import path

from .views import UserHandleApiView, TireApiView, CartApiView, CartItemsView, OrderView

urlpatterns = [
    path("user/", UserHandleApiView.as_view()),
    path("tire/", TireApiView.as_view()),
    path("cart/", CartApiView.as_view()),
    path("cart_items/", CartItemsView.as_view()),
    path("order/", OrderView.as_view()),
]
