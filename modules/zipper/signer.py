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


def zip_signer(self):
    """Sign `flashable zip` with zpsigner.jar

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "java -jar zipsigner.jar {in} {out}"
    """

    if not isinstance(self.session['build_name'], list):
        build_list = [self.session['build_name']]
        self.session['build_name'] = build_list

    for kernel in self.session['build_name']:
        kernel = kernel.replace('.zip', '')

        logging.info(
            self.trad('signing {zip}.zip...').format(zip=kernel)
        )

        run_command(
            'java -jar {sign} {out}/{zip}.zip {out}/{zip}-signed.zip'.format(
                sign='android/tools/zipsigner.jar',
                zip=kernel,
                out=self.session['zip_folder']
            ),
            exit_on_error=True
        )

        logging.info(self.trad('successfully signed !'))
