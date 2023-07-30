
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
bottom = np.zeros(3)



people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=['±%.2f' % e for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
