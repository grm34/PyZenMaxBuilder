# -*- coding: utf-8 -*-

"""
    ZenMaxBuilder Copyright © 2021 darkmaster@grm34 https://github.com/grm34

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import logging

from termcolor import cprint


def app_banner(self):
    """Display `ASCII banner` of the application

    Modules
    -------
        termcolor: "ANSII Color formatting for output in terminal"

    SubModules
    ----------
        cprint: "Print colorize text"

    Actions
    -------
        1) "Print title with a short description of the application"
    """
    for key in range(7):

        cprint(
            self.app['ascii{key}'.format(key=key)],
            'blue',
            attrs=['bold']
        )

    logging.info(self.trad(
        '  Arrow keys to navigate    ↓\n \
                   Space to select options   ↔\n \
                   Enter to confirm          ⇲\n'))
