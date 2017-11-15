import threading, time

def threadExample():
    print("Starting program")

    def takeANap():
        time.sleep(5)
        print("Waking up after nap")

    threadObj = threading.Thread(target=takeANap)
    threadObj.start()

    print("End of the program code")

def threadingWithArgsExample():
    print('Cats', 'Dogs', 'Frogs', sep=' & ')
    threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '}) # kwargs = keyword arguments
    threadObj.start()

# threadExample()
threadingWithArgsExample()
