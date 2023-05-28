import base64
import binascii
import re


def extract_verification_code_from_email(email_body):
    start_index = email_body.find("account-confirm-email/") + len(
        "account-confirm-email/"
    )
    end_index = email_body.find("/", start_index)
    verification_code = email_body[start_index:end_index].strip()
    return verification_code





def extract_username_and_verification_code_from_email(email_body):
    url_pattern = r"http://testserver/api/v1/auth/password-reset/confirm/(?P<uidb64>[^/]+)/(?P<code>[^/\n]+)/"
    match = re.search(url_pattern, email_body)
    if match:
        uidb64 = match.group("uidb64")
        code = match.group("code")
        return uidb64, code
        
        # Decode uidb64 using urlsafe_base64_decode
    #     try:
    #         uid = urlsafe_base64_decode(uidb64).decode()
    #     except (TypeError, ValueError):
    #         uid = None
    #     print("uid: ", uid, "code: ", code)
    # else:
    #     uid = None
    #     code = None
    # return uid, code

