# Generated by Django 2.2.6 on 2019-11-17 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colon',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        serialize=False, verbose_name='ID')),
                ('gene_symbol', models.TextField(blank=True,
                                                 primary_key=True, db_column='Gene Symbol', null=True)),
                ('control1', models.TextField(blank=True, null=True)),
                ('control2', models.TextField(blank=True, null=True)),
                ('control3', models.TextField(blank=True, null=True)),
                ('control4', models.TextField(blank=True, null=True)),
                ('control5', models.TextField(blank=True, null=True)),
                ('kras1', models.TextField(blank=True, db_column='KRAS1', null=True)),
                ('kras2', models.TextField(blank=True, db_column='KRAS2', null=True)),
                ('kras3', models.TextField(blank=True, db_column='KRAS3', null=True)),
                ('kras4', models.TextField(blank=True, db_column='KRAS4', null=True)),
                ('kras5', models.TextField(blank=True, db_column='KRAS5', null=True)),
            ],
            options={
                'db_table': 'colon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(
                    max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GraphsGene',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_symbol', models.CharField(max_length=100)),
                ('control1', models.DecimalField(decimal_places=5, max_digits=10)),
                ('control2', models.DecimalField(decimal_places=5, max_digits=10)),
                ('control3', models.DecimalField(decimal_places=5, max_digits=10)),
                ('control4', models.DecimalField(decimal_places=5, max_digits=10)),
                ('control5', models.DecimalField(decimal_places=5, max_digits=10)),
                ('kras1', models.DecimalField(decimal_places=5, max_digits=10)),
                ('kras2', models.DecimalField(decimal_places=5, max_digits=10)),
                ('kras3', models.DecimalField(decimal_places=5, max_digits=10)),
                ('kras4', models.DecimalField(decimal_places=5, max_digits=10)),
                ('kras5', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
            options={
                'db_table': 'graphs_gene',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchProtein',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_text', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'search_protein',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Gene',
        ),
    ]
