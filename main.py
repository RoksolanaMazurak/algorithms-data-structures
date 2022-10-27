from gamesrv import GameSrv

gamesrv = GameSrv("sources/input1.txt", "sources/output1.txt")
gamesrv.get_min_max_latency()

gamesrv = GameSrv("sources/input2.txt", "sources/output2.txt")
gamesrv.get_min_max_latency()

gamesrv = GameSrv("sources/input3.txt", "sources/output3.txt")
gamesrv.get_min_max_latency()