from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request) :
    # 기존에 입력되어 있는 (혹은 새로 입력한) 카테고리 내용을 DB에서 select 함
    categories = Category.objects.all() # select 진행 후 결과 반환

    # rendering에 사용할 dict로 구성
    content = {'categories' : categories}

    # 구성된 dict를 rendering에 사용하도록 전달

    return render(request, 'shareRes/index.html', content)
    # return HttpResponse('index')
    
def restaurantDetail(request) :
    # return HttpResponse('restaurantDetail')
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request) :
    # return HttpResponse('restaurantCreate')
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request) :
    # return HttpResponse('categoryCreate')
    return render(request, 'shareRes/categoryCreate.html')

def Create_category(request) :
    # 사용자가 입력한 카테고리 data를 추출해서 DB에 저장
    # 1. 사용자가 입력한 카테고리 Data를 추출(post 방식으로 서버에 전송됨)
    category_name = request.POST['categoryName']
    # 2. 추출 Data DB에 저장
    new_category = Category(category_name = category_name)
    new_category.save()

    # DB 저장 완료 후 index.html 파일을 재 요청
    return HttpResponseRedirect(reverse('index')) # index url (기본페이지 요청)
    # return HttpResponse("여기서 카테고리 저장을 구현합니다.")
