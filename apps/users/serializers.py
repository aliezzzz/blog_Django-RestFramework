import re
from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import EmailVerifyRecord, UserProfile

User = get_user_model()
REGEX_EMAIL = "^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$"


class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)

    def validate_email(self, email):
        """
        验证邮箱
        """

        # 验证邮箱是否存在
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证邮箱是否合法
        if not re.match(REGEX_EMAIL, email):
            raise serializers.ValidationError("邮箱格式错误")

        # 验证频率限制
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if EmailVerifyRecord.objects.filter(add_time__gt=one_minutes_ago, email=email).count():
            raise serializers.ValidationError("1分钟只能发送一次")

        return email


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, min_length=1, required=True, label='用户名')
    email = serializers.EmailField(required=True, label='邮箱')
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4)
    password = serializers.CharField(required=True, write_only=True, style={'input-type': 'password'})

    # def create(self, validated_data):
    #     user = super(RegisterSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        verify_records = EmailVerifyRecord.objects.filter(email=self.initial_data["email"]).order_by("-add_time")
        if verify_records:
            last_records = verify_records[0]
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=59, seconds=0)
            if not last_records.is_active:
                raise serializers.ValidationError("验证码已使用")
            if five_minutes_ago > last_records.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_records.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码未发送")
        last_records.is_active = False
        last_records.save()
        return code

    def validate(self, attrs):
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'email', 'code', 'password')
