from django.db import models


class TextSummary(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    original_text = models.TextField()
    summarized_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title or self.original_text[:3]
