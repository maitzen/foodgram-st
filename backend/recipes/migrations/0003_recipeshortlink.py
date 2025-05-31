from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0002_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='RecipeShortLink',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'url_hash',
                    models.CharField(
                        db_index=True,
                        max_length=10,
                        unique=True,
                        verbose_name='Хэш',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата создания ссылки',
                    ),
                ),
                (
                    'recipe',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='recipes.recipe',
                        verbose_name='Рецепт',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Краткая ссылка на рецепт',
                'verbose_name_plural': 'Краткие ссылки на рецепты',
            },
        ),
    ]
