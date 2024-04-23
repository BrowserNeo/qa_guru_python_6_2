from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
# browser.element('#L2AGLb').click() #принять куки
browser.element('[name="nq"]').should(be.blank).press_enter()
browser.element('[name="q"]').should(be.blank).type('yashake/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
