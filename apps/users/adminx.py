import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', "send_type", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
