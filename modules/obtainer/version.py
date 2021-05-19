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
import re

from ..manager.cmd import command_output


def get_kernel_version(self):
    """Get `kernel version`

    Functions
    ----------
        `command_output`: "Subprocess `check_output` with return codes"

    Actions
    -------
        1) "make kernelversion"

    Returns
    -------
        output: "String containing the version of the kernel or Boolean"
    """
    output = command_output(
        'make kernelversion',
        path=self.session['kernel_folder'],
        exit_on_error=True,
        error=self.trad('failed to make kernel version')
    )

    if output is not False:

        output = output.split('\n')[0].split(': ')[-1]
        output = re.sub(' +', ' ', output)

    return output
