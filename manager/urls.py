from django.urls import path
from manager.view import depart, user, project, admin, account

urlpatterns = [
    # depart
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    # path('depart/edit/', manager.view.depart.depart_edit),
    path('depart/delete/', depart.depart_delete),

    # user
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/delete/', user.user_delete),
    # project
    path('project/list/', project.project_list),
    path('project/add/', project.project_add),
    path('project/delete/', project.project_delete),
    # admin
    path('superadmin/list/', admin.adminlist),
    path('superadmin/add/', admin.adminadd),

    # login
    path('login/', account.login)
]
