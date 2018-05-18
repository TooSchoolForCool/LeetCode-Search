from __future__ import print_function, unicode_literals

import sys

from workflow import Workflow, web, ICON_ERROR, ICON_SETTINGS

from utils import parse_args

# Define Global Variables
UPDATE_SETTINGS = {'github_slug': 'TooSchoolForCool/LeetCode-Search'}
HELP_URL = 'https://github.com/TooSchoolForCool/LeetCode-Search/issues'

# LeetCode Algorithm Problem URL
LEETCODE_URL = "https://leetcode.com/problemset/algorithms/"


class SearchResult(object):
    def __init__(self, content, url):
        self.content_ = content
        self.url_ = url


def search_topic(args):
    results = []

    return results


def search_prob(args):
    content = args["query"]
    url = "{0}?search={1}".format(LEETCODE_URL, content)

    result = SearchResult(content, url)
    
    return [result] 


def main(wf):
    args = parse_args(wf.args)

    if args["mode"] == "topic":
        results = search_topic(args)
    elif args["mode"] == "problem":
        results = search_prob(args)

    for res in results:
        wf.add_item(
            title=res.content_,
            subtitle="Search LeetCode for {0}".format(res.content_),
            autocomplete=res.content_ + " ",
            valid=True,
            uid=res.url_,
            arg=res.url_
        )

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(update_settings=UPDATE_SETTINGS, help_url=HELP_URL)
    sys.exit( wf.run(main) )