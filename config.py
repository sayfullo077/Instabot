from environs import Env

env = Env()
env.read_env()
username = env.str('USERNAME')
password = env.str('PASSWORD')
