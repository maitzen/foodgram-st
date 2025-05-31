from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0004_alter_recipeingredient_recipe'),
    ]
    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='text',
        ),
    ]
