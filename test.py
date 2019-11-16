from OptimusTime import OptimusTime

# Descripti
# self.on: These tests require the user to type, click, and scroll to get the tests to pass

# This is the entry-point for the application.
if __name__ == '__main__':
    # Instantiate the time optimizer
    optimusTime = OptimusTime()

    keyboardPrompt = input("Type some keys, scroll your mouse, and click a few times: ")
    
    if optimusTime.keyCount > 0:
        print('Passed Keyboard Test')
    else:
        print('Failed Keyboard Test')

    if optimusTime.mouseClickCount > 0:
        print('Passed Mouse Test')
    else:
        print('Failed Mouse Test')

    if optimusTime.scrollCount > 0:
        print('Passed Scroll Test')
    else:
        print('Failed Scroll Test')

    exit()
    
