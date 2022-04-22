import random

min = "abcdefghijklmnopqrstuvwxyz"
mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nun = "1234567890"
sim = "()/-@&$%#}{][+*%#?!_;:."

todos = min + mai + nun + sim

senha = "".join(random.sample(todos, 10))

print(senha)