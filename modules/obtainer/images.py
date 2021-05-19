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
from ..manager.cmd import command_output


def get_kernel_img(self):
    """Get `kernel image` files

    Functions
    ---------
        `command_output`: "Subprocess `check_output` with return codes"

    Actions
    -------
        1) "ls {out} | grep .gz-dtb"

    Returns
    -------
        output: "Array containing kernel image files or Boolean"
    """
    if self.session['kernel_img_folder'] != 'None':

        cmd = 'ls {out} | grep ".gz-dtb"'.format(
            out=self.session['kernel_img_folder']
        )

    else:
        cmd = 'ls | grep None'

    output = command_output(
        cmd,
        exit_on_error=True,
        error=self.trad('no kernel image found in: {path}').format(
            path=self.session['kernel_img_folder']
        ),
        warning=self.trad(
            'use --img-folder option or edit app/settings.py'
        )
    )

    if output is not False:
        output = list(filter(None, output.split('\n')))

    return output
