import logging
import newspaper
from multiprocessing import Pool

from dubito.models import Newspaper, NewspaperArticle
from dubito.database import newspaper_db

from datetime import datetime

def fetch(url: str, language):
    logging.info(f'Fetching {url}...')
    np = newspaper.build(url, memoize_articles=False, language=language, fetch_images=False, fetch_videos=False)
    _newspaper = Newspaper(url=url, name=np.brand)
    _newspaper.save()
    for article in np.articles:
        try:
            logging.info(f'Fetching {article.url}...')
            article.download()
            article.parse()
            article.nlp()
            publish_date = article.publish_date
            if publish_date:
                publish_date = article.publish_date.replace(tzinfo=None)
            newspaper_article = NewspaperArticle(
                url=article.url,
                title=article.title,
                text=article.text,
                publish_date=publish_date,
                summary=article.summary,
                description=article.meta_description,
                newspaper=_newspaper,
            )
            newspaper_article.save()
        except Exception as e:
            logging.error(f'Error fetching {article.url}: {e}')
