from django.db import models

class Wall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    open = models.IntegerField()

    class Meta:
        db_table = 'Wall'     # Match your exact table name in SQLite
        managed = False       # Do NOT let Django create/migrate this table

    def __str__(self):
        return self.name

class Route(models.Model):
    id = models.AutoField(primary_key=True)
    wall = models.ForeignKey(Wall, on_delete=models.DO_NOTHING, db_column='wall')
    color = models.TextField()
    grade = models.TextField()
    date_set = models.TextField()
    date_strip = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Route'   # Match your SQLite table name exactly
        managed = False       # Avoid migrations on this table

    def __str__(self):
        return f'{self.color} - {self.grade}'

