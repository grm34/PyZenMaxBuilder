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
import shlex
from subprocess import (PIPE, CalledProcessError, Popen, SubprocessError,
                        TimeoutExpired, check_output)

from .exit import app_exit


def run_command(
    cmd, path=None, args=None, error=None, warning=None, exit_on_error=False):
    """Subprocess Popen with `console output`

    Arguments
    ---------
        cmd: "String containing the shell command to run"

    Keyword Arguments
    -----------------
        path: "String of the folder from where to run the command"
        args: "String of the arguments to pipe" (default: None)
        error: "String to set custom error message" (default: None)
        warning: "String to set custom warning message" (default: None)
        `exit_on_error`: "Boolean to exit on exception" (default: False)

    Returns
    -------
        "String containing the ouptut of the shell command"
    """
    try:
        if args is not None:
            pipe = Popen(args, stdout=PIPE)
            command = Popen(
                shlex.split(cmd),
                stdin=pipe.stdout,
                stdout=PIPE,
                encoding='utf-8',
                shell=False,
                cwd=path
            )
            command = command.communicate()[0]
            output = None

        else:
            command = Popen(
                shlex.split(cmd),
                stdin=PIPE,
                stdout=PIPE,
                encoding='utf-8',
                shell=False,
                cwd=path
            )
            while True:
                output = command.stdout.readline()
                if not output:
                    break

                logging.debug(output.strip())
                print(output.strip())
            output = command.poll()

    except (SubprocessError, OSError, ValueError) as cmd_error:

        if error is not None:
            cmd_error = error

        if exit_on_error is True:
            logging.error(cmd_error)

            if warning is not None:
                logging.warning(warning)

            app_exit()

        else:
            logging.debug(cmd_error)

    return output


def command_output(cmd, path=None, exit_on_error=False, error=None,
    warning=None, timeout=None):
    """Subprocess `check_output` with return codes

    Arguments
    ---------
        cmd: "String containing the shell command to run"

    Keyword Arguments
    -----------------
        path: "String of the folder from where to run the command"
        error: "String to set custom error message" (default: None)
        warning: "String to set custom warning message" (default: None)
        `exit_on_error`: "Boolean to exit on exception" (default: False)

    Returns
    -------
        "String containing the ouptut of the shell command"
    """
    try:
        output = check_output(
            cmd,
            shell=True,
            encoding='utf-8',
            timeout=timeout,
            cwd=path
        )

    except (TimeoutExpired, CalledProcessError) as cmd_error:
        output = False

        if error is not None:
            cmd_error = error

        if exit_on_error is True:
            logging.error(cmd_error)

            if warning is not None:
                logging.warning(warning)

            app_exit()

        else:
            logging.debug(cmd_error)

    return output
