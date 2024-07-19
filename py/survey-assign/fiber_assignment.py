import numpy as np

def get_faprob(targdens, fp_area=8.63, fib_patrol_area=0.0015, n_fibers=13000):
    """
    Calculate the fiber assignment probability for a given target density.

    This function simulates the fiber assignment process and calculates the
    probability of assigning fibers to targets based on the given parameters.

    Args:
        targdens (float): Target density (targets per square degree).
        fp_area (float, optional): Focal plane area in square degrees. Defaults to 8.63.
        fib_patrol_area (float, optional): Fiber patrol area in square degrees. Defaults to 0.0015.
        n_fibers (int, optional): Number of available fibers. Defaults to 13000.

    Returns:
        tuple: A tuple containing:
            - int: Number of assigned fibers
            - int: Total number of targets
    """
    n_targets = int(targdens * fp_area)
    n_assigned_fibers = 0
    fa_prob = 0.0
    if n_targets > 0:
        for target in range(n_targets):
            prob = (n_fibers - n_assigned_fibers) * fib_patrol_area / fp_area
            prob = max(0, min(1, prob))  # (forced in range [0,1])
            n_assigned_fibers += prob
        faprob = n_assigned_fibers / n_targets
    return int(n_assigned_fibers), int(n_targets)

def get_faprob_total(targdens_list, fp_area=8.63, fib_patrol_area=0.0015, n_fibers=13000):
    """
    Calculate the total fiber assignment probability for multiple target types.

    This function iterates through a list of target densities, simulating the
    fiber assignment process for each type and calculating the overall
    fiber assignment probability.

    Args:
        targdens_list (list): List of target densities for different types.
        fp_area (float, optional): Focal plane area in square degrees. Defaults to 8.63.
        fib_patrol_area (float, optional): Fiber patrol area in square degrees. Defaults to 0.0015.
        n_fibers (int, optional): Number of available fibers. Defaults to 13000.

    Returns:
        tuple: A tuple containing:
            - float: Overall fiber assignment probability
            - numpy.ndarray: Array of assigned fibers for each target type
    """
    n_type = len(targdens_list)
    n_assigned_fibers = np.zeros(n_type)
    n_targets = np.zeros(n_type)

    for i in range(n_type):
        n_assigned_fibers[i], n_targets[i] = get_faprob(targdens_list[i], 
                                              fib_patrol_area=fib_patrol_area,
                                              n_fibers=n_fibers-np.sum(n_assigned_fibers))
    fa_prob = 0.0
    a = 0.0
    b = 0.0
    for i in range(n_type):
        a += n_assigned_fibers[i]
        b += n_targets[i]
    fa_prob = a/b
    return fa_prob, n_assigned_fibers 

# Note: This code was originally written by Julien Guy and adapted from
# Anand Raichoor's presentation at the March 29, 2023 Stage 5 workshop in Napa Valley.
# Source: https://desi.lbl.gov/DocDB/cgi-bin/private/RetrieveFile?docid=7454;filename=Raichoor_29Mar2023.pdf
# The default numbers were updated on 21.02.2024 to reflect the SpecS5 conditions
# in the HEPAP response document.
