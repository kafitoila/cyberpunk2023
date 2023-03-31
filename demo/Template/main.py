from environs import Env

env = Env()
env.read_env()
token = env('token')

print(token)