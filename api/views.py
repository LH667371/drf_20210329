# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView

from api.models import User


class userAPIView(APIView):
    """
        DRF视图
    """

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        if user_id:
            user_obj = User.objects.get(pk=user_id)
            if user_obj:
                return JsonResponse({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'result': [{'username': user_obj.username, 'password': user_obj.password, 'gender': user_obj.get_gender_display()}],
                })
        else:
            user_obj_all = User.objects.all().values()
            if user_obj_all:
                return JsonResponse({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'result': list(user_obj_all),
                })
        return JsonResponse({
            'status': 500,
            'message': '查询的用户不存在',
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.create(username=username, password=password)
            return JsonResponse({
                'status': 201,
                'message': '创建单个用户成功',
                'results': {'username': user_obj.username, 'gender': user_obj.get_gender_display()}
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 500,
                'message': '新增单个用户失败',
            })
