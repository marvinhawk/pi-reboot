from gpiozero import Button
import subprocess

# GPIO pin number
PIN = 3
# Time threshold for shutdown in seconds
THRES = 3

button = Button(PIN)

def button_listener(button):
	button.wait_for_press()
	
	while button.is_pressed:
		if button.active_time > THRES:
			print('SHUTDOWN')
			subprocess.call(['sudo', 'shutdown', '-h', 'now'], shell=False)
			return 0
	print('REBOOT')
	subprocess.call(['sudo', 'shutdown', '-r', 'now'], shell=False)
	return 0

if __name__ == '__main__':
	button_listener(button)
