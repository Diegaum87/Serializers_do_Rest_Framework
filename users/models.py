from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()

    # auto_now_add -> Atualização no momento de criação do dado
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now -> Atualização no momento de atualização do dado
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<User ({self.id}) - ({self.first_name})>"
