import os
import shutil

import pytest
import numpy as np

import species
from species.util import test_util


class TestCalibration:

    def setup_class(self):
        self.limit = 1e-10
        self.test_path = os.path.dirname(__file__) + '/'
        self.model_param = {'scaling': 1.}

    def teardown_class(self):
        os.remove('species_database.hdf5')
        os.remove('species_config.ini')
        shutil.rmtree('data/')

    def test_species_init(self):
        test_util.create_config('./')
        species.SpeciesInit()

    def test_read_calibration(self):
        database = species.Database()
        database.add_spectrum('vega')

        read_calib = species.ReadCalibration('vega', filter_name='Paranal/NACO.H')
        assert read_calib.wavel_range == pytest.approx((1.44, 1.88), rel=self.limit, abs=0.)

    def test_resample_spectrum(self):
        read_calib = species.ReadCalibration('vega')
        spec_box = read_calib.resample_spectrum(np.linspace(1., 2., 10), apply_mask=True)

        assert np.sum(spec_box.wavelength) == 15.
        assert np.sum(spec_box.flux) == pytest.approx(2.288734760321133e-08, rel=self.limit, abs=0.)

    def test_get_spectrum(self):
        read_calib = species.ReadCalibration('vega', filter_name='Paranal/NACO.Lp')
        spec_box = read_calib.get_spectrum(self.model_param, apply_mask=True, spec_res=100.)

        assert np.sum(spec_box.wavelength) == pytest.approx(79.79662545707652, rel=self.limit, abs=0.)
        assert np.sum(spec_box.flux) == pytest.approx(1.094246808910988e-09, rel=self.limit, abs=0.)

        with pytest.warns(UserWarning) as warning:
            spec_box = read_calib.get_spectrum(self.model_param, apply_mask=True, spec_res=1000.,
                                               extrapolate=True, min_wavelength=None)

        assert len(warning) == 2

        assert np.sum(spec_box.wavelength) == pytest.approx(2594.7730845698397, rel=self.limit, abs=0.)
        assert np.sum(spec_box.flux) == pytest.approx(1.5194443166871866e-08, rel=self.limit, abs=0.)

    def test_get_flux(self):
        read_calib = species.ReadCalibration('vega', filter_name='Paranal/NACO.H')
        flux = read_calib.get_flux(model_param=self.model_param)

        assert flux  == pytest.approx(1.1329023591019857e-09, rel=self.limit, abs=0.)

    def test_get_magnitude(self):
        read_calib = species.ReadCalibration('vega', filter_name='Paranal/NACO.H')
        magnitude = read_calib.get_magnitude(model_param=self.model_param)

        assert magnitude[0] == 0.03
        assert magnitude[1] is None
