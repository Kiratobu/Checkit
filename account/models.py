# from email.policy import default

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# from django.utils.crypto import get_random_string


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, **extra_fields):
        """
        Methode creates user
        :param email: str
        :param name: str
        :param surname: str
        :param extra_fields: dict
        :return: user
        """
        if not email:
            raise ValueError("Вы должны ввести свою электронную почту")
        if not first_name or not last_name:
            raise ValueError("Вы должны ввести свое Имя/Фамилию")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password()
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Methode creates superuser
        :param email: str
        :param password: str
        :return: superuser
        """
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, TimeStamp):
    """User model"""

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    number = models.CharField(max_length=20, unique=True, null=False)
    email = models.CharField(
        max_length=30, blank=False, unique=True, null=False
    )
    # referral_token = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    img = models.ImageField(default=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    """
    def save(self, *args, **kwargs):
        self.referral_token = f'{self.email}&{get_random_string(length=30)}'
        super().save(*args, **kwargs)
    """


class Event(TimeStamp):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    date = models.DateField(verbose_name="Дата события")
    description = models.TextField(null=True, verbose_name="Описание")
    time_from = models.TimeField(verbose_name="Время начала")
    time_to = models.TimeField(verbose_name="Время окончания")
    repeat = models.ManyToManyField(
        "Repeat",
    )
    is_private = models.BooleanField(
        default=True, verbose_name="Является личным событием"
    )
    room_id = models.ForeignKey("Room", on_delete=models.CASCADE)
    event_type = models.ForeignKey("EventType", on_delete=models.CASCADE)
    notification = models.ManyToManyField("Notification")

    def __str__(self):
        return f"{self.title}"


class Repeat(models.Model):

    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"
    SATURDAY = "SAT"
    SUNDAY = "SUN"
    EVERY_DAY = "ED"
    EVERY_WEEK = "EW"
    EVERY_MONTH = "EM"
    EVERY_YEAR = "EY"

    REPEAT_CHOICES = (
        (MONDAY, "Каждый Понедельник"),
        (TUESDAY, "Каждый Вторник"),
        (WEDNESDAY, "Каждую Среду"),
        (THURSDAY, "Каждый Четверг"),
        (FRIDAY, "Каждую Пятницу"),
        (SATURDAY, "Каждую Субботу"),
        (SUNDAY, "Каждое Воскресенье"),
        (EVERY_DAY, "Каждый день"),
        (EVERY_WEEK, "Каждую неделю"),
        (EVERY_MONTH, "Каждый месяц"),
        (EVERY_YEAR, "Каждый год"),
    )

    repetition = models.CharField(
        max_length=255, choices=REPEAT_CHOICES, null=True
    )


class Notification(models.Model):

    FIVE_MIN = "five_minutes"
    TEN_MIN = "ten_minutes"
    FIFETEEN = "fifteen_minutes"
    THIRTY_MIN = "thirty_minutes"
    ONE_HOUR = "one_hour"
    THREE_HOUR = "three_hours"
    ONE_DAY = "one_day"
    THREE_DAY = "three_days"

    NOTIFICATION_CHOICES = (
        (FIVE_MIN, "За 5 минут до события"),
        (TEN_MIN, "За 10 минут до события"),
        (FIFETEEN, "За 15 минут до события"),
        (THIRTY_MIN, "За 30 минут до события"),
        (ONE_HOUR, "За час до события"),
        (THREE_HOUR, "За 3 часа до события"),
        (ONE_DAY, "За день до события"),
        (THREE_DAY, "За 3 дня до события"),
    )

    notifications = models.CharField(
        max_length=255, choices=NOTIFICATION_CHOICES, null=True
    )


class UserParticipant(TimeStamp):
    STATUS_ACCEPTED = "accepted"
    STATUS_DECLINED = "declined"
    STATUS_DELIGATED = "deligated"

    STATUS_CHOICES = (
        (STATUS_ACCEPTED, "Принято"),
        (STATUS_DECLINED, "Отклонено"),
        (STATUS_DELIGATED, "Делегировано"),
    )

    is_creator = models.BooleanField(
        unique=True, verbose_name="Является организатором"
    )
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        verbose_name="Статус мероприятия",
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id}"


class EventType(models.Model):

    RED = "R"
    GREEN = "G"
    BLUE = "B"
    YELLOW = "Y"
    ORANGE = "O"
    PURPLE = "P"

    COLOR_CHOICES = (
        (RED, "Красный"),
        (GREEN, "Зелёный"),
        (BLUE, "Синий"),
        (YELLOW, "Жёлтый"),
        (ORANGE, "Оранжевый"),
        (PURPLE, "Фиолетовый"),
    )

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    color = models.CharField(
        max_length=255, choices=COLOR_CHOICES, verbose_name="Цвет"
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Room(TimeStamp):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")
    is_available = models.BooleanField(verbose_name="Доступно")
    has_projector = models.BooleanField(verbose_name="Имеется проектор")
    has_desk = models.BooleanField(verbose_name="Имеется доска")
    # organization_id = models.ForeignKey()

    def __str__(self):
        return f"{self.title}"


class ImageRoom(models.Model):
    name = models.CharField(max_length=255)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
