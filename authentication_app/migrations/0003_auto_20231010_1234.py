from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0002_remove_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
    ]
