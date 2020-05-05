"""faceDetect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from face_app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('mainadmin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('af10ef20dd9060bbeead0afbc55381a66af442ef/',views.user_login,name='user_login'),
    path('f90453ec712ce4505cc425e7e881e1d58ea274c3/',views.dashboard,name='dashboard'),
    path('ffedd6efd387c77989d15ad1db28c76323f7f48f/',views.facial_database,name='facial_database'),
    path('42aef171c1c0accaeee38c605d98ab5db51a13f5/',views.track,name='track'),
    path('a27297bde9732f2e73fbc06db2611764e3ad9855/',views.report,name='report'),
    path('d6df1ab7ac275f8c7aff9d010ccfd0db08bbe2d8/',views.settings,name='settings'),
    path('c29aea40b84e04595f2fec3e5918530f71f31a7f/<int:pid>/', views.p_details, name='p_details'),
    path('3113a9343abdb3954f6932e2759bf694c6d5f67e/',views.settings,name='settings'),
    path('55525e1b3dfd8787fd202aed45fb04494e3242d0/',views.logout,name='logout'),
    path('edit_photo/',views.edit_photo,name='edit_photo'),
    path('ip_record_table/',views.ip_record_table,name='ip_record_table'),
    path('edit_pofile/',views.edit_pofile,name='edit_pofile'),
    path('webcam/',views.webcam,name='webcam'),
    path('trace_face/',views.trace_face,name='trace_face'),
    path('photo_detect/',views.photo_detect,name='photo_detect'),
    path('video_detect/',views.video_detect,name='video_detect'),
    path('success', views.success, name = 'success'),
    path('92864c44be1c8a39577e107e47097825/', views.home1, name = 'home1'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('image_upload/',views.image_upload,name='image_upload'),
    path('edit_photo/',views.edit_photo,name='edit_photo'),
    path('load_ip/',views.load_ip,name='load_ip'),
    path('web_upload/',views.web_upload,name='web_upload'),
    path('record_table/',views.record_table,name='record_table'),
    path('web_image_upload/',views.web_image_upload,name='web_image_upload'),
    path('mylogin/',views.admin_login,name='admin_login'),
    path('users_data/',views.users_data,name='users_data'),
    path('users_repo/',views.users_repo,name='users_repo'),
    path('34c6c76432d8db915e8dc7d585d817da/',views.admin_request,name='admin_request'),
    path('Add_user/',views.adduser,name='adduser'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
    path('Deactivate/<int:pid>',views.disable_user,name='disable_user'),
    path('Activate/<int:eid>',views.enable_user,name='enable_user'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('ad66cc5f7daad7a9c5b53d3a04cc3308/',views.admin_home,name='admin_home'),
    path('email/',views.email,name='email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
