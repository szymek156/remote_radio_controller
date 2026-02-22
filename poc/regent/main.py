from fsapi2 import FSAPI

URL = 'http://192.168.68.53:80/device'
PIN = 1234
TIMEOUT = 1 # in seconds

print("connect ")
fs = FSAPI(URL, PIN)

print('Name: %s' % fs.friendly_name)
print('Mute: %s' % fs.mute)
print('Mode: %s' % fs.mode)

# fs.mute = False

print('Modes: %s' % fs.modes)
print('Power: %s' % fs.power)
print('Volume steps: %s' % fs.volume_steps)
print('Volume: %s' % fs.volume)

fs.volume = 4
print('Play status: %s' % fs.play_status)
print('Track name: %s' % fs.play_info_name)
print('Track text: %s' % fs.play_info_text)
print('Artist: %s' % fs.play_info_artist)
print('Album: %s' % fs.play_info_album)
print('Graphics: %s' % fs.play_info_graphics)