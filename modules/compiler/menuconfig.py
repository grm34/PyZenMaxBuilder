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

from ..manager.exit import app_exit


def make_menuconfig(self):
    """Edit kernel defconfig with `menuconfig`

    Modules
    -------
        os.system: "Execute the command in a subshell"

    Actions:
    --------
        1) "make menuconfig"
    """
    logging.info(self.trad('make menuconfig...'))

    cmd = (
        'make -C {kernel} O={out} {arch} {subarch} menuconfig {out}/.config'
        .format(
            kernel=self.session['kernel_folder'],
            out=self.session['out_folder'],
            arch=self.session['arch'],
            subarch=self.session['subarch']
        )
    )

    try:
        os.system(cmd)

    except OSError:
        app_exit()
