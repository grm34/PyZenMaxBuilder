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
from datetime import datetime

from modules.obtainer.defconfigs import get_defconfig_files
from modules.obtainer.devices import get_devices, get_device_data
from modules.obtainer.images import get_kernel_img
from modules.obtainer.processor import get_processor
from modules.obtainer.version import get_kernel_version
from modules.obtainer.zips import get_flashable_zips


def global_settings(self):
    """Define `global settings`

    Returns
    -------
        "Updated dictonary of the required settings"
    """

    # Date
    self.session['build_date'] = datetime.now().date().isoformat()
    self.session['time'] = datetime.now().strftime('%Hh%Mm%Ss')
    self.session['datetime'] = '{date}_{time}'.format(
        date=self.session['build_date'],
        time=self.session['time']
    )

    # Folders
    self.session['zip_folder'] = '{out}/{path}'.format(
        out=os.getcwd(),
        path=self.session['zip_folder']
    )
    self.session['out_folder'] = '{out}/{path}'.format(
        out=os.getcwd(),
        path=self.session['out_folder']
    )
    self.session['defconfig_folder'] = '{kernel}/{configs}'.format(
        kernel=self.session['kernel_folder'],
        configs=self.session['defconfig_folder']
    )


def mode_settings(self):
    """Get required `settings` by `MODE`

    Returns
    -------
        "Updated dictonary of the required settings"
    """

    # [NEWBUILD]
    if self.session['mode'] == 'newbuild':
        self.session['defconfig_list'] = get_defconfig_files(self)
        logging.info(self.trad('checking current kernel version...'))
        self.session['kernel_version'] = get_kernel_version(self)
        self.session['cpu'] = get_processor(self)
        if self.session['device_codename'] == '':
            self.devices = get_devices(self)

    # [MENUCONFIG]
    elif self.session['mode'] == 'menuconfig':
        self.session['defconfig_list'] = get_defconfig_files(self)
        logging.info(self.trad('checking current kernel version...'))
        self.session['kernel_version'] = get_kernel_version(self)

    # [MAKEZIP]
    elif self.session['mode'] == 'makezip':
        self.session['kernel_img_list'] = get_kernel_img(self)
        logging.info(self.trad('checking current kernel version...'))
        self.session['kernel_version'] = get_kernel_version(self)
        if self.session['device_codename'] == '':
            self.devices = get_devices(self)

    # [ZIPSIGNER]
    elif self.session['mode'] == 'zipsigner':
        self.session['zip_list'] = get_flashable_zips(self)

    # [MODE] makeclean
    elif self.session['mode'] == 'makeclean':
        logging.info(self.trad('checking current kernel version...'))
        self.session['kernel_version'] = get_kernel_version(self)


def session_settings(self):
    """Get and define `session settings`

    Returns
    -------
        "Updated dictonary of the required settings"
    """

    # Set variables [newbuild] [makezip]
    if self.session['mode'] in ['newbuild', 'makezip']:

        # Device
        if self.session['device_codename'] == '':
            self.session['device_codename'] = (
                self.session['answers']['codename']
            )
        get_device_data(self)

        # Build name
        self.session['build_name'] = '{team}{kv}-{codename}-{date}'.format(
            team=('{0}-'.format(self.session['kernel_name'])
                  if self.session['kernel_name'] != '' else ''),
            codename=self.session['device_codename'],
            kv=self.session['kernel_version'],
            date=self.session['build_date']
        )
