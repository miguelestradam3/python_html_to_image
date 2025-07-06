from html2image import Html2Image

hti = Html2Image()
# Assuming 'design.html' exists
# More information at: https://pypi.org/project/html2image/
hti.screenshot(
    html_file='design.html', save_as='other.png', size=(3000, 7600)
)