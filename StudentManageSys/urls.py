"""StudentManageSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static

from StudentManageSys import settings

urlpatterns = [
    # url(r'admin/', admin.site.urls),
    url(r'^api/v1/', include('user_info.urls')),
    url(r'^api/v1/', include('campus.urls')),
    url(r'^api/v1/', include('channel.urls')),
    url(r'^api/v1/', include('course.urls')),
    url(r'^api/v1/', include('coupon.urls')),
    url(r'^api/v1/', include('order.urls')),
    url(r'^api/v1/', include('project.urls')),
    url(r'^api/v1/', include('student.urls')),
    url(r'^api/v1/', include('log_info.urls')),
    url(r'^api/v1/', include('record.urls')),
    url(r'^api/v1/', include('student_course.urls')),
    url(r'^api/v1/', include('complain.urls')),
    url(r'^api/v1/', include('message.urls')),
    url(r'^api/v1/', include('common.urls')),
]
