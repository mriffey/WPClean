import pyperclip

txttoclean = pyperclip.paste()
txttoclean = txttoclean.replace('<!-- /wp:paragraph -->','')
txttoclean = txttoclean.replace('<!-- wp:paragraph -->','')

txttoclean = txttoclean.replace('<!-- /wp:heading -->','')
txttoclean = txttoclean.replace('<!-- wp:heading -->','')

txttoclean = txttoclean.replace('<!-- wp:list -->','')
txttoclean = txttoclean.replace('<!-- /wp:list -->','')

txttoclean = txttoclean.replace('<!-- wp:quote -->','')
txttoclean = txttoclean.replace('<!-- /wp:quote -->','')

txttoclean = txttoclean + '<i>Mark Riffey is an investor and advisor to small business owners. Want to learn' + \
             ' more about Mark or ask him to write about a strategic, operations or marketing problem? See ' + \
             '<a class="text" href="http://www.markriffey.com/" target="_blank" rel="noopener noreferrer">' + \
             'Mark\'s site</a>, contact him on <a class="text" href="https://linkedin.com/in/markriffey" ' + \
             'target="_blank" rel="noopener noreferrer">LinkedIn</a> or <a class="text" ' + \
             'href="http://www.twitter.com/MarkRiffey" target="_blank" rel="noopener noreferrer">Twitter</a>,' + \
             'or email him at <a class="text" href="mailto:mriffey@flatheadbeacon.com">' + \
             'mriffey@flatheadbeacon.com</a>.</i>'

pyperclip.copy(txttoclean)
print(txttoclean)