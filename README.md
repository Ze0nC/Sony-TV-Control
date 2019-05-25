# Sony-TV-Control
## This is basically working. 

## Modules required
requests, wakeonlan
## Usage
Edit `tv_config.py` to update match your TV's ip address and MAC address.

Use anything for nickname and id.

###### Wake up:
Waking up uses wakeonlan. Pairing is not necessary, but it is necessary to use correct MAC address.

`python sony_tv_control.py --wake`

###### Pairing: 
`python sony_tv_control.py --init`

Then enter the 4-digit code on tv screen.

###### Button press:
`python sony_tv_control.py --button <button_name>`

A list of button names is displayed by `python sony_tv_control.py -h`

###### Switch input source:
`python sony_tv_control.py --source <source_name>`

A list of source names is displayed by `python sony_tv_control.py -h`

## References
[http://shimobepapa.hatenadiary.jp/entry/2016/12/18/002916](http://shimobepapa.hatenadiary.jp/entry/2016/12/18/002916)

## Button List

```
power_off
volume_down
volume_up
mute_toggle
channel_down
channel_up
cursor_down
cursor_up
cursor_right
cursor_left
cursor_enter
menu_home
exit
return
display
guide
0
1
2
3
4
5
6
7
8
9
10
digit_separator
enter
menu_popup
function_red
function_yellow
function_green
function_blue
3d
subtitle
previous_channel
help
sync_menu
options
input_toggle
wide
sony_entertainment_network
pause
play
stop
forward
reverse
previous
next
```

## Source List
```
hdmi1
hdmi2
hdmi3
hdmi4
tv
mirroring
```

## License
WTFPL

Do what ever you want.

