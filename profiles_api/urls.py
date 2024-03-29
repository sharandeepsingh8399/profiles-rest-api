from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewset)
router.register('feed',views.UserProfileFeedViewSet)
##we are not giving base name because it tallies from the viewset as the query field is used


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
