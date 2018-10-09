if 'urxvt' in window.get_active_class().lower():
    keyboard.send_keys("<ctrl>+<alt>+c")
else:
    keyboard.send_keys("<ctrl>+c")