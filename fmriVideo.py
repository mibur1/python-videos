import sys
import numpy as np
import nibabel as nib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from bids import BIDSLayout

# animation loop  
def animate(frame_number):
    img1.set_array(np.flipud(nii_data[x, :, :, frame_number].T))
    img2.set_array(np.flipud(nii_data[:, y, :, frame_number].T))
    img3.set_array(nii_data[:, :, z, frame_number])
    print(f'\rProgress: {int(frame_number/nii_data.shape[3]*100)}%', end='')
    return 

wd = sys.path[0] # current working directory
layout = BIDSLayout(wd)  # path to BIDS dataset
subject_ids = layout.get_subjects() # get all unique subject IDs in the dataset

# loop over all subjects and create a video for each
for subject in subject_ids:
    print(f"\nCreating video for sub-{subject}")

    # get data
    nii_file = layout.get(subject=subject, suffix='bold', extension='nii.gz', return_type='file')[0]
    nii_img = nib.load(nii_file)
    nii_data = nii_img.get_fdata()

    # figure params
    fig, ax = plt.subplots(1,3, figsize=(20,8))
    fig.suptitle(f'sub-{subject}', fontsize=30)
    plt.tight_layout()

    # create prototype image object and only update data in each frame
    # we are assuming that nii_data is 4D and we are visualizing the first slice at the first time point
    x,y,z = nii_data.shape[0]//2, nii_data.shape[1]//2, nii_data.shape[2]//2
    img1 = ax[0].imshow(np.flipud(nii_data[x, :, :, 0].T), cmap='viridis')
    img2 = ax[1].imshow(np.flipud(nii_data[:, y, :, 0].T), cmap='viridis') 
    img3 = ax[2].imshow(nii_data[:, :, z, 0], cmap='viridis')

    # set equal aspect ratio, remove labels and axis
    for i in range(3):
        ax[i].set_aspect('equal')
        ax[i].axis('off')

    anim = animation.FuncAnimation(fig, animate, frames=nii_data.shape[3]) # create the video
    anim.save(f'{wd}/sub-{subject}.mp4', writer=animation.FFMpegWriter(fps=10)) # save as mp4 using ffmpeg writer
    plt.close()