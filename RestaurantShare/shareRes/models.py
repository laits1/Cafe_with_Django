from django.db import models

# Create your models here.
class Category(models.Model) :
    category_name = models.CharField(max_length=100)
    # varChar(100) 인 컬럼 category_name 이 테이블 추가
    # 기본키 필드 명시가 없으면 자동으로 생성
