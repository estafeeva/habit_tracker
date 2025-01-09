from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer

from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    pagination_class = CustomPagination
    serializer_class = HabitSerializer

    def get_queryset(self):
        queryset = Habit.objects.filter(user__pk=self.request.user.pk)
        return queryset

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner]
        return super().get_permissions()


class PublicViewSet(ModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = CustomPagination
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner]
        elif self.action in ["create"]:
            self.permission_classes = [~AllowAny]

        return super().get_permissions()
