import numpy as np
import matplotlib.pyplot as plt

def plots(ims, figsize=(18,12), rows=2, interp=False, titles=None):

    if type(ims[0]) is np.ndarray:
        ims = np.array(ims).astype(np.uint8)
        if (ims.shape[-1] != 3):
            ims = ims.transpose((0,2,3,1))

    f = plt.figure(figsize=figsize)
    cols = len(ims) // rows if len(ims) % 2 == 0 else len(ims) // rows + 1

    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None:
            sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i], interpolation = None if interp else 'none')
        plt.tight_layout()

        
words_dict = {"1": " abies concolor", 
              "2": " acer campestre", 
              "3": " carpinus betulus", 
              "4": " catalpa bignonioides", 
              "5": " cedrus deodara", 
              "6": " ginkgo biloba", 
              "7": " magnolia grandiflora", 
              "8": " morus alba", 
              "9": " quercus nigra", 
              "10": " robinia pseudo acacia"}