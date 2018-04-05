def isMAC48Address(inputString):
    try:
        for part in inputString.split('-'):
            if len(part) != 2:
                raise Exception
            int(part, 16)  # This will error if not in hex
        return True
    except:
        return False


""" TESTS """
res = isMAC48Address("00-1B-63-84-45-E6")
print(res)
