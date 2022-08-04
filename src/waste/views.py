from django.http import JsonResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from rest_framework.viewsets import ModelViewSet

import requests
from lxml import etree

from .models import Waste
from .serializers import WasteSerializer
from classification.models import Classification


# Create your views here.


class WasteView(ModelViewSet):
    queryset = Waste.objects.all()
    serializer_class = WasteSerializer


def search(request, waste_name):
    try:
        # 从数据库查询 waste 数据和 classification 数据
        waste = Waste.objects.get(waste_name=waste_name)
        classification = Classification.objects.get(id=waste.classification_id)
    except Waste.DoesNotExist:
        # 如果数据库没有数据, 使用 requests 爬取数据
        headers = {'user-agent': 'Mozilla/5.0', 'cookie': ''}
        url = 'https://lajifenleiapp.com/sk/' + waste_name
        html = requests.get(url, headers=headers).text
        etree_html = etree.HTML(html)
        classification_name = etree_html.xpath("//span[@style='#2e2a2b']/text()")[0]
        print('requests: ' + waste_name + ' --> ' + classification_name)
        classification = Classification.objects.get(classification_name=classification_name)
        # 将爬取到的数据保存到数据库
        waste = Waste(
            waste_name=waste_name,
            classification_id=classification.id,
            create_time=datetime.now(),
        )
        waste.save()

    # 封装返回结果
    result = {
        'id': waste.id,
        'waste_name': waste.waste_name,
        'image': waste.image,
        'classification_id': waste.classification_id,
        'create_time': waste.create_time,
        'classification_name': classification.classification_name,
        'icon': classification.icon,
        'description': classification.description,
        'regulation': classification.regulation,
        'include': classification.include,
    }
    return JsonResponse(result)
