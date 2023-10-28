from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.views import View


# Create your views here.
def auth(request):
    return JsonResponse({'status': True, 'message': 'success'})


# @api_view(["GET"])
# def login(requests):
#     return Response({'status': True, 'message': 'success'})
class UserView(View):
    def get(self, request):
        return JsonResponse({'status': True, 'message': 'success'})

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
