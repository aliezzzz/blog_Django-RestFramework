import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', "send_type", "send_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
