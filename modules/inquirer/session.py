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
from termcolor import colored

import inquirer

from .validator import checkbox_validator, codename_validator, cores_validator


def app_session(self):
    """Application global `questions`

    Modules
    -------
        inquirer: "Common interactive command line user interface"

    Functions
    ---------
        `checkbox_validator`: "Match any checkbox selection"
        `codename_validator`: "Match codename on android-device-list git"
        `cores_validator`: "Match valid amount of CPU cores"

    Actions
    -------
        1) "Ask some questions to the user"

    Returns
    -------
        "Dictionary containing user answers"
    """
    return [

        # Device codename
        inquirer.Text(
            'codename',
            message=colored(
                self.trad('Enter device codename (e.q. ASUS_X00TD)'),
                'green',
                attrs=['bold']
            ),
            validate=lambda _, response:
                codename_validator(self, response),
            ignore=lambda user:
                self.session['device_codename'] != ''
                or self.session['mode'] in [
                    'zipsigner', 'menuconfig', 'makeclean'
            ]
        ),

        # Toolchain compiler
        inquirer.List(
            'compiler',
            message=colored(
                self.trad('Select the compiler to use'),
                'green',
                attrs=['bold']
            ),
            choices=[
                ('Proton Clang', 'proton'),
                ('Clang Stable', 'clang'),
                ('GNU Compiler Collection', 'gcc')
            ],
            carousel=True,
            ignore=lambda user: 'newbuild' not in self.session['mode']
        ),

        # Defconfig file
        inquirer.List(
            'defconfig',
            message=colored(
                self.trad('Select the defconfig to use'),
                'green',
                attrs=['bold']
            ),
            choices=self.session['defconfig_list'],
            carousel=True,
            ignore=lambda user:
                self.session['mode'] not in ['newbuild', 'menuconfig']
        ),

        # Flashable zip
        inquirer.List(
            'makezip',
            message=colored(
                self.trad('Select the kernel image to zip'),
                'green',
                attrs=['bold']
            ),
            choices=self.session['kernel_img_list'],
            carousel=True,
            ignore=lambda user:
                'makezip' not in self.session['mode']
        ),

        # Zipsigner
        inquirer.Checkbox(
            'zipsigner',
            message=colored(
                self.trad('Select the zip(s) to sign'),
                'green',
                attrs=['bold']
            ),
            choices=self.session['zip_list'],
            validate=lambda _, response:
                checkbox_validator(self, response),
            ignore=lambda user:
                'zipsigner' not in self.session['mode']
        ),

        # Menuconfig
        inquirer.Confirm(
            'menuconfig',
            message=colored(
                self.trad('Do you wish to edit {defconfig} with menuconfig'),
                'green',
                attrs=['bold']
            ),
            default=False,
            ignore=lambda user:
                self.session['mode'] not in ['newbuild', 'menuconfig']
        ),

        # CPU Cores
        inquirer.Confirm(
            'cpu',
            message=colored(
                self.trad('Do you wish to use all cores ➡ {proc}').format(
                    proc=self.session['cpu']['name']
                ),
                'green',
                attrs=['bold']
            ),
            default=True,
            ignore=lambda user: 'newbuild' not in self.session['mode']
        ),

        # Amount of Cores
        inquirer.Text(
            'cores',
            message=colored(
                self.trad('Enter the amount of CPU cores to use'),
                'green',
                attrs=['bold']
            ),
            validate=lambda _, response:
                cores_validator(self, response),
            ignore=lambda user:
                user['cpu'] is True
                or 'newbuild' not in self.session['mode']
        ),

        # Clean build
        inquirer.Confirm(
            'cleanbuild',
            message=colored(
                self.trad(
                    'Do you wish to make clean & mrproper ➡ {kv}'
                ).format(
                    kv=self.session['kernel_version']
                ),
                'green',
                attrs=['bold']
            ),
            default=False,
            ignore=lambda user:
                self.session['mode'] not in ['newbuild', 'makeclean']
        ),

        # Confirm new build
        inquirer.Confirm(
            'confirm_newbuild',
            message=colored(
                self.trad(
                    'Do you wish to start new build ➡ {team}{codename}-{kv}'
                ).format(
                    team=('{0}-'.format(self.session['kernel_name'])
                          if self.session['kernel_name'] != ''
                          else ''
                          ),
                    codename=(self.session['device_codename']
                              if self.session['device_codename'] != ''
                              else '{codename}'
                              ),
                    kv=self.session['kernel_version']
                ),
                'green',
                attrs=['bold']
            ),
            default=True,
            ignore=lambda user: 'newbuild' not in self.session['mode']
        ),

        # Confirm make zip
        inquirer.Confirm(
            'confirm_makezip',
            message=colored(
                self.trad('Do you wish to zip selected kernel image'),
                'green',
                attrs=['bold']
            ),
            default=True,
            ignore=lambda user: 'makezip' not in self.session['mode']
        ),

        # Confirm sign zip
        inquirer.Confirm(
            'confirm_zipsigner',
            message=colored(
                self.trad('Do you wish to sign selected kernel(s)'),
                'green',
                attrs=['bold']
            ),
            default=True,
            ignore=lambda user: 'zipsigner' not in self.session['mode']
        )
    ]
