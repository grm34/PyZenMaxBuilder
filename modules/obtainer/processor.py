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

from ..manager.cmd import command_output


def get_processor(self):
    """Get host `processor` (CPU)

    Functions
    ---------
        `command_output`: "Subprocess `check_output` with return codes"

    Actions
    -------
        1) "cat /proc/cpuinfo | grep 'model name' | uniq"
        2) "cat /proc/cpuinfo | awk '/^cpu cores/{print $4}'"

    Returns
    -------
        "Dictionary containing CPU model with nb of cores or Boolean"
    """
    cmd1 = 'cat /proc/cpuinfo | grep "model name" | uniq'
    cmd2 = "cat /proc/cpuinfo | awk '/^cpu cores/{print $4}'"

    cpu_name = command_output(
        cmd1,
        exit_on_error=True,
        error=self.trad('failed to get processor')
    )

    cpu_cores = command_output(
        cmd2,
        exit_on_error=True,
        error=self.trad('failed to get CPU cores')
    )

    if cpu_name is not False:
        cpu_name = cpu_name.split('\n')[0].split(': ')[-1]
        cpu_name = re.sub(' +', ' ', cpu_name)

    if cpu_cores is not False:
        cpu_cores = cpu_cores.split('\n')[0].split(': ')[-1]
        cpu_cores = re.sub(' +', ' ', cpu_cores)

    return {
        'name': '{name}'.format(name=cpu_name),
        'cores': '{cores}'.format(cores=cpu_cores)
    }
