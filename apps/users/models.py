import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, null=True, blank=True, editable=False)
    username = models.CharField(max_length=30, default='', unique=True, verbose_name="用户名")
    email = models.CharField(max_length=50, verbose_name="邮箱")
    avatar = models.ImageField(upload_to="users/images/", null=True, blank=True, verbose_name="头像",
                               help_text="头像")
    is_subcribe = models.BooleanField(default=False, blank=True, verbose_name="是否订阅通知邮件", help_text="除验证码通知邮件外的通知邮件")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码
    """
    CODE_TYPE = (
        ("register", "注册"),
        ("forget", "找回密码"),
        ("update_email", "修改邮箱"),
        ("comment", "评论")
    )

    code = models.CharField(max_length=20, verbose_name="验证码", help_text="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱", help_text="邮箱")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="发送时间", help_text="发送时间")
    send_type = models.CharField(max_length=15, choices=CODE_TYPE, null=True, verbose_name="验证码类型", help_text="验证码类型")
    is_active = models.BooleanField(default=True, verbose_name="验证码状态", help_text="验证码状态")

    def __str__(self):
        return '{0} [{1}]'.format(self.code, self.email)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name