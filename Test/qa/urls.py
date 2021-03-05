from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register(r'answers', views.AnswerViewSet, basename='answers')
router.register(r'questions', views.QuestionViewSet, basename='questions')


urlpatterns = router.urls

