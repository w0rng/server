from apps.user.models import User
from rest_framework.response import Response


def auth(get_response):
    def middleware(request):
        user_token = request.GET.get("token")

        if not user_token:
            return get_response(request)

        user = User.objects.filter(token=user_token).first()

        if not user:
            return Response({'error': 'user not found'}, 405)
        if user.banned:
            Response({'error': 'you are banned'}, 405)
        
        request.student = user
    
        return get_response(request)

    return middleware
