from django.db import models

class ShortUrl(models.Model):
    long_url = models.URLField(max_length=100)
    short_code = models.CharField(max_length=20)

    def __str__(self):
        return self.short_code

# class ShortUrl(models.Model):
#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
