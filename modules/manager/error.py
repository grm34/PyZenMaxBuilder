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
import sys

from .exit import app_exit


def prevent_wrong_usage():
    """Prevent `wrong usage` of the application

    Actions
    -------
        1) "Check for Linux operating system"
        2) "Check if application is run from its path"
        3) "Display error message and exit"
    """

    # Prevent non Linux users
    if os.uname().sysname != 'Linux':

        logging.error('this script must be run on a Linux Operating System !')
        sys.exit(0)

    # Prevent running script from another folder
    if os.path.isfile('modules/manager/error.py') is False:

        logging.error('this script must be run from ZenMaxBuilder folder !')
        sys.exit(0)


def prevent_kernel_folder(self):
    """Prevent invalid `kernel folder`

    Functions
    ----------
        `app_exit`: "Exit the application with 5s timeout"

    Actions
    -------
        1) "Check if path is folder"
        2) "Check if path is a kernel folder"
    """

    # Prevent invalid kernel folder"""
    if os.path.isdir(self.session['kernel_folder']) is False:

        logging.error(
            self.trad('[kernel] {path} not found !').format(
                path=self.session['kernel_folder']
            )
        )
        logging.warning(
            self.trad('use --kernel-folder option or edit app/settings.py')
        )
        app_exit()

    # Prevent invalid kernel tree
    if (os.path.isfile('{path}/kernel/configs/android-base.config'
                       .format(path=self.session['kernel_folder'])
                       ) is False
        or os.path.isfile('{path}/AndroidKernel.mk'
                          .format(path=self.session['kernel_folder'])
                          ) is False):

        logging.error(
            self.trad('[kernel] {path} is not an android kernel tree !')
            .format(path=self.session['kernel_folder'])
        )
        app_exit()


def prevent_defconfig_folder(self):
    """Prevent invalid `defconfig folder`

    Functions
    ----------
        `app_exit`: "Exit the application with 5s timeout"

    Actions
    -------
        1) "Check if path is folder"
    """
    if os.path.isdir(self.session['defconfig_folder']) is False:

        logging.error(
            self.trad('[defconfig] {path} not found !').format(
                path=self.session['defconfig_folder']
            )
        )
        logging.warning(
            self.trad('use --defconfig-folder option or edit app/settings.py')
        )
        app_exit()


def prevent_out_folder(self):
    """Prevent invalid `OUT folder`

    Functions
    ----------
        `app_exit`: "Exit the application with 5s timeout"

    Actions
    -------
        1) "Check if path is folder"
    """
    if os.path.isdir(self.session['out_folder']) is False:

        logging.error(
            self.trad('[out] {path} not found !').format(
                path=self.session['out_folder']
            )
        )
        logging.warning(
            self.trad('use --out-folder option or edit app/settings.py')
        )
        app_exit()


def prevent_img_folder(self):
    """Prevent invalid `kernel image folder`

    Functions
    ----------
        `app_exit`: "Exit the application with 5s timeout"

    Actions
    -------
        1) "Check if path is folder"
    """
    if (self.session['kernel_img_folder'] != 'None'
            and os.path.isdir(self.session['kernel_img_folder']) is False):

        logging.error(
            self.trad('[kernel img] {path} not found !').format(
                path=self.session['kernel_img_folder']
            )
        )
        app_exit()


def prevent_zip_folder(self):
    """Prevent invalid `ZIP folder`

    Functions
    ----------
        `app_exit`: "Exit the application with 5s timeout"

    Actions
    -------
        1) "Check if path is folder"
    """
    if os.path.isdir(self.session['zip_folder']) is False:

        logging.error(
            self.trad('[zip] {path} not found !').format(
                path=self.session['zip_folder']
            )
        )
        logging.warning(
            self.trad('use --zip-folder option or edit app/settings.py')
        )
        app_exit()


def prevent_android_folder():
    """Prevent missing `android folder` (working dir)

    Actions
    -------
        1) "Check if required folders exists"
        2) "Create missing folders"
    """

    paths = [
        'android',
        'android/builds',
        'android/logs',
        'android/out',
        'android/toolchains',
        'android/tools',
    ]

    for path in paths:

        if os.path.isdir(path) is False:
            os.mkdir(path)
