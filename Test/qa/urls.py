from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'answers', views.AnswerViewSet, basename='answers')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'auth', views.CreateUserViewSet, basename='auth')
urlpatterns = router.urls

