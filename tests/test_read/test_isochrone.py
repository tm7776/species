import os
import shutil
import urllib.request

import pytest
import numpy as np

import species
from species.util import test_util


class TestIsochrone:
    def setup_class(self):
        self.limit = 1e-8
        self.test_path = os.path.dirname(__file__) + "/"

    def teardown_class(self):
        os.remove("species_database.hdf5")
        os.remove("species_config.ini")
        shutil.rmtree("data/")

    def test_species_init(self):
        test_util.create_config("./")
        species.SpeciesInit()

    def test_read_isochrone(self):
        database = species.Database()
        database.add_isochrones("ames")

        database.add_model("ames-cond", teff_range=(2000.0, 2500.0))

        read_isochrone = species.ReadIsochrone("ames-cond")
        assert read_isochrone.tag == "ames-cond"

    def test_get_isochrone(self):
        read_isochrone = species.ReadIsochrone("ames-cond")

        isochrone_box = read_isochrone.get_isochrone(
            100.0, np.linspace(10.0, 100.0, 10), ("J", "H"), "J"
        )

        assert np.sum(isochrone_box.mass) == pytest.approx(
            550.0, rel=self.limit, abs=0.0
        )

        assert np.sum(isochrone_box.teff) == pytest.approx(
            23007.53864754502, rel=self.limit, abs=0.0
        )

        assert np.sum(isochrone_box.logg) == pytest.approx(
            47.475577469602705, rel=self.limit, abs=0.0
        )

        assert np.sum(isochrone_box.radius) == pytest.approx(
            14.29977420304961, rel=self.limit, abs=0.0
        )

        assert isochrone_box.color.shape == (10,)
        assert isochrone_box.magnitude.shape == (10,)

        assert np.sum(isochrone_box.color) == pytest.approx(
            2.625186321644007, rel=self.limit, abs=0.0
        )

        assert np.sum(isochrone_box.magnitude) == pytest.approx(
            108.78841310475491, rel=self.limit, abs=0.0
        )

    def test_get_color_magnitude(self):
        read_isochrone = species.ReadIsochrone("ames-cond")

        colormag_box = read_isochrone.get_color_magnitude(
            100.0,
            np.linspace(35.0, 45.0, 10),
            "ames-cond",
            ("MKO/NSFCam.J", "MKO/NSFCam.H"),
            "MKO/NSFCam.J",
        )

        assert colormag_box.object_type == "model"
        assert colormag_box.color.shape == (10,)
        assert colormag_box.magnitude.shape == (10,)

        assert np.sum(colormag_box.color) == pytest.approx(
            2.489776760959666, rel=self.limit, abs=0.0
        )

        assert np.sum(colormag_box.magnitude) == pytest.approx(
            109.56539426050192, rel=self.limit, abs=0.0
        )

        assert np.sum(colormag_box.mass) == pytest.approx(
            400.0, rel=self.limit, abs=0.0
        )

    def test_get_color_color(self):
        read_isochrone = species.ReadIsochrone("ames-cond")

        colorcolor_box = read_isochrone.get_color_color(
            100.0,
            np.linspace(35.0, 45.0, 10),
            "ames-cond",
            (("MKO/NSFCam.J", "MKO/NSFCam.H"), ("MKO/NSFCam.H", "MKO/NSFCam.Ks")),
        )

        assert colorcolor_box.object_type == "model"
        assert colorcolor_box.color1.shape == (10,)
        assert colorcolor_box.color2.shape == (10,)

        assert np.sum(colorcolor_box.color1) == pytest.approx(
            2.489776760959666, rel=self.limit, abs=0.0
        )

        assert np.sum(colorcolor_box.color2) == pytest.approx(
            3.3482651523940685, rel=self.limit, abs=0.0
        )

        assert np.sum(colorcolor_box.mass) == pytest.approx(
            400.0, rel=self.limit, abs=0.0
        )
