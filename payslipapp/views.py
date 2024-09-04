# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payslip
from .serializers import PayslipSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from rest_framework.decorators import api_view


class PayslipListView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PayslipSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = request.FILES.get('pdf_file', None)
            if pdf_file:
                serializer.save(pdf_file=pdf_file)
            else:
                serializer.save()

            return Response({'status': 'success', 'message': 'Data posted successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Error posting data'}, status=status.HTTP_400_BAD_REQUEST)



# views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status

@csrf_exempt
@api_view(['GET'])
def save_pdf(request, payslip_id):
    try:
        payslip = Payslip.objects.get(id=payslip_id)
        if payslip.pdf_file:
            with open(payslip.pdf_file.path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{payslip.pdf_file.name}"'
                return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Payslip has no associated PDF file'}, status=status.HTTP_404_NOT_FOUND)
    except Payslip.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Payslip not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"Exception: {e}")
        return JsonResponse({'status': 'error', 'message': 'Error processing PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

