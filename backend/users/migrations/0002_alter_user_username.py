from django.db import migrations, models

import foodgram.validators


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]
    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                max_length=150,
                unique=True,
                validators=[
                    foodgram.validators.AllowedCharactersUsernameValidator()
                ],
                verbose_name='Имя пользователя',
            ),
        ),
    ]
