from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password, **extrafields):
        if not (firstname and lastname):
            raise ValidationError("User must have first name and last name")
        
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            email=email,
            **extrafields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, firstname, lastname, email, password, **extrafields):
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)

        if extrafields.get("is_staff") == False:
            raise ValidationError("Superuser must have is_staff to true")
        
        if extrafields.get("is_superuser") == False:
            raise ValidationError("Superuser must have is_superuser to true")
        
        user = self.create_user(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            **extrafields,
        )

        return user
