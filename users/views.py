from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# from materials.models import Course, Lesson
from users.models import User
from users.serializers import UserSerializer

"""from users.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session,
)"""


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
