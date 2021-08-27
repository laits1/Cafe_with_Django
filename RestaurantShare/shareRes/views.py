from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request) :
    # 기존에 입력되어 있는 (혹은 새로 입력한) 카테고리 내용을 DB에서 select 함
    categories = Category.objects.all() # select 진행 후 결과 반환
    restaurant = Restaurant.objects.all()
    # rendering에 사용할 dict로 구성
    content = {'categories' : categories,
                'restaurants' : restaurants}

    # 구성된 dict를 rendering에 사용하도록 전달

    return render(request, 'shareRes/index.html', content)
    # return HttpResponse('index')

def Create_restaurant(request) :
    # 외래키로 연결된 카테고리컬럼은 저장을 일반 값이 아닌 해당카테고리 레코드의 인스턴스를 넘겨줘야함
    
    category_id = request.POST['resCategory']

    category = Category.object.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link,
                         restaurant_content = content, restaurant_keyword = keyword)
    new_res.save() # DB저장
    # 저장된 결과를 출력하기 위해 index.html 파일을 요청
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('맛집 DB 저장합니다')

def restaurantDetail(request) :
    # return HttpResponse('restaurantDetail')
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request) :
    # return HttpResponse('restaurantCreate')
    categories = Category.objects.all()
    content = {'categories': categories}

    return render(request, 'shareRes/restaurantCreate.html', content)

def categoryCreate(request) :

    categories = Category.objects.all() # categories 변수에는 Category 테이블의 모든 레코드를 반환받아서 저장
    # Category  테이블 컬럼 : id , category_name

    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content) 

    # return HttpResponse('categoryCreate')
    

def Delete_category(request) :
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

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
