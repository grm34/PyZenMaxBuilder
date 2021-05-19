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
import argparse

from termcolor import colored


def app_helper(self):
    """Application `usage` and `command line` options

    Modules
    -------
        argparse: "Argument handler for parsing command line strings"

    Options
    -------
        help: "display usage and exit"
        debug: "run DEBUG mode"
        theme: "application theme selection"
        lang: "application language selection"
        device: "specify device name"
        codename: "specify device codename"
        kernel: "specify kernel name"
        kernel-folder: "specify kernel folder"
        defconfig-folder: "specify defconfig foder"
        out-folder: "specify out folder"
        img-folder: "specify kernel image folder"
        zip-folder: "specify flashable zip folder"

    Returns
    -------
        options: "Tuple containing command line options from sys.argv"
    """

    # Parser
    parser = argparse.ArgumentParser(
        prog=colored(
            self.app['name'],
            'green',
            attrs=['bold']
        ),
        usage=colored(
            self.app['usage'],
            'red',
            'on_white',
            attrs=['blink']
        ),
        epilog=colored(
            'More information at {url}'.format(
                url=colored(self.app['url'], 'cyan', attrs=['bold'])
            ),
            'white',
            attrs=['bold']
        )
    )

    # optional arguments
    parser.add_argument(
        '--debug',
        nargs=1,
        choices=['on', 'off'],
        default='off',
        help='run DEBUG mode (print session and exit)'
    )
    parser.add_argument(
        '--theme',
        nargs=1,
        choices=['sun', 'x', 'snow'],
        help='theme selection (useless but essential)'
    )
    parser.add_argument(
        '--lang',
        nargs=1,
        choices=['en', 'fr'],
        help='language selection (default: host locales)'
    )

    # ZenMaxBuilder options
    zenmax = parser.add_argument_group(
        title='ZenMaxBuilder options',
        description=None
    )
    zenmax.add_argument(
        '--device',
        nargs=1,
        metavar='',
        dest='name',
        help='device name (e.q. ASUS ZenFone Max Pro M1)'
    )
    zenmax.add_argument(
        '--codename',
        nargs=1,
        metavar='',
        dest='codename',
        help='device codename (e.q. X00TD, lavender)'
    )
    zenmax.add_argument(
        '--kernel',
        nargs=1,
        metavar='',
        dest='kernel',
        help='kernel name (e.q. MyFavoriteKernel)'
    )
    zenmax.add_argument(
        '--kernel-folder',
        nargs=1,
        metavar='',
        dest='k_folder',
        help='path to the kernel to build (e.q. /home/mykernel)'
    )
    zenmax.add_argument(
        '--defconfig-folder',
        nargs=1,
        metavar='',
        dest='d_folder',
        help='path to defconfig folder (default: arch/arm64/configs)'
    )
    zenmax.add_argument(
        '--out-folder',
        nargs=1,
        metavar='',
        dest='out_folder',
        help='path to make folder [OUT] (default: android/out)'
    )
    zenmax.add_argument(
        '--img-folder',
        nargs=1,
        metavar='',
        dest='kb_folder',
        help='path to the kernel img folder [BOOT]'
    )
    zenmax.add_argument(
        '--zip-folder',
        nargs=1,
        metavar='',
        dest='zip_folder',
        help='path to the kernel zip files (default: android/builds)'
    )

    return parser.parse_args()
