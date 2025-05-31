from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь',
            ),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.ingredient',
                verbose_name='Ингредиент',
            ),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ingredient_items',
                to='recipes.recipe',
                verbose_name='Рецепт',
            ),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recipes',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор рецепта',
            ),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(
                related_name='recipes',
                through='recipes.RecipeIngredient',
                to='recipes.ingredient',
                verbose_name='Ингредиенты',
            ),
        ),
        migrations.AddField(
            model_name='follow',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='following',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор рецепта',
            ),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='follower',
                to=settings.AUTH_USER_MODEL,
                verbose_name='подписчик',
            ),
        ),
        migrations.AddField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.recipe',
                verbose_name='Рецепты',
            ),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь',
            ),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_user_recipe_in_shopping_cart',
            ),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_user_author_subscription',
            ),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(
                check=models.Q(('user', models.F('author')), _negated=True),
                name='prevent_self_follow',
            ),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_user_recipe_in_favorites',
            ),
        ),
    ]
