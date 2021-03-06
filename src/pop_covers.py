# Copyright (c) 2014-2016 Cedric Bellegarde <cedric.bellegarde@adishatz.org>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

from lollypop.art_widgets import ArtworkSearch


class CoversPopover(Gtk.Popover):
    """
        Popover with album covers from the web
        @Warning: Destroy it self on close
    """

    def __init__(self, album):
        """
            Init Popover
            @param album as album
        """
        Gtk.Popover.__init__(self)
        self._album = album
        self._monster_pixbufs = {}
        # We only search with first artist, should be ok
        widget = ArtworkSearch(self._album.artist_ids[0],
                               self._album)
        widget.show()
        self.add(widget)
        self.set_size_request(700, 400)
        widget.populate()
