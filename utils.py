from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin
def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('66556B524E69394455786E5A505158455A3066692F587865744C30313556794A2F3632334E78524D69316B3D')
        params = {
            'sender': '10008663',
            'receptor': phone_number,
            'message': f'online shop: your verify code is {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin