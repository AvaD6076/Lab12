class Television:
    # Class Variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance Variables (Private)
        self.__status = False      # TV is initially off
        self.__muted = False       # TV is initially not muted
        self.__volume = Television.MIN_VOLUME  # Start at minimum volume
        self.__channel = Television.MIN_CHANNEL  # Start at minimum channel

    # Methods
    def power(self):
        """Turn the TV on or off."""
        self.__status = not self.__status

    def mute(self):
        """Mute or unmute the TV."""
        if self.__status:  # Only if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the TV channel."""
        if self.__status:  # Only if the TV is on
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease the TV channel."""
        if self.__status:  # Only if the TV is on
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase the TV volume."""
        if self.__status and not self.__muted:  # Only if the TV is on and not muted
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the TV volume."""
        if self.__status and not self.__muted:  # Only if the TV is on and not muted
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return the TV status."""
        status = "On" if self.__status else "Off"
        mute_status = "Muted" if self.__muted else "Not Muted"
        return f"Power: {status}, Channel: {self.__channel}, Volume: {self.__volume}, Mute Status: {mute_status}"


# Example usage (This would be in a different file, or in a test function)
if __name__ == "__main__":
    tv = Television()

    # Simulating TV usage
    print(tv)  # Initial State
    tv.power()  # Turn the TV on
    tv.channel_up()  # Increase the channel
    tv.volume_up()  # Increase the volume
    tv.mute()  # Mute the TV
    tv.channel_down()  # Decrease the channel
    tv.volume_down()  # Decrease the volume
    print(tv)  # Final State
