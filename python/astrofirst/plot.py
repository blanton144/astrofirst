import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = [7., 5.]
matplotlib.rcParams['font.size'] = 20.
matplotlib.rcParams['text.usetex'] = True


def absmag_colors(sps=None, filename=None):
    """Plot colors and absolute magnitudes

    Parameters
    ----------

    filename : str
        file to write to (or None)

    sps : ndarray
        SPS results from MNSA kcorrect analysis

    Notes
    -----

    If filename is specified, writes to that file. Otherwise displays 
    plot to user.
"""
    absmag_r = sps['absmag'][:, 3]
    absmag_FmW1 = sps['absmag'][:, 0] - sps['absmag'][:, 5]

    fig, ax = plt.subplots()
    ax.scatter(absmag_r, absmag_FmW1, s=2)
    ax.set_xlim([-16., -24.5])
    ax.set_ylim([-1.5, 11.5])
    ax.set_xlabel('$M_r$')
    ax.set_ylabel('FUV $-$ W1')
    fig.tight_layout()
    if(filename is None):
        plt.show()
    else:
        plt.savefig(filename)
    fig.clf()
