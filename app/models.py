from django.db import models

from account.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Organisation(models.Model):
    title = models.CharField(max_length=255)
    organisation_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True
    )

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"


class Branch(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    head_branch = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    organisation = models.ForeignKey(
        Organisation,
        related_name="branches",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = ["organisation", "title"]
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.organisation.title} {self.head_branch}"


class UserPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, blank=False
    )


class BranchPost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, blank=False
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=False, blank=False
    )


class Notification(models.Model):
    """Notification model"""

    WITHOUT = "Without notification"
    FIVE_MIN = "five_minutes"
    TEN_MIN = "ten_minutes"
    FIFETEEN = "fifteen_minutes"
    THIRTY_MIN = "thirty_minutes"
    ONE_HOUR = "one_hour"
    THREE_HOUR = "three_hours"
    ONE_DAY = "one_day"
    THREE_DAY = "three_days"

    NOTIFICATION_CHOICES = (
        (WITHOUT, "Без уведомлений"),
        (FIVE_MIN, "За 5 минут до события"),
        (TEN_MIN, "За 10 минут до события"),
        (FIFETEEN, "За 15 минут до события"),
        (THIRTY_MIN, "За 30 минут до события"),
        (ONE_HOUR, "За час до события"),
        (THREE_HOUR, "За 3 часа до события"),
        (ONE_DAY, "За день до события"),
        (THREE_DAY, "За 3 дня до события"),
    )

    notification = models.CharField(
        max_length=255,
        choices=NOTIFICATION_CHOICES,
        default=WITHOUT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.notification}"


class Event(TimeStamp):
    """Event model"""

    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"
    SATURDAY = "SAT"
    SUNDAY = "SUN"
    EVERY_WEEKDAY = "EWD"
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
        (EVERY_WEEKDAY, "Каждый будний день"),
        (EVERY_WEEK, "Каждую неделю"),
        (EVERY_MONTH, "Каждый месяц"),
        (EVERY_YEAR, "Каждый год"),
    )

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    date = models.DateField(verbose_name="Дата события")
    description = models.TextField(null=True, verbose_name="Описание")
    time_from = models.TimeField(verbose_name="Время начала")
    time_to = models.TimeField(verbose_name="Время окончания")
    repeat = models.CharField(
        max_length=255,
        choices=REPEAT_CHOICES,
        verbose_name="Повторение",
        blank=True,
        null=True,
    )
    is_private = models.BooleanField(
        default=True, verbose_name="Является личным событием"
    )
    room_id = models.ForeignKey("Room", on_delete=models.CASCADE)
    event_type = models.ForeignKey(
        "EventType", on_delete=models.CASCADE, related_name="Event_Type"
    )
    notifications = models.ManyToManyField(
        "Notification", related_name="notifications"
    )

    def __str__(self):
        return f"{self.title}"


class EventType(models.Model):

    """Event type model"""

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
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="User"
    )

    def __str__(self):
        return f"{self.title}"


class UserParticipant(TimeStamp):
    """User Participant model"""

    STATUS_ACCEPTED = "accepted"
    STATUS_DECLINED = "declined"
    STATUS_DELIGATED = "deligated"

    STATUS_CHOICES = (
        (STATUS_ACCEPTED, "Принято"),
        (STATUS_DECLINED, "Отклонено"),
        (STATUS_DELIGATED, "Делегировано"),
    )

    is_creator = models.BooleanField(
        default=False, verbose_name="Является организатором"
    )
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        verbose_name="Статус мероприятия",
    )
    user_participant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_Participant"
    )
    event_participant = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_Participant"
    )

    def __str__(self):
        return f"{self.user_participant}"


class Room(TimeStamp):
    """Room model"""

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
    """Image room model"""

    name = models.CharField(max_length=255)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
