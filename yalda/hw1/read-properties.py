import configparser
config = configparser.ConfigParser()

config.read('assignment2.data')

print( config.get('default','L') )
print( config.get('default','rho') )
