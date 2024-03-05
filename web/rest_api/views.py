import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import TelegramUser, Tire
from admin_panel.models import CartItem, OrderItem, Order
from .serializers import (
    UserSerializer,
    TireSerializer,
    CartIDSerializer,
    CartSerializer,
    OrderSerializer,
)


def get_user_by_id(user_id: int) -> TelegramUser:
    """Fetch a TelegramUser by their user_id.

    Returns the TelegramUser instance if found.
    Raises TelegramUser.DoesNotExist if the user is not found.
    """
    return TelegramUser.objects.get(user_id=user_id)


class UserHandleApiView(APIView):
    """
    API view for handling user operations.

    Methods:
    - post: Create a new user.
    - get: Retrieve user information by user ID.
    """

    def post(self, request: Request):
        data = {
            "user_id": request.data.get("user_id"),
            "first_name": request.data.get("first_name"),
            "username": request.data.get("username"),
            "last_name": request.data.get("last_name"),
            "phone_number": request.data.get("phone_number"),
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok"}, status=status.HTTP_201_CREATED)

        return Response(
            {"status": "User wasn't created"}, status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request: Request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": e.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TireApiView(APIView):
    """
    API view for handling tire operations.

    Methods:
    - post: Create a new user.
    - get: Retrieve user information by user ID.
    """

    def get(self, request: Request):
        tier_id = request.data.get("tier_id")

        if not tier_id:
            return Response("tier_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            tire = Tire.objects.get(id=tier_id)
            serializer = TireSerializer(tire)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tire.DoesNotExist:
            return Response(
                {"error": "Tire not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)


class CartApiView(APIView):
    """
    API view for handling cart operations.

    Methods:
    - post: Create a new cart element.
    - get: Retrieve cart information by cart ID.
    - delete: Delete a cart by cart ID.
    """

    def post(self, request: Request):
        user_id = request.data.get("user_id")
        tire_id = request.data.get("tire_id")
        quantity = request.data.get("quantity", 1)

        if not user_id or not tire_id:
            return Response(
                {"error": "user_id and tire_id are required parameters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            tire = Tire.objects.get(tire_id=tire_id)
        except Tire.DoesNotExist:
            return Response(
                {"error": "tire wasn't found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response({"error": f"There was error: {e}"})

        data = {
            "user": user.pk,
            "tire": tire.pk,
            "quantity": quantity,
        }

        serializer = CartSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "cart_item was successfully added"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"status": "Cart Item wasn't added to the basket"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request: Request):
        cart_id = request.data.get("cart_id")

        if not cart_id:
            return Response("cart_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            cart = CartItem.objects.get(cart_id=cart_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request):
        pass


class CartItemsView(APIView):
    """
    A view for handling cart items related operations.

    Methods:
    - get: Retrieves the cart items for a given user.
    - delete: Deletes all cart items for a given user.
    """

    def get(self, request: Request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            cart_items = CartItem.objects.filter(user=user)
            serializer = CartIDSerializer(cart_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"There was error: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request: Request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            cart_items = CartItem.objects.filter(user=user)
            cart_items.delete()
            return Response(
                {"status": "cart_items was successfully deleted"},
                status=status.HTTP_200_OK,
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    """
    A view for handling order related operations.

    Methods:
    - get: Retrieves the order information for a given user.
    - post: Create the order for the specified user.
    - delete: Delete the order for the specified user.
    """

    def get(self, request: Request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id and cart_ids are required parameters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            order = Order.objects.filter(user=user)
            serializer = OrderSerializer(order)

            if order.is_valid():
                order.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response(
                {"error": "order doesn't exist"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request: Request):
        user_id = request.data.get("user_id")
        cart_ids = json.loads(request.data.get("cart_ids"))

        if not user_id or not cart_ids:
            return Response(
                {"error": "user_id and cart_ids are required parameters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = get_user_by_id(user_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"There was an error: {e.message}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            order = Order.objects.create(user=user)
        except Exception as e:
            return Response({"Error": f"There was error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            for cart_item in cart_ids:
                cart_id = cart_item.get("cart_id")
                cart = CartItem.objects.get(cart_id=cart_id)
                OrderItem.objects.create(
                    order=order, tire=cart.tire, quantity=cart.quantity
                )
                cart.delete()

            return Response(
                {"status": "order was successfully created"},
                status=status.HTTP_201_CREATED,
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "cart wasn't found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response({"error": f"There was error: {e}"})

    def delete(self, request: Request):
        pass
