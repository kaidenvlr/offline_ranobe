from celery import shared_task

from core.celery import app
from parser.utils.parse import concat_to_epub


@shared_task
def parse_novel(url):

    return concat_to_epub(url)
