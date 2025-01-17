# coding: utf-8
# OceanBase Deploy.
# Copyright (C) 2021 OceanBase
#
# This file is part of OceanBase Deploy.
#
# OceanBase Deploy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OceanBase Deploy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OceanBase Deploy.  If not, see <https://www.gnu.org/licenses/>.


from __future__ import absolute_import, division, print_function

# obd dev mode. {0/1}
ENV_DEV_MODE = "OBD_DEV_MODE"

# base path which will be used by runtime dependencies sync and include config. {absolute path style}
ENV_BASE_DIR = "OBD_DEPLOY_BASE_DIR"

# the installation mode of remote repository. {cp/ln}
ENV_REPO_INSTALL_MODE = "OBD_REPO_INSTALL_MODE"

# disable rsync mode even if the rsync exists. {0/1}
ENV_DISABLE_RSYNC = "OBD_DISABLE_RSYNC"
