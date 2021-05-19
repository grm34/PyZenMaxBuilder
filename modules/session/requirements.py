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
from modules.cloner.anykernel import clone_anykernel
from modules.cloner.toolchains import clone_toolchains
from modules.cloner.zipsigner import download_zipsigner


def session_requirements(self):
    """Clone or download `requirements`

    Functions
    ---------
        `clone_anykernel`: "clone AnyKernel repository"
        `clone_toolchains`: "clone selected compiler (toolchain)"
        `download_zipsigner`: "download zipsigner.jar"
    """

    if self.session['mode'] == 'newbuild':
        clone_toolchains(self)
        clone_anykernel(self)
        download_zipsigner(self)

    elif self.session['mode'] == 'makezip':
        clone_anykernel(self)

    elif self.session['mode'] == 'zipsigner':
        download_zipsigner(self)
