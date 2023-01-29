# Generated by Django 4.1.5 on 2023-01-27 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hno', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=255)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phoneNo', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profileimg')),
                ('addressDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.address')),
                ('projects', models.ManyToManyField(to='testapp.project')),
                ('qualifications', models.ManyToManyField(to='testapp.qualification')),
                ('workExperience', models.ManyToManyField(to='testapp.workexperience')),
            ],
        ),
    ]
