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

from ..manager.cmd import run_command


def clone_anykernel(self):
    """Clone `AnyKernel` repository

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "git clone {AnyKernel}.git"
    """
    if os.path.isdir('android/AnyKernel') is False:

        logging.info(
            self.trad('cloning AnyKernel in android...')
        )

        run_command(
            'git clone {url} AnyKernel'.format(
                url=self.session['anykernel_url']
            ),
            exit_on_error=True,
            path='{path}/android'.format(path=os.getcwd()),
            error=self.trad('failed to clone AnyKernel!')
        )
