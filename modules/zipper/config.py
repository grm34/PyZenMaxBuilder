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


def config_anykernel(self):
    """Add `kernel informations` to AnyKernel script

    Functions
    ---------
        `run_command`: "Subprocess Popen with console output"

    Actions
    -------
        1) "Make a copy of ZenMaxBuilder.sh"
        2) "Edit copy to add kernel informations"
    """
    logging.info(self.trad('configuring anykernel...'))

    strings = [
        's/kernel.string=.*/kernel.string={name}/g'.format(
            name=self.session['build_name']
        ),
        's/kernel.for=.*/kernel.for={variant}/g'.format(
            variant=self.session['kernel_variant']
        ),
        's/kernel.compiler=.*/kernel.compiler={compiler}/g'.format(
            compiler=self.session['answers']['compiler']
        ),
        's/kernel.made=.*/kernel.made={builder}/g'.format(
            builder=self.session['builder']
        ),
        's/kernel.version=.*/kernel.version={version}/g'.format(
            version=self.session['kernel_version']
        ),
        's/message.word=.*/message.word={msg}/g'.format(
            msg=self.session['kernel_msg']
        ),
        's/build.date=.*/build.date={date}/g'.format(
            date=self.session['build_date']
        ),
        's/device.name1=.*/device.name1={name}/g'.format(
            name=self.session['device_codename']
        ),
        's/device.name2=.*/device.name2={name}/g'.format(
            name=self.session['device_name']
        ),
        's/device.name3=.*/device.name3={name}/g'.format(
            name=self.session['device_model']
        ),
        's/device.name4=.*/device.name4={name}/g'.format(
            name=self.session['device_codename']
        ),
        's/device.name5=.*/device.name5={name}/g'.format(
            name=self.session['device_name']
        ),
        's/supported.versions=.*/supported.versions={version}/g'.format(
            version=self.session['supported_android_versions']
        )
    ]

    # Copy ZenMaxBuilder.sh to anykernel.sh
    run_command(
        'cp ZenMaxBuilder.sh anykernel.sh',
        path='android/AnyKernel',
        exit_on_error=True
    )

    # Set build settings
    for string in strings:
        run_command(
            'sed -i "{string}" anykernel.sh'.format(string=string),
            path='android/AnyKernel',
            exit_on_error=True
        )
