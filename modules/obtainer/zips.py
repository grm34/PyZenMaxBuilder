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


def get_flashable_zips(self):
    """Get kernel `flashable zips`

    Functions
    ---------
        `command_output`: "Subprocess `check_output` with return codes"

    Actions
    -------
        1) "ls {zip} | grep '.zip' | grep -v 'signed'"

    Returns
    -------
        output: "Array containing flashable zips or Boolean"
    """
    cmd = 'ls {zip} | grep ".zip" | grep -v "signed"'.format(
        zip=self.session['zip_folder']
    )

    output = command_output(
        cmd,
        exit_on_error=True,
        error=self.trad('no flashable zip found in: {path}').format(
            path=self.session['zip_folder']
        ),
        warning=self.trad(
            'use --zip-folder option or edit app/settings.py'
        )
    )

    if output is not False:
        output = list(filter(None, output.split('\n')))

    return output
