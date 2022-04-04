from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

# figure params
fig, ax = plt.subplots(figsize=(10,10))
fig.suptitle('Matrix plot', fontsize=14)

# create prototype image object and only update data in each frame
matrix = ax.imshow(np.random.randn(10,10)) 

# animation loop  
def animate_matrix(frame_number):
    rand = np.random.randn(10, 10)
    matrix.set_array(rand)
    print("aninmating frame", frame_number)
    return 

# create animation  
anim = animation.FuncAnimation(fig, animate_matrix, frames=60)

# save as mp4 using ffmpeg writer
anim.save('matrix.mp4', writer=animation.FFMpegWriter(fps=30))
plt.close()