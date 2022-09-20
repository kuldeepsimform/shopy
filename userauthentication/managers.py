from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, phone,password=None):
        user = self.model(
            email = self.normalize_email(email),
            firstname = firstname,
            lastname = lastname,
            phone = phone,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email,firstname,lastname,phone,password=None):
        user = self.create_user(
            email=email,
            password=password,
            firstname = firstname,
            lastname = lastname,
            phone = phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user