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
from termcolor import colored

import inquirer

from .validator import defconfig_validator


def app_save_config(self):
    """Save kernel config `confirmation`

    Modules
    -------
        inquirer: "Common interactive command line user interface"

    Functions
    ---------
        `defconfig_validator`: "Match regex to validate any defconfig name"

    Actions
    -------
        1) "Ask confirmation to save new defconfig"

    Returns
    -------
        "Dictionary containing user answers"
    """
    return [

        # Save defconfig?
        inquirer.Confirm(
            'save',
            message=colored(
                self.trad(
                    'Do you wish to save copy of modified {config}'
                )
                .format(config=self.session['answers']['defconfig']),
                'green',
                attrs=['bold']
            ),
            default=False
        ),

        # Defconfig name
        inquirer.Text(
            'defconfig_name',
            message=colored(
                self.trad('Enter defconfig name (e.q. new_defconfig)'),
                'green',
                attrs=['bold']
            ),
            validate=lambda _, response:
                defconfig_validator(self, response),
            ignore=lambda user: user['save'] is False
        )
    ]
