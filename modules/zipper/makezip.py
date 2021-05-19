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

from ..manager.cmd import command_output, run_command


def copy_to_anykernel(self):
    """Copy `kernel image` to AnyKernel folder

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "cp Image.gz-dtb AnyKernel/"
    """
    logging.info(self.trad('copy kernel image to AnyKernel...'))

    if self.session['mode'] == 'newbuild':

        img = '{out}/arch/arm64/boot/Image.gz-dtb'.format(
            out=self.session['out_folder']
        )

    else:

        img = '{img_folder}/{image}'.format(
            img_folder=self.session['kernel_img_folder'],
            image=self.session['answers']['makezip']
        )

    run_command(
        'cp {img} android/AnyKernel'.format(img=img),
        exit_on_error=True
    )


def make_flashable_zip(self):
    """Make `flashable zip` with AnyKernel

    Functions
    ---------
        `command_output`: "Subprocess check_output with return codes"

    Actions
    -------
        1) "zip -r9 {build}.zip * -x .git README.md *placeholder"
        2) "mv {build}.zip android/builds"
        3) "rm AnyKernel/*.gz-dtb"
    """
    kernel = self.session['build_name'].replace('.zip', '')

    logging.info(
        self.trad('creating {build}.zip...').format(build=kernel)
    )

    cmd_list = (
        'zip -r9 {build}.zip * -x .git README.md *placeholder'.format(
            build=kernel
        ),
        'mv *.zip {path}'.format(path=self.session['zip_folder']
        ),
        'rm *.gz-dtb'
    )

    for cmd in cmd_list:

        command_output(
            cmd,
            path='android/AnyKernel',
            exit_on_error=True
        )

    logging.info(self.trad('successfully zipped !'))
    logging.info(self.trad('AnyKernel folder cleaned !'))
