from manager.models import Department
from django.shortcuts import render, redirect


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

# def depart_edit(request):
#     # if request.method == 'GET':
#     #     row_obj = Department.objects.filter(id=nid).first()
#     #     return render(request, 'department.html', {'row_obj': row_obj})
#     new_title = request.POST.get('title')
#     Department.objects.filter(title=title).update()
#     return redirect('/depart/list')
