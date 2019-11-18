from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache

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


class Redis(APIView):

    def get(self, request, *args, **kwargs):
        key = request.query_params.get('key')
        if not key:
            print('*')
            # key is null, to list all key
            res = cache.keys("*")
            return Response(data=res)
        else:
            print('is not *'+key)
            # key is not null, get key value
            res = cache.get(key)
            print(res)
        return Response(data={"key": key, "val": res})

    def post(self, request, *args, **kwargs):
        key = request.data.get('key')
        val = request.data.get('val')
        res = cache.set(key, val)
        if res:
            return Response(data="set yes")
        else:
            return Response(data="set error")

    def delete(self, request, *args, **kwargs):
        # delete all key

        res = cache.delete_pattern("*")
        return Response(data={"delete_conunt": res})
