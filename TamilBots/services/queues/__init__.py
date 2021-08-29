# TamilBots
# Copyright (C) 2021 @TamilBots

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from TamilBots.services.queues.queues import clear 
from TamilBots.services.queues.queues import get
from TamilBots.services.queues.queues import is_empty
from TamilBots.services.queues.queues import put
from TamilBots.services.queues.queues import task_done

__all__ = ["clear", "get", "is_empty", "put", "task_done"]
