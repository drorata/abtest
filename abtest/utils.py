import pandas as pd
import numpy as np


def cr_uplift(control, variant, round=None):
    """
    Compute uplift

    Parameters
    ----------
    control : float
        Proportion in control group
    variant : float
        Proportion in variant group
    round
        If int rounds the results to this number of decimals. Otherwise,
        no rounding

    Returns
    -------
    dict
        holding `diff` for the signed difference between the proportions and
        `upli` for the uplift in percentage
    """

    abs_change = variant - control
    pct_chnage = 100 * abs_change / control

    if type(round) is int:
        return {
            "diff": np.round(abs_change, decimals=round),
            'upli': np.round(pct_chnage, decimals=round)
        }
    else:
        return {
            "diff": abs_change,
            "upli": pct_chnage
        }


def generate_experiment(seed=42, N=10000, control_cr=None, variant_cr=None):
    """
    Generate a single experiment

    Parameters
    ----------
    seed : int
        Seed for random numbers generator
    N : int
        Number of observations in the experiment
    control_cr : float
        Probability of success for the control group in (0,1) interval
    variant_cr : float
        Probability of success for the control group in (0,1) interval

    Returns
    -------
    pd.DataFrame

        For example:
                 Converted  Visited  CR_pct
        Control        594     2000    29.7
        Variant        612     2000    30.6
    """
    np.random.seed(seed)
    control = np.random.choice([0, 1], p=[1-control_cr, control_cr], size=N)
    variant = np.random.choice([0, 1], p=[1-variant_cr, variant_cr], size=N)
    res = pd.DataFrame(
        {
            "Converted": [control.sum(), variant.sum()],
            "Visited": [N, N]
        }, index=['Control', 'Variant'])
    res['CR_pct'] = 100 * res.Converted / res.Visited
    return res
