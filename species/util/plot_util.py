"""
Utility functions for plotting data.
"""

import warnings

from string import ascii_lowercase
from typing import Optional, Tuple, List

import numpy as np

from typeguard import typechecked


@typechecked
def sptype_substellar(sptype: np.ndarray, shape: Tuple[int]) -> np.ndarray:
    """
    Function for mapping the spectral types of substellar objects
    (M, L, T, and Y) to numbers.

    Parameters
    ----------
    sptype : np.ndarray
        Array with spectral types.
    shape : tuple(int)
        Shape (1D) of the output array

    Returns
    -------
    np.ndarray
        Array with spectral types mapped to numbers.
    """

    spt_disc = np.zeros(shape)

    for i, item in enumerate(sptype):
        if item[0:2] in ["M0", "M1", "M2", "M3", "M4"]:
            spt_disc[i] = 0.5

        elif item[0:2] in ["M5", "M6", "M7", "M8", "M9"]:
            spt_disc[i] = 1.5

        elif item[0:2] in ["L0", "L1", "L2", "L3", "L4"]:
            spt_disc[i] = 2.5

        elif item[0:2] in ["L5", "L6", "L7", "L8", "L9"]:
            spt_disc[i] = 3.5

        elif item[0:2] in ["T0", "T1", "T2", "T3", "T4"]:
            spt_disc[i] = 4.5

        elif item[0:2] in ["T5", "T6", "T7", "T8", "T9"]:
            spt_disc[i] = 5.5

        elif "Y" in item:
            spt_disc[i] = 6.5

        else:
            spt_disc[i] = np.nan
            continue

    return spt_disc


@typechecked
def sptype_stellar(sptype: np.ndarray, shape: Tuple[int]) -> np.ndarray:
    """
    Function for mapping all spectral types (O through Y) to numbers.

    Parameters
    ----------
    sptype : np.ndarray
        Array with spectral types.
    shape : tuple(int)
        Shape (1D) of the output array

    Returns
    -------
    np.ndarray
        Array with spectral types mapped to numbers.
    """

    spt_disc = np.zeros(shape)

    for i, item in enumerate(sptype):
        if item[0] == "O":
            spt_disc[i] = 0.5

        elif item[0] == "B":
            spt_disc[i] = 1.5

        elif item[0] == "A":
            spt_disc[i] = 2.5

        elif item[0] == "F":
            spt_disc[i] = 3.5

        elif item[0] == "G":
            spt_disc[i] = 4.5

        elif item[0] == "K":
            spt_disc[i] = 5.5

        elif item[0] == "M":
            spt_disc[i] = 6.5

        elif item[0] == "L":
            spt_disc[i] = 7.5

        elif item[0] == "T":
            spt_disc[i] = 8.5

        elif item[0] == "Y":
            spt_disc[i] = 9.5

        else:
            spt_disc[i] = np.nan
            continue

    return spt_disc


@typechecked
def update_labels(param: List[str], object_type: str = "planet") -> List[str]:
    """
    Function for formatting the model parameters to use them as labels
    in the posterior plot.

    Parameters
    ----------
    param : list
        List with names of the model parameters.
    object_type : str
        Object type ('planet' or 'star'). With 'planet', the radius
        and mass are expressed in Jupiter units. With 'star', the
        radius and mass are expressed in solar units.

    Returns
    -------
    list
        List with parameter labels for plots.
    """

    cloud_species = ["fe", "mgsio3", "al2o3", "na2s", "kcl"]

    cloud_labels = ["Fe", r"MgSiO_{3}", r"Al_{2}O_{3}", r"Na_{2}S", "KCl"]

    abund_species = [
        "CO_all_iso",
        "CO_all_iso_HITEMP",
        "H2O",
        "H2O_HITEMP",
        "CH4",
        "NH3",
        "CO2",
        "H2S",
        "Na",
        "Na_allard",
        "Na_burrows",
        "Na_lor_cur",
        "K",
        "K_allard",
        "K_burrows",
        "K_lor_cur",
        "PH3",
        "VO",
        "VO_Plez",
        "TiO",
        "TiO_all_Exomol",
        "FeH",
        "MgSiO3(c)",
        "Fe(c)",
        "Al2O3(c)",
        "Na2S(c)",
        "KCL(c)",
    ]

    abund_labels = [
        "CO",
        "CO",
        "H_{2}O",
        "H_{2}O",
        "CH_{4}",
        "NH_{3}",
        "CO_{2}",
        "H_{2}S",
        "Na",
        "Na",
        "Na",
        "Na",
        "K",
        "K",
        "K",
        "K",
        "PH_{3}",
        "VO",
        "VO",
        "TiO",
        "TiO",
        "FeH",
        "MgSiO_{3}",
        "Fe",
        "Al_{2}O_{3}",
        "Na_{2}S",
        "KCl",
    ]

    if "teff" in param:
        index = param.index("teff")
        param[index] = r"$T_\mathrm{eff}$ (K)"

    if "teff_0" in param:
        index = param.index("teff_0")
        param[index] = r"$T_\mathrm{eff,1}$ (K)"

    if "teff_1" in param:
        index = param.index("teff_1")
        param[index] = r"$T_\mathrm{eff,2}$ (K)"

    if "logg" in param:
        index = param.index("logg")
        param[index] = r"$\log\,g$"

    if "metallicity" in param:
        index = param.index("metallicity")
        param[index] = "[Fe/H]"

    if "feh" in param:
        index = param.index("feh")
        param[index] = "[Fe/H]"

    if "feh_0" in param:
        index = param.index("feh_0")
        param[index] = r"[Fe/H]$_\mathrm{1}$"

    if "feh_1" in param:
        index = param.index("feh_1")
        param[index] = r"[Fe/H]$_\mathrm{2}$"

    if "fsed" in param:
        index = param.index("fsed")
        param[index] = r"$f_\mathrm{sed}$"

    if "fsed_1" in param:
        index = param.index("fsed_1")
        param[index] = r"$f_\mathrm{sed,1}$"

    if "fsed_2" in param:
        index = param.index("fsed_2")
        param[index] = r"$f_\mathrm{sed,2}$"

    if "f_clouds" in param:
        index = param.index("f_clouds")
        param[index] = r"$w_\mathrm{clouds}$"

    if "c_o_ratio" in param:
        index = param.index("c_o_ratio")
        param[index] = r"C/O"

    if "radius" in param:
        index = param.index("radius")
        if object_type == "planet":
            param[index] = r"$R$ ($R_\mathrm{J}$)"
        elif object_type == "star":
            param[index] = r"$R$ ($R_\mathrm{\odot}$)"

    if "distance" in param:
        index = param.index("distance")
        param[index] = "$d$ (pc)"

    if "parallax" in param:
        index = param.index("parallax")
        param[index] = r"$\varpi$ (mas)"

    if "vsini" in param:
        index = param.index("vsini")
        param[index] = r"$v\,\sin\,i$ (km s$^{-1}$)"

    if "mass" in param:
        index = param.index("mass")
        if object_type == "planet":
            param[index] = r"$M$ ($M_\mathrm{J}$)"
        elif object_type == "star":
            param[index] = r"$M$ ($M_\mathrm{\odot}$)"

    if "log_mass" in param:
        index = param.index("log_mass")
        if object_type == "planet":
            param[index] = r"$\log\,M/M_\mathrm{J}$"
        elif object_type == "star":
            param[index] = r"$\log\,M/M_\mathrm{\odot}$"

    if "age" in param:
        index = param.index("age")
        param[index] = "Age (Myr)"

    if "mass" in param:
        index = param.index("mass")
        param[index] = r"$M$ ($M_\mathrm{J}$)"

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"mass_{i}" in param:
            index = param.index(f"mass_{i}")
            param[index] = rf"$M_\mathrm{{{item}}}$ ($M_\mathrm{{J}}$)"
        else:
            break

    if "s_i" in param:
        index = param.index("s_i")
        param[index] = r"$S_\mathrm{i}$ ($k_\mathrm{B}/\mathrm{baryon}$)"

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"s_i_{i}" in param:
            index = param.index(f"s_i_{i}")
            param[index] = rf"$S_\mathrm{{i,{item}}}$ ($k_\mathrm{{B}}/\mathrm{{baryon}}$)"

    if "d_frac" in param:
        index = param.index("d_frac")
        param[index] = r"$\log\,D_\mathrm{i}$"

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"d_frac_{i}" in param:
            index = param.index(f"d_frac_{i}")
            param[index] = rf"$\log\,D_\mathrm{{i,{item}}}$"
        else:
            break

    if "y_frac" in param:
        index = param.index("y_frac")
        param[index] = r"$Y$"

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"y_frac_{i}" in param:
            index = param.index(f"y_frac_{i}")
            param[index] = rf"$Y_\mathrm{{{item}}}$"
        else:
            break

    if "m_core" in param:
        index = param.index("m_core")
        param[index] = r"$M_\mathrm{core}$ ($M_\mathrm{E}$)"

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"m_core_{i}" in param:
            index = param.index(f"m_core_{i}")
            param[index] = rf"$M_\mathrm{{core,{item}}}$ ($M_\mathrm{{E}}$)"
        else:
            break

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"teff_evol_{i}" in param:
            index = param.index(f"teff_evol_{i}")
            param[index] = rf"$T_\mathrm{{eff, {item}}}$ (K)"
        else:
            break

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"radius_evol_{i}" in param:
            index = param.index(f"radius_evol_{i}")
            param[index] = rf"$R_\mathrm{{{item}}}$ ($R_\mathrm{{J}}$)"
        else:
            break

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"logg_evol_{i}" in param:
            index = param.index(f"logg_evol_{i}")
            param[index] = rf"$\log\,g_\mathrm{{{item}}}$"
        else:
            break

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"inflate_lbol{i}" in param:
            index = param.index(f"inflate_lbol{i}")
            param[index] = rf"$\sigma_{{L,{{{item}}}}}$ (dex)"
        else:
            break

    for i, item in enumerate(ascii_lowercase[1:]):
        if f"inflate_mass{i}" in param:
            index = param.index(f"inflate_mass{i}")
            param[index] = rf"$\sigma_{{M,{{{item}}}}}$ ($M_\mathrm{{J}}$)"
        else:
            break

    if "luminosity" in param:
        index = param.index("luminosity")
        param[index] = r"$\log\,L/L_\mathrm{\odot}$"

    if "luminosity_ratio" in param:
        index = param.index("luminosity_ratio")
        param[index] = r"$\log\,L_\mathrm{1}/L_\mathrm{2}$"

    if "luminosity_disk_planet" in param:
        index = param.index("luminosity_disk_planet")
        param[index] = r"$L_\mathrm{disk}/L_\mathrm{atm}$"

    if "lognorm_radius" in param:
        index = param.index("lognorm_radius")
        param[index] = r"$\log\,r_\mathrm{g}$"

    if "lognorm_sigma" in param:
        index = param.index("lognorm_sigma")
        param[index] = r"$\sigma_\mathrm{g}$"

    if "lognorm_ext" in param:
        index = param.index("lognorm_ext")
        param[index] = r"$A_V$"

    if "powerlaw_min" in param:
        index = param.index("powerlaw_min")
        param[index] = r"$\log\,a_\mathrm{min}/\mathrm{µm}$"

    if "powerlaw_max" in param:
        index = param.index("powerlaw_max")
        param[index] = r"$\log\,a_\mathrm{max}/\mathrm{µm}$"

    if "powerlaw_exp" in param:
        index = param.index("powerlaw_exp")
        param[index] = r"$\beta$"

    if "powerlaw_ext" in param:
        index = param.index("powerlaw_ext")
        param[index] = r"$A_V$"

    if "ism_ext" in param:
        index = param.index("ism_ext")
        param[index] = r"$A_V$"

    if "ism_red" in param:
        index = param.index("ism_red")
        param[index] = r"$R_V$"

    if "tint" in param:
        index = param.index("tint")
        param[index] = r"$T_\mathrm{int}$ (K)"

    for i in range(15):
        if f"t{i}" in param:
            index = param.index(f"t{i}")
            param[index] = rf"$T_\mathrm{{{i}}}$ (K)"

    if "alpha" in param:
        index = param.index("alpha")
        param[index] = r"$\alpha$"

    if "log_sigma_alpha" in param:
        index = param.index("log_sigma_alpha")
        param[index] = r"$\log\,\sigma_\alpha$"

    if "log_delta" in param:
        index = param.index("log_delta")
        param[index] = r"$\log\,\delta$"

    if "log_p_quench" in param:
        index = param.index("log_p_quench")
        param[index] = r"$\log\,P_\mathrm{quench}$"

    if "sigma_lnorm" in param:
        index = param.index("sigma_lnorm")
        param[index] = r"$\sigma_\mathrm{g}$"

    if "log_kzz" in param:
        index = param.index("log_kzz")
        param[index] = r"$\log\,K_\mathrm{zz}$"

    if "kzz" in param:
        # Backward compatibility
        index = param.index("kzz")
        param[index] = r"$\log\,K_\mathrm{zz}$"

    for i, item in enumerate(cloud_species):
        if f"{item}_fraction" in param:
            index = param.index(f"{item}_fraction")
            param[index] = (
                rf"$\log\,\tilde{{\mathrm{{X}}}}"
                rf"_\mathrm{{{cloud_labels[i]}}}$"
            )

        if f"{item}_tau" in param:
            index = param.index(f"{item}_tau")
            param[index] = rf"$\bar{{\tau}}_\mathrm{{{cloud_labels[i]}}}$"

    for i, item_i in enumerate(cloud_species):
        for j, item_j in enumerate(cloud_species):
            if f"{item_i}_{item_j}_ratio" in param:
                index = param.index(f"{item_i}_{item_j}_ratio")
                param[index] = (
                    rf"$\log\,\tilde{{\mathrm{{X}}}}"
                    rf"_\mathrm{{{cloud_labels[i]}}}/"
                    rf"\mathrm{{\tilde{{X}}}}_\mathrm{{{cloud_labels[j]}}}$"
                )

    for i, item in enumerate(abund_species):
        if item in param:
            index = param.index(item)
            param[index] = rf"$\log\,\mathrm{{{abund_labels[i]}}}$"

    for i, item in enumerate(param):
        if item[0:8] == "scaling_":
            item_name = item[8:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$a_\mathrm{{{item_name}}}$"

        elif item[0:6] == "error_":
            item_name = item[6:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$b_\mathrm{{{item_name}}}$"

        elif item[0:7] == "radvel_":
            item_name = item[7:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"RV$_\mathrm{{{item_name}}}$ (km s$^{{-1}}$)"

        elif item[0:11] == "wavelength_":
            item_name = item[11:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$c_\mathrm{{{item_name}}}$ (nm)"

        elif item[-6:] == "_error":
            item_name = item[:-6]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$f_\mathrm{{{item_name}}}$"

        elif item[0:9] == "corr_len_":
            item_name = item[9:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$\log\,\ell_\mathrm{{{item_name}}}$"

        elif item[0:9] == "corr_amp_":
            item_name = item[9:]
            if item_name.find("\\_") == -1 and item_name.find("_") > 0:
                item_name = item_name.replace("_", "\\_")
            param[i] = rf"$f_\mathrm{{{item_name}}}$"

    if "c_h_ratio" in param:
        index = param.index("c_h_ratio")
        param[index] = r"[C/H]"

    if "o_h_ratio" in param:
        index = param.index("o_h_ratio")
        param[index] = r"[O/H]"

    for i in range(100):
        if f"teff_{i}" in param:
            index = param.index(f"teff_{i}")
            param[index] = rf"$T_\mathrm{{{i+1}}}$ (K)"

        else:
            break

    for i in range(100):
        if f"radius_{i}" in param:
            index = param.index(f"radius_{i}")
            param[index] = rf"$R_\mathrm{{{i+1}}}$ ($R_\mathrm{{J}}$)"

        else:
            break

    for i in range(100):
        if f"luminosity_{i}" in param:
            index = param.index(f"luminosity_{i}")
            param[index] = rf"$\log\,L_\mathregular{{{i+1}}}/L_\mathregular{{\odot}}$"

        else:
            break

    if "disk_teff" in param:
        index = param.index("disk_teff")
        param[index] = r"$T_\mathrm{disk}$ (K)"

    if "disk_radius" in param:
        index = param.index("disk_radius")
        param[index] = r"$R_\mathrm{disk}$ ($R_\mathrm{J}$)"

    if "log_powerlaw_a" in param:
        index = param.index("log_powerlaw_a")
        param[index] = r"$a_\mathrm{powerlaw}$"

    if "log_powerlaw_b" in param:
        index = param.index("log_powerlaw_b")
        param[index] = r"$b_\mathrm{powerlaw}$"

    if "log_powerlaw_c" in param:
        index = param.index("log_powerlaw_c")
        param[index] = r"$c_\mathrm{powerlaw}$"

    if "pt_smooth" in param:
        index = param.index("pt_smooth")
        param[index] = r"$\sigma_\mathrm{P-T}$"

    if "log_prob" in param:
        index = param.index("log_prob")
        param[index] = r"$\log\,\mathcal{L}$"

    if "log_tau_cloud" in param:
        index = param.index("log_tau_cloud")
        param[index] = r"$\log\,\tau_\mathrm{cloud}$"

    if "veil_a" in param:
        index = param.index("veil_a")
        param[index] = r"$a_\mathrm{veil}$"

    if "veil_b" in param:
        index = param.index("veil_b")
        param[index] = r"$b_\mathrm{veil}$"

    if "veil_ref" in param:
        index = param.index("veil_ref")
        param[index] = r"$F_\mathrm{ref, veil}$"

    if "gauss_amplitude" in param:
        index = param.index("gauss_amplitude")
        param[index] = r"$a$ (W m$^{-2}$ µm$^{-1}$)"

    if "gauss_mean" in param:
        index = param.index("gauss_mean")
        param[index] = r"$\lambda$ (nm)"

    if "gauss_sigma" in param:
        index = param.index("gauss_sigma")
        param[index] = r"$\sigma$ (nm)"

    if "gauss_amplitude_2" in param:
        index = param.index("gauss_amplitude_2")
        param[index] = r"$a_2$ (W m$^{-2}$ µm$^{-1}$)"

    if "gauss_mean_2" in param:
        index = param.index("gauss_mean_2")
        param[index] = r"$\lambda_2$ (nm)"

    if "gauss_sigma_2" in param:
        index = param.index("gauss_sigma_2")
        param[index] = r"$\sigma_2$ (nm)"

    if "gauss_fwhm" in param:
        index = param.index("gauss_fwhm")
        param[index] = r"FWHM (km s$^{-1}$)"

    if "line_flux" in param:
        index = param.index("line_flux")
        param[index] = r"$F_\mathrm{line}$ (W m$^{-2}$)"

    if "line_luminosity" in param:
        index = param.index("line_luminosity")
        param[index] = r"$L_\mathrm{line}$ ($L_\mathrm{\odot}$)"

    if "log_line_lum" in param:
        index = param.index("log_line_lum")
        param[index] = r"$\log\,L_\mathrm{line}/L_\mathrm{\odot}$"

    if "log_acc_lum" in param:
        index = param.index("log_acc_lum")
        param[index] = r"$\log\,L_\mathrm{acc}/L_\mathrm{\odot}$"

    if "line_eq_width" in param:
        index = param.index("line_eq_width")
        param[index] = r"EW ($\AA$)"

    if "line_vrad" in param:
        index = param.index("line_vrad")
        param[index] = r"RV (km s$^{-1}$)"

    if "log_kappa_0" in param:
        index = param.index("log_kappa_0")
        param[index] = r"$\log\,\kappa_0$"

    if "log_kappa_abs" in param:
        index = param.index("log_kappa_abs")
        param[index] = r"$\log\,\kappa_\mathrm{abs}$"

    if "log_kappa_sca" in param:
        index = param.index("log_kappa_sca")
        param[index] = r"$\log\,\kappa_\mathrm{sca}$"

    if "opa_index" in param:
        index = param.index("opa_index")
        param[index] = r"$\xi$"

    if "opa_abs_index" in param:
        index = param.index("opa_abs_index")
        param[index] = r"$\xi_\mathrm{abs}$"

    if "opa_sca_index" in param:
        index = param.index("opa_sca_index")
        param[index] = r"$\xi_\mathrm{sca}$"

    if "log_p_base" in param:
        index = param.index("log_p_base")
        param[index] = r"$\log\,P_\mathrm{cloud}$"

    if "albedo" in param:
        index = param.index("albedo")
        param[index] = r"$\omega$"

    if "opa_knee" in param:
        index = param.index("opa_knee")
        param[index] = r"$\lambda_\mathrm{R}$ (µm)"

    if "lambda_ray" in param:
        index = param.index("lambda_ray")
        param[index] = r"$\lambda_\mathrm{R}$ (µm)"

    if "mix_length" in param:
        index = param.index("mix_length")
        param[index] = r"$\ell_\mathrm{m}$ ($H_\mathrm{p}$)"

    if "spec_weight" in param:
        index = param.index("spec_weight")
        param[index] = r"w$_\mathrm{spec}$"

    if "log_beta_r" in param:
        index = param.index("log_beta_r")
        param[index] = r"$\log\,\beta_\mathrm{r}$"

    if "log_gamma_r" in param:
        index = param.index("log_gamma_r")
        param[index] = r"$\log\,\gamma_\mathrm{r}$"

    if "gamma_r" in param:
        index = param.index("gamma_r")
        param[index] = r"$\gamma_\mathrm{r}$"

    if "log_kappa_gray" in param:
        index = param.index("log_kappa_gray")
        param[index] = r"$\log\,\kappa_\mathrm{gray}$"

    if "log_cloud_top" in param:
        index = param.index("log_cloud_top")
        param[index] = r"$\log\,P_\mathrm{top}$"

    return param


@typechecked
def model_name(in_name: str) -> str:
    """
    Function for updating a model name for use in plots.

    Parameters
    ----------
    in_name : str
        Model name as used by species.

    Returns
    -------
    str
        Updated model name for plots.
    """

    if in_name == "drift-phoenix":
        out_name = "DRIFT-PHOENIX"

    elif in_name == "ames-cond":
        out_name = "AMES-Cond"

    elif in_name == "ames-dusty":
        out_name = "AMES-Dusty"

    elif in_name == "atmo":
        out_name = "ATMO"

    elif in_name == "atmo-ceq":
        out_name = "ATMO CEQ"

    elif in_name == "atmo-neq-weak":
        out_name = "ATMO NEQ weak"

    elif in_name == "atmo-neq-strong":
        out_name = "ATMO NEQ strong"

    elif in_name == "bt-cond":
        out_name = "BT-Cond"

    elif in_name == "bt-cond-feh":
        out_name = "BT-Cond"

    elif in_name == "bt-settl":
        out_name = "BT-Settl"

    elif in_name == "bt-settl-cifist":
        out_name = "BT-Settl"

    elif in_name == "bt-nextgen":
        out_name = "BT-NextGen"

    elif in_name == "petitcode-cool-clear":
        out_name = "petitCODE"

    elif in_name == "petitcode-cool-cloudy":
        out_name = "petitCODE"

    elif in_name == "petitcode-hot-clear":
        out_name = "petitCODE"

    elif in_name == "petitcode-hot-cloudy":
        out_name = "petitCODE"

    elif in_name == "exo-rem":
        out_name = "Exo-REM"

    elif in_name == "planck":
        out_name = "Blackbody radiation"

    elif in_name == "zhu2015":
        out_name = "Zhu (2015)"

    elif in_name == "sonora-cholla":
        out_name = "Sonora Cholla"

    elif in_name == "sonora-bobcat":
        out_name = "Sonora Bobcat"

    elif in_name == "sonora-bobcat-co":
        out_name = "Sonora Bobcat C/O"

    elif in_name == "petitradtrans":
        out_name = "petitRADTRANS"

    else:
        out_name = in_name

        warnings.warn(f"The model name '{in_name}' is not known "
                      "so the output name will not get adjusted "
                      "for plot purposes")

    return out_name


@typechecked
def quantity_unit(
    param: List[str], object_type: str
) -> Tuple[List[str], List[Optional[str]], List[str]]:
    """
    Function for creating lists with quantities, units, and labels
    for fitted parameter.

    Parameters
    ----------
    param : list
        List with parameter names.
    object_type : str
        Object type (``'planet'`` or ``'star'``).

    Returns
    -------
    list
        List with the quantities.
    list
        List with the units.
    list
        List with the parameter labels for plots.
    """

    quantity = []
    unit = []
    label = []

    for item in param:
        if item == "teff":
            quantity.append("teff")
            unit.append("K")
            label.append(r"$T_\mathrm{eff}$")

        if item == "logg":
            quantity.append("logg")
            unit.append(None)
            label.append(r"$\log g$")

        if item == "metallicity":
            quantity.append("metallicity")
            unit.append(None)
            label.append("[Fe/H]")

        if item == "feh":
            quantity.append("feh")
            unit.append(None)
            label.append("[Fe/H]")

        if item == "fsed":
            quantity.append("fsed")
            unit.append(None)
            label.append(r"$f_\mathrm{sed}$")

        if item == "c_o_ratio":
            quantity.append("c_o_ratio")
            unit.append(None)
            label.append("C/O")

        if item == "radius":
            quantity.append("radius")

            if object_type == "planet":
                unit.append(r"$R_\mathrm{J}$")

            elif object_type == "star":
                unit.append(r"$R_\mathrm{\odot}$")

            label.append(r"$R$")

        for i in range(100):
            if item == f"teff_{i}":
                quantity.append(f"teff_{i}")
                unit.append("K")
                label.append(rf"$T_\mathrm{{{i+1}}}$")

            else:
                break

        for i in range(100):
            if item == f"radius_{i}":
                quantity.append(f"radius_{i}")

                if object_type == "planet":
                    unit.append(r"$R_\mathrm{J}$")

                elif object_type == "star":
                    unit.append(r"$R_\mathrm{\odot}$")

                label.append(rf"$R_\mathrm{{{i+1}}}$")

            else:
                break

        if item == "distance":
            quantity.append("distance")
            unit.append("pc")
            label.append(r"$d$")

        if item == "mass":
            quantity.append("mass")

            if object_type == "planet":
                unit.append(r"$M_\mathrm{J}$")

            elif object_type == "star":
                unit.append(r"$M_\mathrm{\odot}$")

            label.append("M")

        if item == "luminosity":
            quantity.append("luminosity")
            unit.append(None)
            label.append(r"$\log\,L/L_\mathrm{\odot}$")

        if item == "ism_ext":
            quantity.append("ism_ext")
            unit.append(None)
            label.append(r"$A_V$")

        if item == "lognorm_ext":
            quantity.append("lognorm_ext")
            unit.append(None)
            label.append(r"$A_V$")

        if item == "powerlaw_ext":
            quantity.append("powerlaw_ext")
            unit.append(None)
            label.append(r"$A_V$")

        if item == "pt_smooth":
            quantity.append("pt_smooth")
            unit.append(None)
            label.append(r"$\sigma_\mathrm{P-T}$")

    return quantity, unit, label


def field_bounds_ticks(field_range):
    """
    Parameters
    ----------
    field_range : tuple(str, str), None
        Range of the discrete colorbar for the field dwarfs. The tuple
        should contain the lower and upper value ('early M', 'late M',
        'early L', 'late L', 'early T', 'late T', 'early Y). The full
        range is used if set to None.

    Returns
    -------
    np.ndarray
    np.ndarray
    list(str, )
    """

    spectral_ranges = ["M0-M4", "M5-M9", "L0-L4", "L5-L9", "T0-T4", "T5-T9", "Y1-Y2"]

    if field_range is None:
        index_start = 0
        index_end = 7

    else:
        if field_range[0] == "early M":
            index_start = 0
        elif field_range[0] == "late M":
            index_start = 1
        elif field_range[0] == "early L":
            index_start = 2
        elif field_range[0] == "late L":
            index_start = 3
        elif field_range[0] == "early T":
            index_start = 4
        elif field_range[0] == "late T":
            index_start = 5
        elif field_range[0] == "early Y":
            index_start = 6

        if field_range[1] == "early M":
            index_end = 1
        elif field_range[1] == "late M":
            index_end = 2
        elif field_range[1] == "early L":
            index_end = 3
        elif field_range[1] == "late L":
            index_end = 4
        elif field_range[1] == "early T":
            index_end = 5
        elif field_range[1] == "late T":
            index_end = 6
        elif field_range[1] == "early Y":
            index_end = 7

    index_range = index_end - index_start + 1

    bounds = np.linspace(index_start, index_end, index_range)
    ticks = np.linspace(index_start + 0.5, index_end - 0.5, index_range - 1)
    labels = spectral_ranges[index_start:index_end]

    return bounds, ticks, labels


@typechecked
def remove_color_duplicates(
    object_names: List[str], empirical_names: np.ndarray
) -> List[int]:
    """ "
    Function for deselecting young/low-gravity objects that will
    already be plotted individually as directly imaged objects.

    Parameters
    ----------
    object_names : list(str)
        List with names of directly imaged planets and brown dwarfs.
    empirical_names : np.ndarray
        Array with names of young/low-gravity objects.

    Returns
    -------
    list
        List with selected indices of the young/low-gravity objects.
    """

    indices = []

    for i, item in enumerate(empirical_names):
        if item == "beta_Pic_b" and "beta Pic b" in object_names:
            continue

        if item == "HR8799b" and "HR 8799 b" in object_names:
            continue

        if item == "HR8799c" and "HR 8799 c" in object_names:
            continue

        if item == "HR8799d" and "HR 8799 d" in object_names:
            continue

        if item == "HR8799e" and "HR 8799 e" in object_names:
            continue

        if item == "kappa_And_B" and "kappa And b" in object_names:
            continue

        if item == "HD1160B" and "HD 1160 B" in object_names:
            continue

        indices.append(i)

    return indices
