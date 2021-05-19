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

from ..manager.cmd import command_output
from ..manager.exit import app_exit


def make_clean(self):
    """Clean the `kernel` tree

    Functions
    ---------
        `command_output`: "Subprocess check_output with return codes"

    Actions:
    --------
        1) "make clean"
        2) "make mrproper"
        2) "rm -rf {out_folder} && mkdir {out_folder}"
    """

    # Make clean
    logging.info(
        self.trad('make clean and MrProper ({version})...')
        .format(version=self.session['kernel_version'])
    )

    cmd = (
        'make -C {kernel} clean && make -C {kernel} mrproper'
        .format(kernel=self.session['kernel_folder'])
    )

    try:
        os.system(cmd)

    except OSError:
        app_exit()

    # Rmdir out folder
    logging.info(
        self.trad('cleaning {out}...').format(out=self.session['out_folder'])
    )

    cmd = 'rm -rf {out} && mkdir {out}'.format(
        out=self.session['out_folder']
    )
    command_output(cmd, exit_on_error=True)
    logging.info(self.trad('successfully cleaned !'))
