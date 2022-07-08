from django.db import models
from account.models import User

class Organisation(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    organisation_admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

class Branch(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    head_branch = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    organisation = models.ForeignKey(Organisation, related_name='branches', on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        unique_together = ['organisation', 'title']
        ordering = ['title']

    def __str__(self):
        return f'{self.title} {self.organisation.title} {self.head_branch}'

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)

class BranchPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)
