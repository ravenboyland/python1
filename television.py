class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television object."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Turn the TV on and off by changing the value of the status variable."""
        self._status = not self._status

    def mute(self):
        """Mute and unmute the TV when it's on by changing the value of the muted variable."""
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume = self.MIN_VOLUME

    def channel_up(self):
        """Increase the TV channel value when the TV is on."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the TV channel value when the TV is on."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        """Increase the TV volume when the TV is on."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the TV volume when the TV is on."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """Send the values of the TV object in the specified format."""
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
