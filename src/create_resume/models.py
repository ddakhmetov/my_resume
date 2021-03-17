from django.db import models


class Worker(models.Model):

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    father_name = models.CharField(max_length=30, verbose_name='Отчество')
    phone = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город')
    email = models.EmailField(verbose_name='e-mail')
    position = models.CharField(max_length=255, verbose_name='Желаемая должность')
    birth_date = models.DateField(verbose_name='Дата рождения')
    money = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='Желаемая зарплата')
    about_me = models.TextField(verbose_name='О себе')
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    # def __str__(self):
    #     return self.last_name


class Hard_skills(models.Model):

    title = models.CharField(max_length=50, verbose_name='Hard skills', blank=True)
    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)
    skills = models.CharField(max_length=255, verbose_name='Основные навыки')

    class Meta:
        verbose_name = 'Hard skill'
        verbose_name_plural = 'Hard skills'
    
    def __str__(self):
        return self.title


class Soft_skills(models.Model):

    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)
    skills = models.JSONField(verbose_name='Дополнительные навыки')

    class Meta:
        verbose_name = 'Soft skill'
        verbose_name_plural = 'Soft skills'


class Photo_worker(models.Model):

    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)
    url = models.URLField(verbose_name='Ссылка на фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Projects(models.Model):

    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)
    url = models.URLField(verbose_name='Ссылка на проекты')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Works(models.Model):

    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(verbose_name='Конец работы')
    company = models.CharField(max_length=255, verbose_name='Компания')
    position = models.CharField(max_length=100, verbose_name='Должность')
    duties = models.TextField(verbose_name='Обязанности')
    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Education(models.Model):

    start_date = models.DateField(verbose_name='Начало учёбы')
    end_date = models.DateField(verbose_name='Окончание учёбы')
    university = models.CharField(max_length=255, verbose_name='Учебное заведение')
    academy = models.CharField(max_length=255, verbose_name='Степень')
    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class Hobbie(models.Model):

    worker_id = models.ForeignKey('Worker', verbose_name='Для работника', on_delete=models.CASCADE)
    hobbies = models.JSONField(verbose_name='Мои хобби')

    class Meta:
        verbose_name = 'Хобби'
        verbose_name_plural = 'Хобби'
