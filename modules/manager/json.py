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
import json
import logging

from requests import ConnectionError as ConnectError
from requests import ConnectTimeout, ReadTimeout, get

from .exit import app_exit


def api_json_output(
        url, exit_on_error=False, error=None, warning=None, timeout=None):
    """JSON API `url parser`

    Arguments
    ---------
        url: "String containing the url to parse"

    Keyword Arguments
    -----------------
        `exit_on_error`: "Boolean to exit on exception" (default: False)
        error: "String to set custom error message" (default: None)
        warning: "String to set custom warning message" (default: None)
        timeout: "Integer to set timeout expired exception" (default: None)

    Returns
    -------
        "Dictionary containing the json output"
    """
    try:
        output = get(url, timeout=timeout).json()

    except (ConnectError, ConnectTimeout, ReadTimeout) as url_error:

        if error is not None:
            url_error = error

        logging.error(url_error)

        if warning is not None:
            logging.warning(warning)

        if exit_on_error is True:
            app_exit()

    return output


def load_json_file(file):
    """JSON LOAD `file parser`

    Arguments
    ---------
        file: "String containing the file to parse"

    Returns
    -------
        "Dictionary containing the json file values"
    """
    with open(
            'app/{file}'.format(file=file), 'r', encoding='utf-8'
    ) as out:

        output = json.load(out)

    return output


def dump_json_file(dictionary, file):
    """JSON DUMP store `dictionary` to JSON `file`

    Arguments
    ---------
        dictionary: "String containing the dictionary to store"
        file: "String containing the JSON file"

    Actions
    -------
        1) "Store the desired dictionary to the desired JSON file"
    """
    with open(
        'android/logs/{file}'.format(
            file=file), 'w', encoding='utf-8'
    ) as log:

        json.dump(dictionary, log, ensure_ascii=False, indent=4)
