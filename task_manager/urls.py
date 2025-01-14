"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView

from tasks.views import (
    GenericTaskCreateView,
    GenericTaskDeleteView,
    GenericTaskDetailView,
    GenericTaskUpdateView,
    GenericTaskView,
    UserCreateView,
    UserLoginView,
    all_task_view,
    completed_task_view,
    done_task_view,
    sessions_storage_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", GenericTaskView.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("update-task/<pk>/", GenericTaskUpdateView.as_view()),
    path("detail-task/<pk>/", GenericTaskDetailView.as_view()),
    path("delete-task/<pk>/", GenericTaskDeleteView.as_view()),
    path("user/signup", UserCreateView.as_view()),
    path("user/login", UserLoginView.as_view()),
    path("user/logout", LogoutView.as_view()),
    path("completed_task/", completed_task_view),
    path("completed_task/<int:index>/", done_task_view),
    path("all_tasks/", all_task_view),
    path("sessiontest/", sessions_storage_view),
]
