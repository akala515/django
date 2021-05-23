from django.shortcuts import render, redirect

# Create your views here.

import random

from app_data.models import DataForm


# lst = []
# for i in range(20):
#     lst.append(DataForm(name=random.randint(0, 1000), position=random.randint(0, 1000), types=random.randint(0, 1000),date='2021-05-22'))
# DataForm.objects.bulk_create(lst)


def index(request):
    # 查询所有数据
    data_list = DataForm.objects.all()
    return render(request, 'app_data/home.html', locals())


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        date = request.POST.get('date')
        types = request.POST.get('types')
        date = date[:4] + '-' + date[4:6] + '-' + date[6:]
        DataForm.objects.create(name=name, position=position, date=date, types=types)
        return redirect('/')
    return render(request, 'app_data/add.html')


def update(request):
    # get请求 返回这条数据
    id = request.GET.get('id')
    data_obj = DataForm.objects.filter(id=id).first()
    # post请求 更新数据
    if request.method == 'POST':
        id = request.GET.get('id')
        name = request.POST.get('name')
        position = request.POST.get('position')
        date = request.POST.get('date')
        types = request.POST.get('types')
        date = date[:4] + '-' + date[4:6] + '-' + date[6:]
        # 更新对应 id 的数据
        DataForm.objects.filter(id=id).update(name=name, position=position, date=date, types=types)
        return redirect('/')
    return render(request, 'app_data/update.html', locals())


def delete(request):
    # 获取id 删除这条数据
    id = request.GET.get('id')
    DataForm.objects.get(id=id).delete()
    return redirect('/')


def search(request):
    if request.method == 'POST':
        data = {}
        # 获取 名称， 位置，时间，类型
        name = request.POST.get('searchname', '')
        if name:
            data['name'] = name
        position = request.POST.get('searchposition', '')
        if position:
            data['position'] = position
        date = request.POST.get('searchdate', '')
        if date:
            date = date[:4] + '-' + date[4:6] + '-' + date[6:]
            data['date'] = date
        types = request.POST.get('searchtypes', '')
        if types:
            data['types'] = types
        # 查找相应的数据
        data_list = DataForm.objects.filter(**data)
        return render(request, 'app_data/home.html', locals())
