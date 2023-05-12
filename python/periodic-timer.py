def timer_callback():
    time.sleep(3)
    print('timer - callback')
    timer_thread.run()

timer_thread = threading.Thread(target=timer_callback)
timer_thread.start()

# Quix only
qx.App.run()
