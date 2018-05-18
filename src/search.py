from __future__ import print_function, unicode_literals

import sys

from workflow import Workflow, web, ICON_ERROR, ICON_SETTINGS

from utils import parse_args, is_match
from settings import UPDATE_SETTINGS, HELP_URL, LEETCODE_URL, LC_TOPICS


class SearchResult(object):
    def __init__(self, title, subtitle, url):
        self.title_ = title
        self.subtitle_ = subtitle
        self.url_ = url


def search_topic(args):
    results = []

    query = args["query"]
    difficulty_api = "difficulty=" + args["difficulty"] if args["difficulty"] else ""
    difficulty = "[%s]" % args["difficulty"] if args["difficulty"] else ""

    for k, v in LC_TOPICS.items():
        if is_match(query, k):
            title = "%s %s" % (v[0], difficulty)
            subtitle = "Search LeetCode Topic '%s' %s" % (v[0], difficulty)
            url = "{0}?topicSlugs={1}&{2}".format(LEETCODE_URL, v[1], difficulty_api)

            results.append( SearchResult(title, subtitle, url) )

    if not results:
        title = query
        subtitle = "Search LeetCode for '%s'" % query
        url = "{0}?search={1}".format(LEETCODE_URL, query)

        results.append( SearchResult(title, subtitle, url) )

    return results


def search_prob(args):
    query = args["query"] if args["query"] else "..."
    difficulty_api = "difficulty=" + args["difficulty"] if args["difficulty"] else ""
    difficulty = "[%s]" % args["difficulty"] if args["difficulty"] else ""

    title = title = "%s %s" % (query, difficulty)
    subtitle = "Search LeetCode for '%s' %s" % (query, difficulty)
    url = "{0}?search={1}&{2}".format(LEETCODE_URL, query, difficulty_api)

    result = SearchResult(title, subtitle, url)
    
    return [result] 


def main(wf):
    args = parse_args(wf.args)

    if args["mode"] == "topic":
        results = search_topic(args)
    elif args["mode"] == "problem":
        results = search_prob(args)

    for res in results:
        wf.add_item(
            title=res.title_,
            subtitle=res.subtitle_,
            valid=True,
            uid=res.url_,
            arg=res.url_
        )

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(update_settings=UPDATE_SETTINGS, help_url=HELP_URL)
    sys.exit( wf.run(main) )