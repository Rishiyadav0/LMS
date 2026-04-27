from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication to gracefully handle Swagger UI cases where 
    users provide just the token without the 'Bearer ' prefix.
    """
    def get_header(self, request):
        header = super().get_header(request)
        if header:
            # If the header doesn't contain a space, assume they just pasted the token
            # without the 'Bearer ' prefix (common in Swagger UI).
            if b' ' not in header:
                # Add the 'Bearer ' prefix so it passes the default JWTAuthentication checks
                header = b'Bearer ' + header
        return header
