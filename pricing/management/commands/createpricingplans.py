import yaml
from django.core.management.base import BaseCommand
from pricing.models import PricingPlan


class Command(BaseCommand):
    help = 'Create pricing plans from yaml'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as stream:
            plans = yaml.safe_load(stream)
            for plan in plans:
                pricing_plan, _ = PricingPlan.objects.get_or_create(name=plan['name'])
                pricing_plan.amount = plan['amount']
                pricing_plan.save()

        self.stdout.write(self.style.SUCCESS('Successfully created plans'))
