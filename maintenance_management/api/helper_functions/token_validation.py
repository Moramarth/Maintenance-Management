import jwt
from decouple import config
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def validate_token(request_data):
    status_code = None
    user = None
    try:
        token = request_data["token"]
        info = jwt.decode(jwt=token, key=config("JWT_SECRET"), algorithms=["HS256"])
        user = UserModel.objects.get(pk=info["id"])
        if not user:
            status_code = 400
            return user, status_code
        return user, status_code
    except Exception as e:
        status_code = 403
        return user, status_code
