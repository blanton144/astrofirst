import os
import fitsio


def read_mnsa_catalog(version='0.3.1', ext='SUMMARY'):
    """Read the MNSA catalog from standard location

    Parameters
    ----------

    version : str
        version number of catalog

    ext : str
        FITS HDU to read

    Returns
    -------

    data : ndarray
        data in HDU desired

    Notes
    -----

    Available HDUs are: SUMMARY, ELLIPSE, SPS_AP04, SPS_AP05, SPS_AP06,
    SPS_AP07, SPS_AP08, and CENTRAL_FLUX.
"""
    mnsa_file = os.path.join(os.getenv('MNSA_DATA'),
                             version, 'mnsa-{v}.fits'.format(v=version))
    data = fitsio.read(mnsa_file, ext=ext)
    return(data)
