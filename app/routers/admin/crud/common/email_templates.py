def forgot_password(name: str, otp: str):
    html = """
<html>
    <body>
        <p>Hi ###NAME###, your OTP for password reset is ###OTP### and It's valid for 10 minutes.<p>
    </body>
</html>
    """
    html = html.replace("###NAME###", name)
    html = html.replace("###OTP###", otp)
    return html
