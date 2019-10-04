"""
Unit and regression test for the ballistico package.
"""

# Import package, test suite, and other packages as needed
from finitedifference.finitedifference import FiniteDifference
import numpy as np
from ballistico.phonons import Phonons
import ballistico.conductivity as bac
import os

TMP_FOLDER = 'tmp-folder'

def create_phonons():
    # Create a finite difference object
    finite_difference = FiniteDifference.import_from_dlpoly_folder(folder='si-dlpoly',
                                                                   supercell=[3, 3, 3])

    # Create a phonon object
    phonons = Phonons(finite_difference=finite_difference,
                      kpts=[5, 5, 5],
                      is_classic=False,
                      temperature=300,
                      folder=TMP_FOLDER)
    return phonons


def test_qhgk_conductivity():
    try:
        os.rmdir(TMP_FOLDER)
    except FileNotFoundError:
        pass
    phonons = create_phonons()
    cond = bac.conductivity(phonons, method='qhgk').sum(axis=0)
    cond = np.abs(np.mean(cond.diagonal()))
    np.testing.assert_approx_equal(cond, 230, significant=3)
