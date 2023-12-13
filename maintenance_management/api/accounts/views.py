import base64

import jwt
import datetime
from decouple import config
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from maintenance_management.accounts.models import AppUserProfile
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

        return response


class LogoutUser(APIView):
    def post(self, request):
        response = Response()
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
            print(data)
            if data["file"] is None:
                profile.file = None
            else:
                image_as_string = data["file"]
                file_name = data["filename"]
                extension = data["extension"]
                try:
                    image_data = base64.b64decode(image_as_string)
                    profile.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
                except Exception as error:
                    print(error)
                    return HttpResponse(status=400)

            profile.first_name = data.get("first_name", profile.first_name)
            profile.last_name = data.get("last_name", profile.last_name)
            profile.phone_number = data.get("phone_number", profile.phone_number)
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


@api_view(["POST"])
@csrf_exempt
def test_authentication(request):
    token = request.data["token"]
    response = HttpResponse()
    try:
        info = jwt.decode(jwt=token, key=config("JWT_SECRET"), algorithms=["HS256"])
        user = UserModel.objects.get(pk=info["id"])
        if not user:
            response.status_code = 400
            return response
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        response.status_code = 403
        return response
