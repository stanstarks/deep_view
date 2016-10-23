import numpy as np

# create test.txt
with open('test.txt', 'w') as outfile:
    for i in range(1, 7):
        outfile.write('%d.png 0\n' % i)

# create inds.py
inds = (np.arange(60).reshape((6, 10))) % 6
np.save('inds.npy', inds)

# create predicts.py
predicts = np.vstack((np.zeros(6), np.ones(6)))
np.save('predicts.npy', predicts)
