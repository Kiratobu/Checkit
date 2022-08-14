from django.contrib.auth.models import BaseUserManager


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
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user
