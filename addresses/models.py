from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.IntegerField()

    user = models.OneToOneField(
        # Passar o caminho absoluto até a model
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
        null=True,
    )

    def __repr__(self) -> str:
        return f"<Address ({self.id}) - ({self.street})>"
