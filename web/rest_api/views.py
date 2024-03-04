from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import TelegramUser, Tire
from .serializers import UserSerializer, TireSerializer


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

        return Response({"status": "User wasn't created"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response("user_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = TelegramUser.objects.get(user_id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TelegramUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)       


class TireApiView(APIView):
    """
    API view for retrieving tire information.
    
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
            return Response({"error": "Tire not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)


class CartApiView(APIView):
    def post(self, request: Request):
        pass

