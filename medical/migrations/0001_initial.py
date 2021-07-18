# Generated by Django 3.2.3 on 2021-07-14 11:42

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_auto_20210714_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('doctor_name', models.CharField(max_length=100)),
                ('wieght', models.IntegerField(max_length=2)),
                ('height', models.IntegerField(max_length=2)),
                ('hearing_right', models.CharField(max_length=20)),
                ('hearing_left', models.CharField(max_length=20)),
                ('visual_acuity_with_correction_left', models.CharField(max_length=20)),
                ('visual_acuity_with_correction_right', models.CharField(max_length=20)),
                ('visual_acuity_without_correction_left', models.CharField(max_length=20)),
                ('skin_state', multiselectfield.db.fields.MultiSelectField(choices=[('skin infection', 'skin infection')], max_length=14)),
                ('skin_exam', models.TextField()),
                ('ophtalmological_state', multiselectfield.db.fields.MultiSelectField(choices=[('tearing', 'tearing'), ('pain', 'pain'), ('eye spots', 'eye spots')], max_length=22)),
                ('ophtalmological_exam', models.TextField()),
                ('orl_state', multiselectfield.db.fields.MultiSelectField(choices=[('whistling', 'whistling'), ('repeated tonsillitis', 'repeated tonsillitis'), ('epistaxis', 'epistaxis'), ('rhinorrhea', 'rhinorrhea')], max_length=51)),
                ('orl_exam', models.TextField()),
                ('locomotor_case', multiselectfield.db.fields.MultiSelectField(choices=[('muscular', 'muscular'), ('articular', 'articular'), ('vertebral', 'vertebral'), ('neurological', 'neurological')], max_length=41)),
                ('locomotor_exam', models.TextField()),
                ('respiratory_state', multiselectfield.db.fields.MultiSelectField(choices=[('cough', 'cough'), ('dyspnea', 'dyspnea'), ('expectoration', 'expectoration'), ('chest pain', 'chest pain')], max_length=38)),
                ('respiratory_exam', models.TextField()),
                ('cardiovascular_state', multiselectfield.db.fields.MultiSelectField(choices=[('palpitations', 'palpitations'), ('edema pain', 'edema pain'), ('pain on walk', 'pain on walk'), ('pain on rest', 'pain on rest'), ('pain on effort', 'pain on effort')], max_length=64)),
                ('cardiovascular_exam', models.TextField()),
                ('digestive_state', multiselectfield.db.fields.MultiSelectField(choices=[('appetite problem', 'appetite problem'), ('transit', 'transit'), ('stool', 'stool'), ('rectal bleeding', 'rectal bleeding'), ('abdominal pain', 'abdominal pain')], max_length=61)),
                ('digestive_exam', models.TextField()),
                ('aptitude', models.BooleanField(default=False)),
                ('motife', models.TextField()),
                ('specialist', models.CharField(max_length=100)),
                ('orientation_cause', models.CharField(choices=[('notice', 'notice'), ('hospitalization', 'hospitalization'), ('treatment', 'treatment')], default='notice', max_length=50)),
                ('orientation_response', models.TextField()),
                ('patient', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='authentication.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_number', models.BigIntegerField(unique=True)),
                ('biometric', models.CharField(max_length=200)),
                ('tobaco_consumption', models.BooleanField(default=False)),
                ('tobaco_taken_as', models.CharField(choices=[('smoking tobaco', 'smoking tobaco'), ('chewing tobaco', 'chewing tobaco'), ('injection tobaco', 'injection tobaco')], max_length=50)),
                ('number_units', models.IntegerField(max_length=2)),
                ('alcohol_consumption', models.BooleanField(default=False)),
                ('medication_consumption', models.BooleanField(default=False)),
                ('medications', models.TextField()),
                ('other', models.TextField()),
                ('general_diseases', models.TextField()),
                ('surgical_intervention', models.TextField()),
                ('congenital_condition', models.TextField()),
                ('allergic_reaction', models.TextField()),
                ('patient', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='authentication.patient')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.medicalexam')),
            ],
        ),
    ]
