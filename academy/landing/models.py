from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    teaching_course = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name} ({self.phone_number})"

# ForeignKey - тип поля один - к - одному
# Это поле необходимо для создания связи какого либо поля с другой моделью

# null - необходим для определения обязательности внесения информации в поле

# есть 3 сценария действий бд после удаления какой либо модели с которой налажена связь
# 1) если модель удалена, то будет удалён и столбец, который ссылался на эту модель - models.CASCADE
# 2)  если мод удалена, то поля столбца примут значения null - models.SET_NULL
# 3) если мод удалена, то значения полей сохранятся - models.PROTECT
