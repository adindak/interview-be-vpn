from django.db import models

class Notification(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"