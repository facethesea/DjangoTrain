from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BaseInfo(APIView):
    def get(self,request):
        print(request.query_params)

        ret={'cod':100,'message':'Insert a student successfully'}
        return Response(ret)

    def post(self,request):
        print(request.data)
        ret={'cod':100,'message':'到达 a student successfully'}
        return Response(ret)

  