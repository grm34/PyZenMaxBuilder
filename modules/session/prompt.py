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
import os
import sys

import inquirer
from inquirer.themes import load_theme_from_dict
from modules.inquirer.mode import app_mode
from modules.inquirer.session import app_session


def ask_for_mode(self):
    """Run `inquirer` mode

    Functions
    ---------
        `app_mode`: "application mode selection"

    Returns
    -------
        "string containing the selected mode"
    """
    current_session = inquirer.prompt(
        app_mode(self),
        theme=load_theme_from_dict(self.theme)
    )

    if current_session['mode'] == 'quit':
        sys.exit(0)

    self.session['mode'] = current_session['mode']


def ask_questions(self):
    """Run `inquirer` session

    Functions
    ---------
        `app_session`: "application questions"

    Returns
    -------
        "Dictionary containing user's answers"
    """

    # Ask questions to the user
    self.session['answers'] = inquirer.prompt(
        app_session(self), theme=load_theme_from_dict(self.theme)
    )

    # Get confirm status for [newbuild] [makezip] [zipsigner]
    confirm = True
    confirm_list = [
        self.session['answers']['confirm_newbuild'],
        self.session['answers']['confirm_makezip'],
        self.session['answers']['confirm_zipsigner'],
    ]

    for response in confirm_list:
        if response is False:
            confirm = False

    # Set confirm status for [makeclean] [menuconfig]
    if (self.session['answers']['cleanbuild'] is False
            and self.session['mode'] == 'makeclean') or (
                self.session['answers']['menuconfig'] is False
                and self.session['mode'] == 'menuconfig'):
        confirm = False

    # Restart new session?
    if confirm is False:
        del self
        os.execl(sys.executable, sys.executable, * sys.argv)
