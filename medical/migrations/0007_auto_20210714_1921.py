# Generated by Django 3.2.3 on 2021-07-14 19:21

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0006_alter_medicalrecord_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalexam',
            name='cardiovascular_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='cardiovascular_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('palpitations', 'palpitations'), ('edema pain', 'edema pain'), ('pain on walk', 'pain on walk'), ('pain on rest', 'pain on rest'), ('pain on effort', 'pain on effort')], max_length=64),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='digestive_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='digestive_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('appetite problem', 'appetite problem'), ('transit', 'transit'), ('stool', 'stool'), ('rectal bleeding', 'rectal bleeding'), ('abdominal pain', 'abdominal pain')], max_length=61),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='locomotor_case',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('muscular', 'muscular'), ('articular', 'articular'), ('vertebral', 'vertebral'), ('neurological', 'neurological')], max_length=41),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='locomotor_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='ophtalmological_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='ophtalmological_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('tearing', 'tearing'), ('pain', 'pain'), ('eye spots', 'eye spots')], max_length=22),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='orientation_cause',
            field=models.CharField(blank=True, choices=[('notice', 'notice'), ('hospitalization', 'hospitalization'), ('treatment', 'treatment')], default='notice', max_length=50),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='orientation_response',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='orientation_specialist',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='orl_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='orl_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('whistling', 'whistling'), ('repeated tonsillitis', 'repeated tonsillitis'), ('epistaxis', 'epistaxis'), ('rhinorrhea', 'rhinorrhea')], max_length=51),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='respiratory_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='respiratory_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cough', 'cough'), ('dyspnea', 'dyspnea'), ('expectoration', 'expectoration'), ('chest pain', 'chest pain')], max_length=38),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='skin_exam',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalexam',
            name='skin_state',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('skin infection', 'skin infection')], max_length=14),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='allergic_reaction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='congenital_condition',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='general_diseases',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='medications',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='number_units',
            field=models.IntegerField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='other',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='surgical_intervention',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='tobaco_taken_as',
            field=models.CharField(blank=True, choices=[('smoking tobaco', 'smoking tobaco'), ('chewing tobaco', 'chewing tobaco'), ('injection tobaco', 'injection tobaco')], max_length=50),
        ),
    ]