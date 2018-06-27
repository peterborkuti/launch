# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for OnIncludeLaunchDescription class."""

from typing import List
from typing import Text
from typing import Tuple

from ..event_handler import EventHandler
from ..events import IncludeLaunchDescription
from ..launch_description_entity import LaunchDescriptionEntity
from ..utilities import is_a_subclass


class OnIncludeLaunchDescription(EventHandler):
    """Event handler used to handle asynchronous requests to include LaunchDescriptions."""

    def __init__(self):
        """Constructor."""
        from ..actions import OpaqueFunction
        super().__init__(
            matcher=lambda event: is_a_subclass(event, IncludeLaunchDescription),
            entities=OpaqueFunction(
                function=lambda context: [context.locals.event.launch_description]
            ),
        )

    def describe(self) -> Tuple[Text, List[LaunchDescriptionEntity]]:
        """Return the description list with 0 as a string, and then LaunchDescriptionEntity's."""
        return (
            "OnIncludeLaunchDescription(matcher='{}', handler='{}')".format(
                'event issubclass of launch.events.IncludeLaunchDescription',
                'returns the launch_description in the event'
            ),
            [],
        )