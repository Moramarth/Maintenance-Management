import jwt
import datetime
from decouple import config

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from maintenance_management.accounts.models import AppUserProfile, AppUser
from maintenance_management.api.accounts.serializers import ProfileSerializer, AppUserSerializer
from maintenance_management.settings import SESSION_COOKIE_AGE

UserModel = get_user_model()


class LoginUser(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = UserModel.objects.get(email=email)

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        token_payload = {
            "id": user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=SESSION_COOKIE_AGE),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(token_payload, config('JWT_SECRET'), algorithm='HS256')
        response = Response({
            "jwt": token,
            "user_id": user.id,
        })

        response.set_cookie(key="jwt", value=token, httponly=True,
                            expires=datetime.datetime.utcnow() + datetime.timedelta(seconds=SESSION_COOKIE_AGE))

        return response


class LogoutUser(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message": "Logged out successfully"
        }
        return response


@api_view(["GET"])
@csrf_exempt
def get_all_profiles(request):
    profiles = AppUserProfile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PATCH"])
@csrf_exempt
def get_profile_by_id(request, pk):
    if request.method == "GET":
        profile = get_object_or_404(AppUserProfile, pk=pk)
        if profile:
            serializer = ProfileSerializer(profile)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "PATCH":
        profile = get_object_or_404(AppUserProfile, pk=pk)
        if profile:
            data = request.data
            profile.first_name = data.get("first_name", profile.first_name)
            profile.last_name = data.get("last_name", profile.last_name)
            profile.phone_number = data.get("phone_number", profile.phone_number)
            profile.file = data.get("file", profile.file)
            profile.save()
            return JsonResponse({"call was successful": "asd"})


@api_view(["GET"])
@csrf_exempt
def get_user_by_id(request, pk):
    user = get_object_or_404(UserModel, pk=pk)
    if user:
        serializer = AppUserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    return
