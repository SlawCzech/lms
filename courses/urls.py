from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CoursesView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('create/', views.CreatCourseView.as_view(), name='course-create'),
    path('delete/<slug:slug>/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('edit/<slug:slug>/', views.CourseUpdateView.as_view(), name='course-edit'),
]

