class UrlMapClass:
    
    urlmap = {'google':'https://www.google.com',
              'open_ai':"https://chat.openai.com/auth/login",
              'google_bard':"https://bard.google.com/?utm_source=sem&utm_medium=paid-media&utm_campaign=q4enIN_sem7&hl=en",
              'bing':'https://www.bing.com',
              'bing_ai':'https://www.bing.com/search?q=bing&cvid=9a7dc9d1b7174746b7918744bb3a81a4&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIECAEQADIECAIQADIECAMQADIGCAQQRRg8MgYIBRBFGDwyBggGEEUYPDIGCAcQRRg8MgYICBBFGDzSAQgyOTU1ajBqOagCALACAA&FORM=ANAB01&PC=U531&showconv=1&wlsso=0'
              }

class XPaths:
    xpaths = {'search':'//*[@id="input"]',
              'email':'',
              'password':'',
              'login':'',
              'bard_submit':'/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/chat-window/div[1]/div[2]/div[1]/input-area/div/div[2]/button/span[3]',
              'verify':'//*[@id="challenge-stage"]/div/label/input',
              'bard_input':'/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/chat-window/div[1]/div[2]/div[1]/input-area/div/div[1]/div/div/div/rich-textarea/div[1]/p',
              'bard_answers':'//*[contains(@id, "message-content-idr_")]/div/p',
              }