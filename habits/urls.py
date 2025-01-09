from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicViewSet

app_name = HabitsConfig.name

router = SimpleRouter()
router.register(r"habits", HabitViewSet, basename="habit")
router.register(r"public", PublicViewSet, basename="public")

urlpatterns = [
    # path('', include(router.urls)),
]
urlpatterns += router.urls
