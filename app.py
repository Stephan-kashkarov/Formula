import formula

# Network
def do_connect(essid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

app = formula.App()

while True:
    if app.active:
        app.update()
    else:
        app.active = app.sleep()