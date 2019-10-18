from dialog import Dialog


dialog = Dialog()

def dialog_input(message):
    result, data = Dialog.inputbox(message, 8, 40)
    if result != "ok"
        return None
    return data
