from django.db import models

IDEA_STATUS = (
    ('pending', 'Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)


class Idea(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default='pending')

    def __str__(self):
        return self.title


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'ID {self.id}'
