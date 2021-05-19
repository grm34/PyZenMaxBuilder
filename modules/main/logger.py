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

import coloredlogs


def app_logger():
    """Application `logger`

    Modules
    -------
        logging: "Logging package for Python. Based on PEP 282"

    Actions
    -------
        1) "Write logs to file"
        2) "Display logs in terminal"
    """

    # Create a StreamHandler wich write to sys.stderr
    level = '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d [%(funcName)s]'
    message = '{level} %(message)s'.format(level=level)

    logging.basicConfig(
        filename='zmb.log',
        level=logging.DEBUG,
        filemode='w',
        format=message
    )

    # Create a logger for terminal output
    console = logging.getLogger()

    coloredlogs.install(
        level='INFO',
        logger=console,
        datefmt='%H:%M:%S',
        fmt='[%(asctime)s] %(levelname)s ➡ %(message)s',
        level_styles={
            'critical': {'color': 'red', 'bold': True},
            'debug': {'color': 'magenta', 'bold': False},
            'error': {'color': 'red', 'bold': False},
            'info': {'color': 'cyan', 'bold': False},
            'warning': {'color': 'yellow', 'bold': True}
        },
        field_styles={
            'levelname': {'bold': True, 'color': 'magenta'},
            'asctime': {'color': 'yellow'}
        }
    )
