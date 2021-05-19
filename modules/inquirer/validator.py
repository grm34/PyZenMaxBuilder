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

from termcolor import colored

from inquirer.errors import ValidationError


def defconfig_validator(self, response):
    """Match regex to `validate` any_defconfig name

    Arguments
    ---------
        response: "String containing current answer"

    Raises
    ------
        ValidationError: "Display a short description with available formats"

    Returns
    -------
        boolean: True
    """
    if not re.match(r'^[a-z]{1}[a-z0-9-_]{1,15}_defconfig$', response):

        raise ValidationError(
            '',
            reason=colored(
                self.trad(
                    'Invalid defconfig name: {response} (e.q., new_defconfig)'
                ).format(
                    response=colored(response, 'yellow', attrs=['bold'])
                ),
                'red',
                attrs=['bold']
            )
        )

    return True


def codename_validator(self, response):
    """Match valid `codename` on android-device-list repository

    Arguments
    ---------
        response: "String containing current answer"

    Raises
    ------
        ValidationError: "Display a short description with available formats"

    Returns
    -------
        boolean: True
    """
    codenames = []

    for device in self.devices:
        codenames.append('{model}'.format(model=device['model']))
        codenames.append('{device}'.format(device=device['device']))

    if response not in codenames or response == '':

        raise ValidationError(
            '',
            reason=colored(
                self.trad(
                    'Invalid device codename: {response} (e.q., ASUS_X00TD)'
                ).format(
                    response=colored(response, 'yellow', attrs=['bold'])
                ),
                'red',
                attrs=['bold']
            )
        )

    return True


def cores_validator(self, response):
    """Match valid amount of `CPU cores`

    Arguments
    ---------
        response: "String containing current answer"

    Raises
    ------
        ValidationError: "Display a short description with available formats"

    Returns
    -------
        boolean: True
    """
    if (response > self.session['cpu']['cores']
            or response == '' or response == '0'):

        raise ValidationError(
            '',
            reason=colored(
                self.trad(
                    'Invalid entry: {response} ﴾{proc} ➟ {cores} CORE(s)﴿'
                ).format(
                    response=colored(response, 'yellow', attrs=['bold']),
                    proc=self.session['cpu']['name'],
                    cores=colored(
                        self.session['cpu']['cores'],
                        'red',
                        attrs=['bold']
                    )
                ),
                'red',
                attrs=['bold'])
        )

    return True


def checkbox_validator(self, response):
    """Match any `checkbox selection` but `raise error` on empty

    Arguments
    ---------
        response: "String containing current answer"

    Raises
    ------
        ValidationError: "Display a short description with available formats"

    Returns
    -------
        boolean: True
    """
    if response == []:

        raise ValidationError(
            '',
            reason=colored(
                self.trad('You must select at least one element...'),
                'red',
                attrs=['bold'])
        )

    return True
