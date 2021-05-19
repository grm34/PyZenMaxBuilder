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
import os


def get_compiler_path(self):
    """Get compiler `path` (toolchain)

    Returns
    -------
        output: "String containing the compiler PATH to use"
    """

    # Proton Clang
    if self.session['answers']['compiler'] == 'proton':

        output = '{dir}/proton/bin:/usr/bin:$PATH'.format(
            dir='{out}/android/toolchains'.format(out=os.getcwd())
        )

    # Clang Stable
    elif self.session['answers']['compiler'] == 'clang':

        output = (
            '{dir}/clang/bin:{dir}/gcc64/bin:{dir}/gcc32/bin:/usr/bin:$PATH'
            .format(dir='{out}/android/toolchains'.format(out=os.getcwd()))
        )

    # GNU Compiler Collection
    elif self.session['answers']['compiler'] == 'gcc':

        output = '{dir}/gcc32/bin:{dir}/gcc64/bin:/usr/bin/:$PATH'.format(
            dir='{out}/android/toolchains'.format(out=os.getcwd())
        )

    return output
