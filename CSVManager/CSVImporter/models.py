from django.db import models

class CsvFile(models.Model):
    username = models.CharField(max_length=50, verbose_name="Username", blank=True, default=None)
    csv_file = models.FileField(upload_to="files/",verbose_name='File', null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'csv_file'
        verbose_name = 'CsvFile'
        verbose_name_plural = 'CsvFiles'
        ordering = ['created']