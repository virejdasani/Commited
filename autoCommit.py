import os

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	os.system('git commit --allow-empty -m "New Commit at: $(date)"')

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
	
# git commit --allow-empty -m "New Commit at: $(date)"

#  MADE BY:_            _   _____                        _ 
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |                                 
#                    |__/                                  