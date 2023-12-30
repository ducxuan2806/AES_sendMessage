from Cryptodome.Random import get_random_bytes
from django.db import models


class UserProfile(models.Model):

    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    key = models.TextField(blank=True, null=True)  # Add privateKey field

    def generate_rsa_key(self, bytes):
        if not self.key:  # Check if private key already exists
            self.key = get_random_bytes(bytes)
            self.save()
            return self.key
        else:
            return self.key

    def __str__(self):
        return f"{self.name}"


class Messages(models.Model):

    description = models.TextField()
    sender_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name} From: {self.sender_name}"

    class Meta:
        ordering = ('timestamp',)


class Friends(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    friend = models.IntegerField()
    key = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.friend}"

