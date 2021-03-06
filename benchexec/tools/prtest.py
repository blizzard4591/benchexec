# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import benchexec.util as util
import benchexec.tools.template


class Tool(benchexec.tools.template.BaseTool):
    """
    Tool info for PRTest (https://gitlab.com/sosy-lab/software/prtest).
    """

    REQUIRED_PATHS = ["src", "include", "bin"]

    def program_files(self, executable):
        return self._program_files_from_executable(
            executable, self.REQUIRED_PATHS, parent_dir=True
        )

    def executable(self):
        return util.find_executable("prtest", "bin/prtest")

    def version(self, executable):
        return self._version_from_tool(executable)

    def name(self):
        return "PRTest"
