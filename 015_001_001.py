from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

config.add_section('NEWLOGIN')
config.set('NEWLOGIN','login', 'my_new_login')
config.set('NEWLOGIN', 'pass', 'my_new_pass')

print(config['NEWLOGIN']['login'])


with open('new_config.ini', 'w', encoding='utf8') as new_config_file:
    config.write(new_config_file)


print(int(config['PROGRAM']['setting']))
print(type(int(config['PROGRAM']['setting'])))








'''config['DATABASE'] = {
    'login': 'root',
    'pass':'12345678',
    'host': 'localhost',
    'database' : 'test_db'
}

config['DEAFULT'] = {
    'login': 'mylogin',
    'pass': 'mypass'

}
config['EMAIL'] = {
    'login': 'email_login',
    'pass': 'email_pass'
}

config['PROGRAM'] = {
    'setting': True
}
with open('config.ini', 'w', encoding='utf8') as config_file:
    config.write(config_file)'''




