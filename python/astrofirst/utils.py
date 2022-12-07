import numpy as np


def match_plateifus(plateifu1=None, plateifu2=None):
    """Return matched indices in plate-IFU lists

    Parameters
    ----------

    plateifu1 : str
        Plate-IFU list #1

    plateifu2 : str
        Plate-IFU list #2

    Returns
    -------

    indx1 : ndarray of np.int32
       [nmatch] index into first list

    indx2 : ndarray of np.int32
       [nmatch] index into second list


    Notes
    -----

    indx1 and indx2 only return indices of matched values
"""

    ## Need to add code here to perform calculation!
    indx1 = np.zeros(0, dtype=np.int32)
    indx2 = np.zeros(0, dtype=np.int32)

    return(indx1, indx2)
