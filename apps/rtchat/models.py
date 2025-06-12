from django.db import models
from django.contrib.auth.models import User


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.group_name


class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} : {self.body[:20]+'...' if len(self.body) > 20 else self.body}"

    class Meta:
        ordering = ['-created_at']