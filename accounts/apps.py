from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from .models import BankAccountType
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
