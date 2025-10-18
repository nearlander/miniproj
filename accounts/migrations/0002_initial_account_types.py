# In accounts/migrations/0002_initial_account_types.py

from django.db import migrations

def create_initial_account_types(apps, schema_editor):
    # Get the BankAccountType model from the historical app registry
    BankAccountType = apps.get_model('accounts', 'BankAccountType')

    defaults = [
        ("Savings Account", 50000, 3.5, 4),
        ("Current Account", 100000, 1.5, 2),
        ("Student Account", 20000, 2.0, 1),
        ("Joint Account", 75000, 2.5, 4),
    ]

    for name, max_withdraw, rate, calc in defaults:
        BankAccountType.objects.get_or_create(
            name=name,
            defaults={
                "maximum_withdrawal_amount": max_withdraw,
                "annual_interest_rate": rate,
                "interest_calculation_per_year": calc,
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # Make sure this matches your first migration file
    ]

    operations = [
        migrations.RunPython(create_initial_account_types),
    ]