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
from modules.main.banner import app_banner
from modules.main.helper import app_helper
from modules.main.logger import app_logger
from modules.main.translator import app_translator
from modules.manager.error import (prevent_android_folder,
                                   prevent_defconfig_folder,
                                   prevent_img_folder, prevent_kernel_folder,
                                   prevent_out_folder, prevent_wrong_usage,
                                   prevent_zip_folder)
from modules.manager.exit import app_exit
from modules.manager.json import load_json_file
from modules.manager.options import options_manager
from modules.session.debug import session_debug
from modules.session.prompt import ask_for_mode, ask_questions
from modules.session.requirements import session_requirements
from modules.session.run import run_session
from modules.session.settings import (global_settings, mode_settings,
                                      session_settings)


class ZenMaxBuilder:
    """Application `main` object

    Project structure
    -----------------
        " ZenMaxBuilder.py
        " |
        " |---- modules/
        " |     |
        " |     |---- cloner/
        " |     |     |---- anykernel.py
        " |     |     |---- toolchains.py
        " |     |     |---- zipsigner.py
        " |     |
        " |     |---- compiler/
        " |     |     |---- build.py
        " |     |     |---- clean.py
        " |     |     |---- defconfig.py
        " |     |     |---- menuconfig.py
        " |     |
        " |     |---- inquirer/
        " |     |     |---- mode.py
        " |     |     |---- save.py
        " |     |     |---- session.py
        " |     |     |---- validator.py
        " |     |
        " |     |---- main/
        " |     |     |---- banner.py
        " |     |     |---- helper.py
        " |     |     |---- logger.py
        " |     |     |---- translator.py
        " |     |
        " |     |---- manager/
        " |     |     |---- cmd.py
        " |     |     |---- error.py
        " |     |     |---- exit.py
        " |     |     |---- json.py
        " |     |     |---- options.py
        " |     |
        " |     |---- obtainer/
        " |     |     |---- compiler.py
        " |     |     |---- defconfigs.py
        " |     |     |---- devices.py
        " |     |     |---- images.py
        " |     |     |---- processor.py
        " |     |     |---- version.py
        " |     |     |---- zips.py
        " |     |
        " |     |---- session/
        " |     |     |---- debug.py
        " |     |     |---- prompt.py
        " |     |     |---- requirements.py
        " |     |     |---- run.py
        " |     |     |---- settings.py
        " |     |
        " |     |---- zipper/
        " |     |     |---- config.py
        " |     |     |---- makezip.py
        " |     |     |---- signer.py
        " |     |
        " |
    """

    def __init__(self):
        """Set main `class` instance

        Initialize
        ----------
            self.app: "Dictionary containing application informations"
            self.language: "String containing desired language code"
            self.themes: "Dictionary containing application themes"
            self.theme: "Dictionary containing selected theme settings"
            self.options: "Tuple containing cmd line options from sys.argv"
            self.session: "Dictionary to store session parameters"
            self.devices: "Array of dict of availables devices and data"
            self.trad: "Gettext function to translate strings"
        """
        self.app = load_json_file('app.json')
        self.language = self.app['language']
        self.themes = load_json_file('themes.json')
        self.theme = self.themes['default']
        self.options = app_helper(self)
        self.session = load_json_file('settings.json')
        self.devices = {}
        self.trad = ''

    def __str__(self):
        """Add extra method to the class.

        Returns
        -------
            Current class name
        """
        return self.__class__.__name__

    def run(self):
        """Start the `application`

        Actions
        -------
            1) "Set global settings"
            2) "Set user options"
            3) "Prevent bad settings"
            3) "Ask for mode to use"
            4) "Set mode settings"
            5) "Ask required questions"
            6) "Set session settings"
            7) "Check for requirements"
            8) "Run selected action"
        """

        # Options
        global_settings(self)
        options_manager(self)
        self.trad = app_translator(self.language)

        # Prevent wrong settings
        prevent_kernel_folder(self)
        prevent_defconfig_folder(self)
        prevent_out_folder(self)
        prevent_img_folder(self)
        prevent_zip_folder(self)
        prevent_android_folder()

        # Session
        app_banner(self)
        ask_for_mode(self)
        mode_settings(self)
        ask_questions(self)
        session_debug(self)
        session_settings(self)
        session_requirements(self)
        run_session(self)


if __name__ == '__main__':

    try:
        app_logger()
        prevent_wrong_usage()
        ZenMaxBuilder().run()

    except KeyboardInterrupt:
        app_exit()
