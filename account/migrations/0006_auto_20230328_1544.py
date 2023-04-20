# Generated by Django 3.2 on 2023-03-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20230322_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bank_account_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bvn',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gendre',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='highest_level_of_education',
            field=models.CharField(choices=[('NURSERY', 'NURSERY'), ('PRIMARY', 'PRIMARY'), ('SECONDARY', 'SECONDARY'), ('DEGREE', 'DEGREE'), ('MASTERS', 'MASTERS'), ('PHD', 'PHD')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_image',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_type',
            field=models.CharField(choices=[('NATIONAL IDENTITY CARD', 'NATIONAL IDENTITY CARD'), ('VOTERS CARD', 'VOTERS CARD'), ('DRIVERS LICENCE', 'DRIVERS LICENCE'), ('PASSPORT', 'PASSPORT')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lga_origin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lga_residence',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_names',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(default='', null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='residencial_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='scheme_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state_of_origin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state_of_residence',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_of_application',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
