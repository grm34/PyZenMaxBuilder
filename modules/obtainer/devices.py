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

from ..manager.json import api_json_output


def get_devices(self):
    """Get `android devices` list

    Functions
    ---------
        `api_json_output`: "JSON API url parser"

    Returns
    -------
        "Dictionary containing android devices codenames"
    """
    logging.info(self.trad('Get android devices list...'))

    return api_json_output(
        '{api}'.format(api=self.session['devices']),
        exit_on_error=True,
        error=self.trad('failed to get android devices list'),
        warning=self.trad(
            'use --codename option or edit app/settings.py'
        ),
        timeout=1
    )


def get_device_data(self):
    """Search for device data in `self.devices`

    Returns
    -------
        "android device name and model from codename"
    """
    device_data = []

    for device in self.devices:
        for value in device.items():

            if self.session['device_codename'] in value:
                device_data.append(device)

    if device_data:

        if self.session['device_name'] == '':
            self.session['device_name'] = (
                device_data[0]['name'].replace('  ', ' ').split('/')[0]
            )

        if self.session['device_model'] == '':
            self.session['device_model'] = (
                device_data[0]['model'].replace('  ', ' ').split('/')[0]
            )

    if self.session['device_name'] == '':
        self.session['device_name'] = self.session['device_codename']

    if self.session['device_model'] == '':
        self.session['device_model'] = self.session['device_codename']
