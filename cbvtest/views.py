from rest_framework.views import APIView
from rest_framework.response import Response

redata = {
    'code': 1000,
    'msg': 'test',
    'data': '', }


class Apple(APIView):

    def get(self, request, *args, **kwargs):
        redata.update({'data': 'is '+request.method})
        return Response(data=redata)

    def post(self, request, *args, **kwargs):
        redata.update({'data': 'is '+request.method})
        return Response(data=redata)


class Sydney(APIView):
    def get(self, request, *args, **kwargs):
        redata.update({'data': 'is '+request.method})
        return Response(data=redata)
