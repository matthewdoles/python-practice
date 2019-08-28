import racquetball
print(racquetball.game_over(0, 0))
# false
print(racquetball.game_over(5, 10))
# false
print(racquetball.game_over(15, 3))
# true
print(racquetball.game_over(3, 15))
# true

# run multiple times, ensure games were prob. are close that scores are close
# and when prob. are spread, the game should usually be a rout
print(racquetball.sim_one_game(.5, .5))
print(racquetball.sim_one_game(.5, .5))
print(racquetball.sim_one_game(.3, .3))
print(racquetball.sim_one_game(.3, .3))
print(racquetball.sim_one_game(.4, .9))
print(racquetball.sim_one_game(.4, .9))
print(racquetball.sim_one_game(.9, .4))
print(racquetball.sim_one_game(.9, .4))