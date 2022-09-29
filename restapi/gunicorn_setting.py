import os

#bind = '127.0.0.1:' + str(os.getenv('PORT', 8080))
bind = '0.0.0.0:' + str(os.getenv('PORT', 8080))
proc_name = 'Infrastructure-Practice-Flask'
workers = 1
