from django.http import JsonResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from rest_framework.viewsets import ModelViewSet

import requests
from lxml import etree

from .models import Waste
from .serializers import WasteSerializer
from category.models import Category


# Create your views here.


class WasteView(ModelViewSet):
    queryset = Waste.objects.all()
    serializer_class = WasteSerializer


def search(request, waste_name):
    try:
        # 从数据库查询 waste 数据和 category 数据
        waste = Waste.objects.get(waste_name=waste_name)
        category = Category.objects.get(id=waste.category_id)
    except Waste.DoesNotExist:
        # 如果数据库没有数据, 使用 requests 爬取数据
        headers = {'user-agent': 'Mozilla/5.0', 'cookie': ''}
        url = 'https://lajifenleiapp.com/sk/' + waste_name
        html = requests.get(url, headers=headers).text
        etree_html = etree.HTML(html)
        category_name = etree_html.xpath("//span[@style='#2e2a2b']/text()")[0]
        print('requests: ' + waste_name + ' --> ' + category_name)
        category = Category.objects.get(category_name=category_name)
        # 将爬取到的数据保存到数据库
        waste = Waste(
            waste_name=waste_name,
            category_id=category.id,
            create_time=datetime.now(),
        )
        waste.save()

    # 封装返回结果
    result = {
        'id': waste.id,
        'waste_name': waste.waste_name,
        'image': waste.image,
        'category_id': waste.category_id,
        'create_time': waste.create_time,
        'category_name': category.category_name,
        'icon': category.icon,
        'description': category.description,
        'regulation': category.regulation,
        'include': category.include,
    }
    return JsonResponse(result)
