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


def app_mode(self):
    """Application `mode` selection

    Modules
    -------
        inquirer: "Common interactive command line user interface"

    Actions
    -------
        1) "Ask which mode to use"

    Returns
    -------
        "Dictionary containing user answers"
    """
    return [

        inquirer.List(
            'mode',
            message=colored(
                self.trad('Select the desired mode'),
                'green',
                attrs=['bold']
            ),
            choices=[
                (self.trad('Build new android kernel'), 'newbuild'),
                (self.trad('Create/edit with menuconfig'), 'menuconfig'),
                (self.trad('Create flashable zip'), 'makezip'),
                (self.trad('Sign flashable zip'), 'zipsigner'),
                (self.trad('Run make clean/mrproper'), 'makeclean'),
                (self.trad('Return to terminal'), 'quit')
            ],
            carousel=True
        )
    ]
