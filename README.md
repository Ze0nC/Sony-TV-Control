# Sony-TV-Control
## This is basically working. 

## Dependent
requests, wakeonlan
## Usage
Edit `tv_config.py` to update match your TV's ip address and MAC address.
Use anything for nickname and id.

Wake up:
Waking up uses wakeonlan. Pairing is not necessary, but it is necessary to use correct MAC address.
`python sony_tv_control.py --wake`

Pairing: 
`python sony_tv_control.py --init`
Then enter the 4-digit code on tv screen.

Button press:
`python sony_tv_control.py --button <button_name>`
A list of button names is displayed by `python sony_tv_control.py -h`

Switch input source:
`python sony_tv_control.py --source <source_name>`
A list of source names is displayed by `python sony_tv_control.py -h`

## References
[http://shimobepapa.hatenadiary.jp/entry/2016/12/18/002916](http://shimobepapa.hatenadiary.jp/entry/2016/12/18/002916)

## Licence
WTFPL
Do what ever you want.

