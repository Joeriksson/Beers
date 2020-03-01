from django.core.management import BaseCommand

import requests

from beers.models import Beer


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Update Beer table from punkapi.com"

    def handle(self, *args, **options):
        response = requests.get('https://api.punkapi.com/v2/beers/?beer_name=my_name_is')

        for beer in response.json():
            try:
                beer_row = Beer.objects.get(name=beer['name'])
            except Beer.DoesNotExist:
                beer_row = None

            if beer_row:
                # Beer already exists
                self.stdout.write(f'{beer_row.name} already exists.')
                continue
            else:
                # Add beer to db
                self.stdout.write('Create new row')
                beer_row = Beer()
                beer_row.name = beer['name']
                beer_row.tagline = beer['tagline']
                beer_row.first_brewed = beer['first_brewed']
                beer_row.description = beer['description']
                beer_row.save()
                # self.stdout.write(f"name: {len(beer['name'])}")
                # self.stdout.write(f"tagline: {len(beer['tagline'])}")
                # self.stdout.write(f"first_brewed: {len(beer['first_brewed'])}")
                # self.stdout.write(f"description: {len(beer['description'])}")

        self.stdout.write('#########################')
        self.stdout.write('Updated Beer list')
        self.stdout.write('#########################')

