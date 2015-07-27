__title__ = 'wikipy'
__author__ = 'Colby Brown'


import click
import wikipedia
import sys
import requests
from PIL import Image
from . import nlp


#TODO: Process the article text better to eliminate Unicode errors
""" Avoiding errors related to Unicode printing in Windows """
def safeprint(s):
    try:
        click.echo(s)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(s.encode('utf8').decode(sys.stdout.encoding))
        else:
            print(s.encode('utf8'))


@click.command()
@click.argument('article_name', default='Wikipedia', required=True)
@click.argument('language', default='en', required=False)
@click.option('--tldr', '-p', default=False, is_flag=True, help='Use natural language processing to condense output.')
def main(article_name, language, tldr):
    wikipedia.set_lang(language)
    str_article_name = str(article_name)
    click.echo(" ")
    click.echo("Fetching results for: {0}".format(article_name))
    click.echo(" ")
    wiki_object = wikipedia.page(str_article_name)

    #img = Image.open(wiki_object.images[10])
    #img.show()

    if tldr:
        summary = nlp.summarize(wiki_object.title, wiki_object.content)
        for each in summary:
            each = "--" + each
            safeprint(each)
            safeprint(" ")
        quit()
    else:
        safeprint(wiki_object.content)