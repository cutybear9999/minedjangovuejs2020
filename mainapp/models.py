from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=225, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    def _str_(self):
        return self.title

class DBItem(models.Model):
    orlHost = models.TextField()
    orlPort = models.TextField()
    orlServiceName = models.TextField()
    orlSchemaName = models.TextField()
    orlUserName = models.TextField()
    orlPassword = models.TextField()
    mysqlHost = models.TextField()
    mysqlPort = models.TextField()
    mysqlDatabaseName = models.TextField()
    mysqlUserName = models.TextField()
    mysqlPassword= models.TextField()
    def _str_(self):
        return self.orlHost

class Structure(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='structures')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

