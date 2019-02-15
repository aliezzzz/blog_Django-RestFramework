from django.shortcuts import render

# Create your views here.
from random import choice
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from django.core.mail import send_mail

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from .serializers import EmailSerializer, RegisterSerializer
from .models import EmailVerifyRecord
from blog.settings import DEFAULT_FORM_EMAIL

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义登录验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class EmailCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送邮箱验证码
    """
    serializer_class = EmailSerializer

    def send_verify_email(self, code, email):
        title = "邮箱验证码Test"
        msg = "验证码：" + str(code)
        email_from = DEFAULT_FORM_EMAIL
        receiver = [email]
        return send_mail(title, msg, email_from, receiver)

    def generate_code(self):
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        code = self.generate_code()
        try:
            self.send_verify_email(code, email)
        except Exception as e:
            return Response({
                "status": False
            }, status=status.HTTP_400_BAD_REQUEST)

        code_record = EmailVerifyRecord(code=code, email=email)
        code_record.save()
        return Response({
            "status": True
        }, status=status.HTTP_201_CREATED)


class RegisterViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)  # 生成payload
        re_dict["token"] = jwt_encode_handler(payload)  # 解码payload生成token

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
