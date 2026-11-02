"""Laboratorios OJS de A1 (matrices estructuradas): se calculan sin errores y responden a los controles.

Cada laboratorio está en su apartado: A1.1 (condicionamiento), A1.4 (Toeplitz), A1.5 (Hankel)
y A1.6 (circulantes). Requiere el sitio renderizado (`quarto render`) y Chromium.
"""
import re

import pytest

from test_fase2 import abre, fija, navegador, salidas, sin_errores  # noqa: F401

LABS = {
    "cond": ("algebra/matrices/a1-1.html", "κ₂(A) ="),
    "toeplitz": ("algebra/matrices/a1-4.html", "Estimados con Yule–Walker"),
    "hankel": ("algebra/matrices/a1-5.html", "Error RMS de la reconstrucción"),
    "circ": ("algebra/matrices/a1-6.html", "Diferencia máxima entre la circular directa"),
}


def numero(texto, patron):
    return float(re.search(patron, texto).group(1))


@pytest.mark.parametrize("lab", sorted(LABS))
def test_sin_errores_de_consola_ni_celdas_rotas(navegador, lab):
    sin_errores(abre(navegador, *LABS[lab]))


def test_condicionamiento_cumple_la_cota_y_crece_al_bajar_epsilon(navegador):
    pagina = abre(navegador, *LABS["cond"])
    fija(pagina, "ε (adimensional)", 0.1)
    fija(pagina, "δ (perturbación", 0.05)
    t = salidas(pagina, "κ₂(A) =")[0]
    k1 = numero(t, r"κ₂\(A\) = ([0-9]+(?:\.[0-9]+)?)")
    assert abs(k1 - 42.1) < 0.2 and "✓" in t
    fija(pagina, "ε (adimensional)", 0.01)
    t = salidas(pagina, "κ₂(A) =")[0]
    assert numero(t, r"κ₂\(A\) = ([0-9]+(?:\.[0-9]+)?)") > 5 * k1 and "✓" in t


def test_toeplitz_el_ruido_de_medida_sesga_yule_walker(navegador):
    pagina = abre(navegador, *LABS["toeplitz"])
    def phi1():
        t = salidas(pagina, "Estimados con Yule–Walker")[0]
        return numero(t, r"φ̂ = \(([0-9.-]+),")
    fija(pagina, "ruido de medida", 0)
    sin_ruido = phi1()
    fija(pagina, "ruido de medida", 1.5)
    con_ruido = phi1()
    teorico = numero(salidas(pagina, "Coeficientes teóricos")[0], r"φ = \(([0-9.-]+),")
    assert abs(sin_ruido - teorico) < 0.1          # sin ruido, Yule–Walker recupera el coeficiente
    assert abs(con_ruido - teorico) > abs(sin_ruido - teorico) + 0.2   # con ruido de medida, queda sesgado


def test_ssa_reconstruye_mejor_que_la_senal_ruidosa(navegador):
    pagina = abre(navegador, *LABS["hankel"])
    fija(pagina, "ruido σ", 0.2)
    t = salidas(pagina, "Error RMS de la reconstrucción")[0]
    err = numero(t, r"limpia: ([0-9.]+)")
    err_ruido = numero(t, r"sin tratar: ([0-9.]+)")
    assert err < 0.5 * err_ruido


def test_convolucion_circular_difiere_de_la_lineal_salvo_con_relleno(navegador):
    pagina = abre(navegador, *LABS["circ"])
    t = salidas(pagina, "Diferencia máxima entre la circular directa")[0]
    assert "no coinciden" in t                      # señal al final del registro y sin relleno: se envuelve
    pagina.locator("form", has=pagina.locator("label", has_text="relleno de ceros")).locator("input[type=checkbox]").check()
    pagina.wait_for_timeout(500)
    t = salidas(pagina, "Diferencia máxima entre la circular directa")[0]
    assert "coinciden (basta el relleno" in t
