import feedparser
import datetime
import delorean
import json


def main():
    rss_marca = feedparser.parse('https://e00-marca.uecdn.es/rss/portada.xml')
    rss_as = feedparser.parse('https://as.com/rss/tags/ultimas_noticias.xml')
    rss = [rss_marca, rss_as]
    entries = []

    for feed in rss:
        time_limit = delorean.parse(
            feed.channel.updated) - datetime.timedelta(hours=6)
        entries += [entry for entry in feed.entries if delorean.parse(
            entry.published) > time_limit]

    rss = json.dumps(
        sorted(entries, key=lambda item: item['published_parsed']))

    print(rss)


if __name__ == '__main__':
    main()
