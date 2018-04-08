def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    print({yourLeft, yourRight}, {friendsLeft, friendsRight})
    if yourLeft >= yourRight and friendsLeft >= friendsRight:
        return yourLeft == friendsLeft and yourRight == friendsRight
    elif yourRight >= yourLeft and friendsRight >= friendsLeft:
        return yourLeft == friendsLeft and yourRight == friendsRight
    elif yourLeft >= yourRight and friendsRight >= friendsLeft:
        return yourLeft == friendsRight and yourRight == friendsLeft
    elif yourRight >= yourLeft and friendsLeft >= friendsRight:
        return yourRight == friendsLeft and yourLeft == friendsRight

    return False


res = areEquallyStrong(5, 6, 6, 5)
print(res)
