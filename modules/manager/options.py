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


def options_manager(self):
    """Command line `options` manager

    Actions
    -------
        1) "Define command line arguments"
    """

    # Language
    if self.options.lang:
        self.language = self.options.lang[0].strip()

    # Theme
    if self.options.theme:
        self.theme = self.themes[self.options.theme[0].strip()]

    # DEBUG
    if self.options.debug:
        self.session['debug'] = self.options.debug[0].strip()

    # Device name
    if self.options.name:
        self.session['device_name'] = self.options.name[0].strip()

    # Device codename
    if self.options.codename:
        self.session['device_codename'] = self.options.codename[0].strip()

    # Kernel name
    if self.options.kernel:
        self.session['kernel_name'] = self.options.kernel[0].strip()

    # Kernel folder
    if self.options.k_folder:
        self.session['kernel_folder'] = self.options.k_folder[0].strip()

    # Defconfig folder
    if self.options.d_folder:
        self.session['defconfig_folder'] = self.options.d_folder[0].strip()

    # OUT folder
    if self.options.out_folder:
        self.session['out_folder'] = self.options.out_folder[0].strip()

    # Kernel images folder
    if self.options.kb_folder:
        self.session['kernel_img_folder'] = self.options.kb_folder[0].strip()

    # Zip folder
    if self.options.zip_folder:
        self.session['zip_folder'] = self.options.zip_folder[0].strip()
