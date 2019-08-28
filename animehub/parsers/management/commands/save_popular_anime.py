from django.core.management.base import BaseCommand

from animehub.parsers.shikimori import ShikimoriClient, ShikimoriParser


class Command(BaseCommand):
    help = 'Save popular anime from shikimori'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--pages',
            default=1,
            type=int,
            help='Количество страниц'
        )

    def handle(self, *args, pages: int, **options):
        self.stdout.write(f'Start saving popular animes. Max page {pages}')
        client = ShikimoriClient()
        parser = ShikimoriParser(client)

        parser.save_popular_list(pages)
