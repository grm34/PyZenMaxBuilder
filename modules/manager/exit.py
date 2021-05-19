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
import sys
import time

from termcolor import cprint


def app_exit():
    """Application `clean exit`

    Modules
    -------
        os: "exports all functions from posix or nt, e.g. unlink, stat, etc"
        sys: "provides access to some objects by the interpreter"
        time: "various functions to manipulate time values"

    Actions
    -------
        1) "Exit the application with 5s timeout"
    """

    for second in range(5, 0, -1):

        message = 'Exiting in {second}s...'.format(second=str(second))

        cprint(message, 'yellow', end='\r')
        time.sleep(1)

    sys.exit(0)
