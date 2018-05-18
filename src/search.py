from __future__ import print_function, unicode_literals

import sys


from workflow import Workflow, web, ICON_ERROR, ICON_SETTINGS

import utils
import settings


def main(wf):
    args = utils.parse_args(wf.args)
    wf.logger.debug(args)

    url = "https://leetcode.com/problemset/all/"
    wf.add_item(title="lala", subtitle="asd", valid=True, uid=url, arg=url)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow(update_settings=settings.UPDATE_SETTINGS, 
        help_url=settings.HELP_URL)

    sys.exit( wf.run(main) )