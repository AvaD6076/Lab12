import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv.power)
        self.assertFalse(self.tv.muted)
        self.assertEqual(self.tv.channel, 1)
        self.assertEqual(self.tv.volume, 10)

    def test_power_on(self):
        self.tv.power_on()
        self.assertTrue(self.tv.power)

    def test_power_off(self):
        self.tv.power_on()
        self.tv.power_off()
        self.assertFalse(self.tv.power)

    def test_mute(self):
        self.tv.power_on()
        self.tv.mute()
        self.assertTrue(self.tv.muted)

    def test_unmute(self):
        self.tv.power_on()
        self.tv.mute()
        self.tv.unmute()
        self.assertFalse(self.tv.muted)

    def test_channel_up(self):
        self.tv.power_on()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, 2)

    def test_channel_down(self):
        self.tv.power_on()
        self.tv.channel_up()
        self.tv.channel_down()
        self.assertEqual(self.tv.channel, 1)

    def test_channel_down_not_powered(self):
        self.tv.channel_down()
        self.assertEqual(self.tv.channel, 1)

    def test_volume_up(self):
        self.tv.power_on()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, 11)

    def test_volume_down(self):
        self.tv.power_on()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, 10)

    def test_volume_down_not_muted(self):
        self.tv.power_on()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume, 10)

    def test_volume_not_muted(self):
        self.tv.power_on()
        self.tv.mute()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume, 10)  # Volume shouldn't change when muted

if __name__ == '__main__':
    unittest.main()
