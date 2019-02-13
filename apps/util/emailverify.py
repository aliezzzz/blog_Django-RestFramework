# from django.core.mail import send_mail, send_mass_mail
#
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.qq.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = "504141280@qq.com"
# EMAIL_HOST_PASSWORD = "gotqagxeqrbqcaha"
# DEFAULT_FORM_EMAIL = EMAIL_HOST_USER
#
# class EmailVerify(object):
#
#     def send_verify_email(self, code, email):
#         title = "邮箱验证码Test"
#         msg = "验证码：" + str(code)
#         email_from = DEFAULT_FORM_EMAIL
#         receiver = [email]
#
#         send_mail(title, msg, email_from, receiver)
