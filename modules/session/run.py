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
from shutil import copyfile

import inquirer
from inquirer.themes import load_theme_from_dict
from modules.compiler.build import make_build
from modules.compiler.clean import make_clean
from modules.compiler.defconfig import make_defconfig
from modules.compiler.menuconfig import make_menuconfig
from modules.inquirer.save import app_save_config
from modules.manager.cmd import run_command
from modules.manager.json import dump_json_file
from modules.obtainer.compiler import get_compiler_path
from modules.zipper.config import config_anykernel
from modules.zipper.makezip import copy_to_anykernel, make_flashable_zip
from modules.zipper.signer import zip_signer


def run_session(self):
    """Application `main session`

    Actions
    -------
        1) "Make clean and mrproper"
        2) "Make defconfig"
        3) "Make menuconfig"
        4) "Make build"
        5) "Make zip"
        6) "Sign zip"
    """
    # Make clean/mrproper
    if self.session['answers']['cleanbuild'] is True:
        make_clean(self)

    # Make defconfig
    if self.session['mode'] in ['newbuild', 'menuconfig']:
        make_defconfig(self)

    # Make menuconfig
    if self.session['answers']['menuconfig'] is True:
        make_menuconfig(self)

        # Save new defconfig?
        save_config = inquirer.prompt(
            app_save_config(self),
            theme=load_theme_from_dict(self.theme)
        )
        if save_config['save'] is True:

            run_command(
                'cp {kernel}/.config {path}/{config}'.format(
                    kernel=self.session['out_folder'],
                    config=save_config['defconfig_name'],
                    path=self.session['defconfig_folder']
                ),
                exit_on_error=True
            )
            logging.info(self.trad('successfully saved'))

    # Make build
    if self.session['mode'] == 'newbuild':
        self.session['compiler_path'] = get_compiler_path(self)
        make_build(self)
        config_anykernel(self)
        copy_to_anykernel(self)
        make_flashable_zip(self)
        zip_signer(self)

        # Copy logs
        logging.info(self.trad('saving build logs to android/logs...'))
        dump_json_file(
            self.session,
            '{codename}-{date}.json'.format(
                codename=self.session['device_codename'],
                date=self.session['datetime']
            )
        )
        copyfile(
            'zmb.log',
            'android/logs/{codename}-{date}.log'.format(
                codename=self.session['device_codename'],
                date=self.session['datetime']
            )
        )

    # Make Zip
    elif self.session['mode'] == 'makezip':
        copy_to_anykernel(self)
        config_anykernel(self)
        make_flashable_zip(self)

    # Zip Signer
    elif self.session['mode'] == 'zipsigner':
        self.session['build_name'] = self.session['answers']['zipsigner']
        zip_signer(self)
