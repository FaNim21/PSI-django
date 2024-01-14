from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from CS2Ranking.models import Match, Team


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError('User must have an email address')

        user: 'RankingUser' = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class RankingUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=45, unique=True, null=True)
    password = models.CharField(max_length=255)
    favourite_teams = models.ManyToManyField(Team)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Comment(models.Model):
    ranking_user = models.ForeignKey(
        RankingUser,
        on_delete=models.SET_DEFAULT,
        default=None,
    )
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.CharField(max_length=140)
    created_time = models.DateTimeField(auto_now_add=True)
