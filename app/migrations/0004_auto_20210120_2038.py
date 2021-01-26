# Generated by Django 3.1.5 on 2021-01-20 15:08

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210118_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/client')),
                ('stars', models.IntegerField()),
                ('name', models.TextField()),
                ('emotion', models.TextField(default='HAPPY')),
                ('desc', models.TextField()),
                ('source', models.TextField()),
                ('source_link', models.TextField()),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/company_logo')),
                ('name', models.TextField()),
                ('link', models.TextField()),
            ],
            options={
                'verbose_name': 'CompanyLogo',
                'verbose_name_plural': 'CompanyLogos',
                'db_table': 'company_logo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('head', models.TextField()),
                ('desc', models.TextField()),
                ('phone', models.TextField(help_text='+91-9962230987')),
                ('mail', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.TextField()),
                ('company', models.TextField()),
                ('year', models.TextField()),
                ('count', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/company')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('btn_url', models.TextField()),
                ('btn_text', models.TextField(default='DETAILS +')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'db_table': 'experience',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social', models.BooleanField(default='true')),
                ('sec1', models.BooleanField(default='true')),
                ('sec2', models.BooleanField(default='true')),
                ('sec3', models.BooleanField(default='true')),
                ('sec4', models.BooleanField(default='true')),
                ('sec5', models.BooleanField(default='true')),
                ('sec6', models.BooleanField(default='true')),
                ('company_logo', models.BooleanField(default='true')),
                ('video', models.BooleanField(default='true')),
            ],
            options={
                'verbose_name': 'Hide',
                'verbose_name_plural': 'Hides',
                'db_table': 'hide',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Navigate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec1', models.TextField(default='SLIDER')),
                ('sec2', models.TextField(default='ABOUT')),
                ('sec3', models.TextField(default='RESUME')),
                ('sec4', models.TextField(default='SKILLS')),
                ('sec5', models.TextField(default='PROJECTS')),
                ('sec6', models.TextField(default='CLIENTS')),
            ],
            options={
                'verbose_name': 'Navigate',
                'verbose_name_plural': 'Navigates',
                'db_table': 'navigate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField()),
                ('desc', models.TextField()),
                ('btn_link', models.TextField()),
                ('btn_text', models.TextField()),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'project',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjectShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/project')),
                ('icon', models.TextField()),
                ('project', models.TextField()),
                ('project_link', models.TextField()),
                ('cat1', models.TextField()),
                ('cat_link1', models.TextField()),
                ('cat2', models.TextField()),
                ('cat_link2', models.TextField()),
            ],
            options={
                'verbose_name': 'ProjectShow',
                'verbose_name_plural': 'ProjectShows',
                'db_table': 'projectShow',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_name', models.TextField(default='MY RESUME')),
                ('name', models.TextField()),
                ('sub_title', models.TextField()),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('download', models.FileField(upload_to='download/')),
                ('vlink', models.URLField()),
                ('vhead', models.TextField()),
                ('vdesc', models.TextField()),
                ('vbtn_link', models.TextField()),
                ('vbtn_text', models.TextField(default='MY YOUTUBE CHANNEL')),
                ('subhead', models.TextField()),
                ('whead', models.TextField()),
                ('wdesc', models.TextField()),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
                'db_table': 'resume',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FAC921', max_length=18)),
                ('title', models.TextField()),
                ('favicon', models.ImageField(upload_to='images/favicon')),
                ('logo', models.ImageField(upload_to='images/logo')),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('map_link', models.URLField()),
                ('map_text', models.TextField()),
                ('footer', models.TextField()),
                ('footer_link', models.TextField()),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
                'db_table': 'setting',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_name', models.TextField(default='Attainments')),
                ('image', models.ImageField(upload_to='images/skill')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'db_table': 'skill',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField()),
                ('desc', models.TextField()),
                ('count', models.IntegerField()),
                ('skill1', models.TextField()),
                ('percent1', models.IntegerField()),
                ('skill2', models.TextField()),
                ('percent2', models.IntegerField()),
                ('skill3', models.TextField()),
                ('percent3', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Skillset',
                'verbose_name_plural': 'Skillsets',
                'db_table': 'skillset',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/slider')),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
                ('btn_url', models.TextField()),
                ('btn_text', models.TextField()),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'db_table': 'slider',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.TextField()),
                ('social', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'db_table': 'social_links',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_name', models.TextField(default='TESTIMONIALS')),
                ('sub_head', models.TextField()),
                ('head', models.TextField()),
                ('desc', models.TextField()),
                ('call_to', models.TextField(default='READY TO ORDER YOUR PROJECT ?')),
                ('btn_link', models.TextField()),
                ('btn_text', models.TextField(default='GET IN TOUCH')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'db_table': 'testimonial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.TextField()),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
                ('desc', models.TextField()),
                ('more', models.TextField(default='MORE DETAILS')),
                ('more_link', models.TextField()),
                ('text', models.TextField(default='Need more info ? Visit my services page :')),
                ('btn', models.TextField(default='MY SERVICES')),
                ('btn_link', models.TextField()),
            ],
            options={
                'verbose_name': 'WorkProcess',
                'verbose_name_plural': 'WorkProcesss',
                'db_table': 'work_process',
                'managed': True,
            },
        ),
        migrations.RenameField(
            model_name='about',
            old_name='Content',
            new_name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='bg_name',
            field=models.TextField(default='ABOUT ME'),
        ),
        migrations.AlterField(
            model_name='about',
            name='btn_text',
            field=models.TextField(default='MY PORTFOLIO'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='images/about'),
        ),
    ]