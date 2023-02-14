from django.db import models

# Action Dropdown values

class Action(models.TextChoices):
    Backup_Intervention = 'BI', 'Backup Intervention'
    Change_Disk = 'CD', 'Change Disk'
    Restore = 'RE', 'Restore'
    Other_Action = 'OT', 'Other Action'

# Bern Logbook

class BernLog(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        verbose_name='Date',
        help_text='Enter the date in the format: DD/MM/YYYY'
    )
    action = models.CharField(
        max_length=2,
        choices=Action.choices,
        default=Action.Backup_Intervention,
    )
    comments = models.TextField()
    initials = models.CharField(max_length=10)

# Marly Logbook

class MarlyLog(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        verbose_name='Date',
        help_text='Enter the date in the format: DD/MM/YYYY'
    )
    action = models.CharField(
        max_length=2,
        choices=Action.choices,
        default=Action.Backup_Intervention,
    )
    comments = models.TextField()
    initials = models.CharField(max_length=10)
