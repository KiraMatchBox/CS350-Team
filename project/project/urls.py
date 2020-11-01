from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns= [
#    path('post/<int:pk>/',HomeDetailView.as_view(),name='post_detail'),
#
#    path('',HomePageView.as_view(),name='home'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/register/', user_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('studentPage/',user_views.studentPage,name='studentPage'),
    path('courses/',views.courses, name='courses'),
    path('courses/add/',courseAddView.as_view(template_name='project/course_add.html'),name='course_add'),
    path('courses/<int:course_id>/', views.coursehome, name='coursehome'),
    path('courses/<int:course_id>/assignments', views.assignments, name='assignments'),
    path('courses/<int:course_id>/assignments/<int:assignment_id>', views.assignmenthome, name='assignmenthome'),
    path('courses/<int:course_id>/grades', views.grades, name='grades'),
    path('courses/<int:course_id>/discussion', views.discussion, name='discussion'),
    path('courses/<int:course_id>/discussion/<int:discussion_id>', views.discussionhome, name='discussionhome'),
    path('courses/<int:course_id>/discussion/add/', discussionCreateView.as_view(template_name='project/discussion_new.html') , name='addDiscussion'),
#   path('studentPage/TestClass/', TestClassView.as_view(),name='TestClass'),
#   path('studentPage/TestClass/discussion',discussionView.as_view(), name='discussion'),
#   path('studentPage/TestClass/discussion/<int:pk>',discussionDetailView.as_view(), name='discussion_detail'),
#   path('studentPage/TestClass/discussion/new/', discussionCreateView.as_view(), name='discussion_new'),
#   path('studentPage/TestClass/discussion/<int:pk>/edit/', discussionUpdateView.as_view(), name='discussion_edit'),
#   path('studentPage/TestClass/discussion/<int:pk>/delete/',discussionDetailView.as_view(), name='discussion_delete'),
#   path('studentPage/TestClass/studentList/', views.studentListView, name='studentList'),
#   path('assignment/', assignmentView.as_view(), name='assignment'),
#   path('assignment/new/', assignmentCreateView.as_view(), name='assignment_create'),

    #path('<int:pk>', StudentDetailView.as_view(), name='student_detail'),   

]