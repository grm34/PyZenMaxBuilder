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


def clone_toolchains(self):
    """Clone salected compiler `toolchain`

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "git clone {toolchain}.git"
    """

    # Define toolchains to clone
    if self.session['answers']['compiler'] == 'gcc':
        toolchain_urls = ['gcc32_url', 'gcc64_url']

    elif self.session['answers']['compiler'] == 'clang':
        toolchain_urls = ['clang_url', 'gcc64_url']

    else:
        toolchain_urls = ['proton_url']

    # Clone missing toolchains
    for toolchain in toolchain_urls:

        if os.path.isdir(
            'android/toolchains/{path}'.format(
                path=toolchain.replace('_url', '')
            )
        ) is False:

            logging.info(
                self.trad('cloning {toolchain} in android/toolchains...')
                .format(toolchain=toolchain.replace('_url', ''))
            )

            run_command(
                'git clone {url} {name}'.format(
                    url=self.session[toolchain],
                    name=toolchain.replace('_url', '')
                ),
                exit_on_error=True,
                path='{path}/android/toolchains'.format(path=os.getcwd()),
                error=self.trad('failed to clone {toolchain}!')
                .format(toolchain=toolchain.replace('_url', ''))
            )
