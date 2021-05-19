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


def download_zipsigner(self):
    """Download JAVA `ZipSigner`

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "wget {zipsigner}.jar"
    """
    if os.path.isfile('android/tools/zipsigner.jar') is False:

        logging.info(self.trad('downloading ZipSigner in android/tools...'))

        run_command(
            'wget -O zipsigner.jar --quiet --show-progress {url}'.format(
                url=self.session['zipsigner_url']
            ),
            exit_on_error=True,
            path='{path}/android/tools'.format(path=os.getcwd()),
            error=self.trad('failed to download Zipsigner!')
        )
