

def extract_verification_code_from_email(email_body):
    start_index = email_body.find("account-confirm-email/") + len(
        "account-confirm-email/"
    )
    end_index = email_body.find("/", start_index)
    verification_code = email_body[start_index:end_index].strip()
    return verification_code
