# Ayiin - Ubot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/AyiinUbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/AyiinUbot/blob/main/LICENSE/>.
#
# FROM AyiinUbot <https://github.com/AyiinXd/AyiinUbot>
# t.me/AyiinChat & t.me/AyiinSupport & t.me/HyperSupportQ 


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging

from config import *
from git import Repo
from pyHyper import PyrogramEx
from pyHyper.Clients import *
from pyHyper.config import Var


repo = Repo()
branch = repo.active_branch
ling = PyrogramEx()
var = Var()
hndlr = [
    f"{var.HNDLR[0]}",
    f"{var.HNDLR[1]}",
    f"{var.HNDLR[2]}",
    f"{var.HNDLR[3]}",
    f"{var.HNDLR[4]}",
    f"{var.HNDLR[5]}",
]
logs = logging.getLogger(__name__)
