import pickle
game_data = {
    'play-position':"N23 E45",
    'pockets':['keys', 'pocket knife', 'polished stone'],
    'backpack':['rope', 'hammer', 'apple'],
    'money':158.02
    }
save_file = open('save.dat','wb')
pickle.dump(game_data,save_file)

save_file.close()
