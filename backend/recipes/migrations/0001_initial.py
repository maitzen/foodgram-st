import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Favorite',
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
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
            },
        ),
        migrations.CreateModel(
            name='Follow',
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
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
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
                    'name',
                    models.CharField(
                        db_index=True,
                        max_length=128,
                        unique=True,
                        verbose_name='Название ингредиента',
                    ),
                ),
                (
                    'measurement_unit',
                    models.CharField(
                        max_length=128,
                        verbose_name='Единица измерения',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
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
                    'name',
                    models.CharField(
                        db_index=True,
                        max_length=128,
                        verbose_name='Название рецепта',
                    ),
                ),
                (
                    'description',
                    models.TextField(verbose_name='Описание'),
                ),
                (
                    'image',
                    models.ImageField(
                        upload_to='recipes_photo/',
                        verbose_name='Фотография блюда',
                    ),
                ),
                (
                    'cooking_time',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1,
                                message=(
                                    'Время не может быть меньше одной минуты.',
                                ),
                            ),
                        ],
                        verbose_name='Время приготовления (в минутах)',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name='Дата создания',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
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
                    'amount',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1,
                                message=(
                                    'Количество не может быть меньше единицы.',
                                ),
                            ),
                        ],
                        verbose_name='Количество',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Ингридиент рецепта',
                'verbose_name_plural': 'Ингридиенты рецептов',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
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
                    'recipe',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='recipes.recipe',
                        verbose_name='Рецепт',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Корзина покупок',
                'verbose_name_plural': 'Корзины покупок',
            },
        ),
    ]
