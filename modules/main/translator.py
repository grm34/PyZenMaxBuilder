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
import gettext


def app_translator(lang):
    """Localization of the `application`

    Arguments
    ---------
        lang: "String containing application language"

    Modules
    -------
        gettext: "Internationalization and localization support"

    Returns
    -------
        trad: "Function to translate string"
    """
    language = gettext.translation(
        'ZenMaxBuilder',
        localedir='locales',
        languages=['{lang}'.format(lang=lang)]
    )

    return language.gettext
