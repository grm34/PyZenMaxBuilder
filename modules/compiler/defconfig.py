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

from ..manager.cmd import run_command


def make_defconfig(self):
    """Make kernel `defconfig > out/.config`

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions:
    --------
        1) "make {defconfig}"
    """
    logging.info(
        self.trad('make {defconfig}...')
        .format(defconfig=self.session['answers']['defconfig'])
    )

    cmd = (
        'make O={out} {arch} {subarch} {defconfig}'
        .format(
            out=self.session['out_folder'],
            arch=self.session['arch'],
            subarch=self.session['subarch'],
            defconfig=self.session['answers']['defconfig']
        )
    )

    self.session['defconfig_command'] = cmd
    run_command(cmd, exit_on_error=True, path=self.session['kernel_folder'])
