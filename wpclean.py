import pyperclip

txttoclean = pyperclip.paste()
txttoclean = txttoclean.replace('<!-- /wp:paragraph -->','')
txttoclean = txttoclean.replace('<!-- wp:paragraph -->','')

txttoclean = txttoclean.replace('<!-- /wp:heading -->','')
txttoclean = txttoclean.replace('<!-- wp:heading -->','')

pyperclip.copy(txttoclean)
print(txttoclean)