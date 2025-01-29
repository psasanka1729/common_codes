
"""
This function takes a sorted array of eigenvalues and computes the level spacing ratios, which are useful in the study of random matrix theory and quantum chaos.
What this code does:
     - Computes the consecutive level spacings (differences between consecutive eigenvalues).
     - Calculates the level spacing ratios r_n, which are the minimum of consecutive spacings divided by the maximum of consecutive spacings.
"""

def compute_level_spacing_ratios(eigenvalues):

    """
    Compute the level spacing ratios r_n for a given set of eigenvalues.

    Parameters:
        eigenvalues (np.array): Sorted array of eigenvalues.
    
    Returns:
        r_n (np.array): Array of level spacing ratios.
    """
    # Compute consecutive level spacings
    delta_E = np.diff(eigenvalues)  # ΔE_n = E_n - E_{n-1}
    
    # Compute r_n for all n
    r_n = np.minimum(delta_E[:-1], delta_E[1:]) / np.maximum(delta_E[:-1], delta_E[1:])
    
    return r_n