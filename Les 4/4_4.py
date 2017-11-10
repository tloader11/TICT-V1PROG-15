def new_password(oldpassword, newpassword):
    if (oldpassword != newpassword) and (len(newpassword) > 5):
        return True
    else:
        return False


print ( new_password("testpass", input("Voer het nieuwe wachtwoord in: ") ) )
