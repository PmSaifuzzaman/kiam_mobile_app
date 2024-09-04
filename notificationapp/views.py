from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification

class NotificationListView(APIView):
    def get(self, request):
        notifications = Notification.objects.all().order_by('-created_at')[:10]
        data = [{'message': notification.message, 'created_at': notification.created_at} for notification in notifications]
        return Response(data)
