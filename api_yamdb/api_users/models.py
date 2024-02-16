from django.db import models
from django.contrib.auth.models import AbstractUser

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLES = (
        (ADMIN, 'Администратор'),
        (USER, 'Аутентифицированный пользователь'),
        (MODERATOR, 'Модератор'),
    )
class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    bio = models.TextField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')

    class Meta:
        verbose_name = ('пользователь')
        verbose_name_plural = ('Пользователи')
        constraints = (
            models.UniqueConstraint(
                fields=('username', 'email',),
                name='unique_user'
            ),
        )
    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_user(self):
        return self.role == USER
    def __str__(self) -> str:
        return self.username
    