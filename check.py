import yaml
from manganelo import MangaInfo
from feedgen.feed import FeedGenerator

cstream = open('config.yaml', 'r')
config = yaml.load(cstream, Loader=yaml.FullLoader)

fg = FeedGenerator()
fg.id(config['self'])
fg.title('Manganelo RSS')
fg.subtitle('Following releases')
fg.link(href=config['self'], rel='self')
fg.language('en')

for url in config['mangas']:
    manga_info = MangaInfo(url, threaded=True)
    manga_page = manga_info.results()

    for c in manga_page.chapters[-5:]:
        fe = fg.add_entry()
        fe.id(c.url)
        fe.title(c.title + ' - ' + manga_page.title)
        fe.link(href=c.url)
        fe.source(url=url, title=manga_page.title)

fg.rss_file(config['xmlpath'])
