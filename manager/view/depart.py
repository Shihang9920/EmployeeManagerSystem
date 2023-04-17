from django.http import HttpResponse, JsonResponse
from manager.models import Department
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


def depart_list(request):
    # 查询所有的部门
    depart = Department.objects.all()
    return render(request, 'department.html', {"depart": depart})


def depart_add(request):
    # 获取post请求中的title字段
    title = request.POST.get("depart")
    # 添加到数据库
    Department.objects.create(title=title)
    return redirect('/depart/list')


def depart_delete(request):
    # 获取get请求的nid参数
    nid = request.GET.get('nid')
    # 从数据库中删除
    Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


@csrf_exempt
def depart_edit(request):
    nid = request.GET.get('id')
    if request.method == 'GET':
        depart = Department.objects.get(id=nid)
        data = {'title': depart.title}
        return JsonResponse(data)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        nid = request.POST.get('id')
        Department.objects.filter(id=nid).update(title=new_title)
        redirect_data = {'url': '/depart/list'}
        return JsonResponse(redirect_data)
