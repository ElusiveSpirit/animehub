from django.core.management.base import BaseCommand

from animehub.parsers.shikimori import ShikimoriClient, ShikimoriParser


class Command(BaseCommand):
    help = 'Save anime by ID'

    def add_arguments(self, parser):
        parser.add_argument('anime_id', type=int)

    def handle(self, *args, anime_id: int, **options):
        client = ShikimoriClient()
        parser = ShikimoriParser(client)

        parser.save_by_id(anime_id)
