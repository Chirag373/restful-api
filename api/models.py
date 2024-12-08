from django.db import models

STATUS_CHOICE = [
    ("Completed", "Completed"),
    ("In-progress", "In-progress"),
    ("Backlog", "Backlog")
]

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICE, 
        default="Completed", 
        blank=False, 
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
