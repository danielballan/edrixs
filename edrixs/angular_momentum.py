#!/usr/bin/env python

import numpy as np

def get_ladd(l,ispin=False):
    """
    Get the matrix form of the raising operator :math:`l^+` in the complex spherical harmonics basis

    .. math::

        l^+|l,m> = \\sqrt{(l-m)(l+m+1)} |l,m+1>

    Parameters
    ----------
    l : int
        Orbital angular momentum number.

    ispin : logical     
        Whether including spin or not (default: False).

    Returns
    ----------
    ladd : 2d complex array
        The matrix form of :math:`l^+`.

        If ispin=True, the dimension will be :math:`2(2l+1)\\times 2(2l+1)`,

        otherwise, it will be :math:`(2l+1) \\times (2l+1)`. 
    """

    norbs = 2 * l + 1
    ladd = np.zeros((norbs,norbs), dtype=np.complex128) 
    cone = np.complex128(1.0+0.0j)
    for m in range(-l,l):
        ladd[l+m+1,l+m] = np.sqrt((l - m) * (l + m + 1.0) * cone)
    if ispin:
        ladd_spin = np.zeros((2*norbs,2*norbs), dtype=np.complex128)
        ladd_spin[0:2*norbs:2, 0:2*norbs:2] = ladd
        ladd_spin[1:2*norbs:2, 1:2*norbs:2] = ladd
        return ladd_spin
    else:
        return ladd

def get_lminus(l,ispin=False):
    """
    Get the matrix form of the lowering operator :math:`l^-` in the complex spherical harmonics basis

    .. math::

        l^-|l,m> = \\sqrt{(l+m)(l-m+1)} |l,m-1>

    Parameters
    ----------
    l : int
        Orbital angular momentum number.
    ispin : logical     
        Whether including spin or not (default: False).

    Returns
    ----------
    lminus : 2d complex array
        The matrix form of :math:`l^-`.

        If ispin=True, the dimension will be :math:`2(2l+1)\\times 2(2l+1)`,

        otherwise, it will be :math:`(2l+1) \\times (2l+1)`. 
    """

    norbs = 2 * l + 1
    lminus = np.zeros((norbs,norbs), dtype=np.complex128) 
    cone = np.complex128(1.0+0.0j)
    for m in range(-l+1,l+1):
        lminus[l+m-1,l+m] = np.sqrt((l + m) * (l - m + 1.0) * cone)
    if ispin:
        lminus_spin = np.zeros((2*norbs,2*norbs), dtype=np.complex128)
        lminus_spin[0:2*norbs:2, 0:2*norbs:2] = lminus
        lminus_spin[1:2*norbs:2, 1:2*norbs:2] = lminus
        return lminus_spin
    else:
        return lminus

def get_lx(l,ispin=False):
    """
    Get the matrix form of the orbital angular momentum operator :math:`l_x` in the complex spherical harmonics basis,

    .. math::

        l_x = \\frac{1}{2} (l^+ + l^-)

    Parameters
    ----------
    l : int
        Orbital angular momentum number.

    ispin : logical     
        Whether including spin or not (default: False).

    Returns
    ----------
    lx : 2d complex array
        The matrix form of :math:`l_x`.

        If ispin=True, the dimension will be :math:`2(2l+1)\\times 2(2l+1)`,

        otherwise, it will be :math:`(2l+1) \\times (2l+1)`. 
    """

    if ispin:
        return (get_ladd(l,True) + get_lminus(l,True)) / 2.0
    else:
        return (get_ladd(l) + get_lminus(l)) / 2.0

def get_ly(l,ispin=False):
    """
    Get the matrix form of the orbital angular momentum operator :math:`l_y` in the complex spherical harmonics basis,

    .. math::

        l_y = \\frac{-i}{2} (l^+ - l^-)

    Parameters
    ----------
    l : int
        Orbital angular momentum number.

    ispin : logical     
        Whether including spin or not (default: False).

    Returns
    ----------
    ly : 2d complex array
        The matrix form of :math:`l_y`.

        If ispin=True, the dimension will be :math:`2(2l+1)\\times 2(2l+1)`,

        otherwise, it will be :math:`(2l+1) \\times (2l+1)`. 
    """

    if ispin:
        return (get_ladd(l,True) - get_lminus(l,True)) / 2.0 * -1j
    else:
        return (get_ladd(l) - get_lminus(l)) / 2.0 * -1j
  
def get_lz(l,ispin=False):
    """
    Get the matrix form of the orbital angular momentum operator :math:`l_z` in the complex spherical harmonics basis.

    Parameters
    ----------
    l : int
        Orbital angular momentum number.

    ispin : logical     
        Whether including spin or not (default: False).

    Returns
    -------
    lz : 2d complex array
        The matrix form of :math:`l_z`.

        If ispin=True, the dimension will be :math:`2(2l+1) \\times 2(2l+1)`,

        otherwise, it will be :math:`(2l+1) \\times (2l+1)`. 
    """
    norbs = 2 * l + 1
    lz = np.zeros((norbs,norbs),dtype=np.complex128)
    for m in range(-l,l+1):
        lz[l+m,l+m] = m
    if ispin:
        lz_spin = np.zeros((2*norbs,2*norbs),dtype=np.complex128)
        lz_spin[0:2*norbs:2,0:2*norbs:2] = lz
        lz_spin[1:2*norbs:2,1:2*norbs:2] = lz
        return lz_spin
    else:
        return lz 

def get_pauli():
    """
    Get the Pauli matrix

    Returns
    -------
    sigma : :math:`3\\times 2 \\times 2` complex array.

        sigma[0] is :math:`\\sigma_x`,

        sigma[1] is :math:`\\sigma_y`,

        sigma[2] is :math:`\\sigma_z`,
    """

    sigma = np.zeros((3,2,2),dtype=np.complex128)
    sigma[0,0,1] =  1.0
    sigma[0,1,0] =  1.0
    sigma[1,0,1] = -1.0j
    sigma[1,1,0] =  1.0j
    sigma[2,0,0] =  1.0
    sigma[2,1,1] = -1.0

    return sigma

def get_sx(l):
    """
    Get the matrix form of spin angular momentum operator :math:`s_x` in the complex spherical harmonics basis.

    Parameters
    ----------
    l : int
        Quantum number of orbital angular momentum.

    Returns
    -------
    sx : 2d complex array.
        Matrix form of :math:`s_x`, the dimension is :math:`2(2l+1) \\times 2(2l+1)`,

        Orbital order is: \\|-l,up\\>, \\|-l,down\\>, ..., \\|+l, up\\>, \\|+l,down\\>.
    """
  
    norbs = 2 * (2 * l + 1)
    sx = np.zeros((norbs, norbs),dtype=np.complex128) 
    sigma = get_pauli()
    for i in range(2*l+1):
        sx[2*i:2*i+2,2*i:2*i+2] = sigma[0,:,:]/2.0

    return sx

def get_sy(l):
    """
    Get the matrix form of spin angular momentum operator :math:`s_y` in the complex spherical harmonics basis.

    Parameters
    ----------
    l : int
        Quantum number of orbital angular momentum.

    Returns
    -------
    sy : 2d complex array.
        Matrix form of :math:`s_y`, the dimension is :math:`2(2l+1) \\times 2(2l+1)`, spin order is: 

        Orbital order is: \\|-l,up\\>, \\|-l,down\\>, ..., \\|+l, up\\>, \\|+l,down\\>
    """
 
    norbs = 2 * (2 * l + 1)
    sy = np.zeros((norbs, norbs),dtype=np.complex128) 
    sigma = get_pauli()
    for i in range(2*l+1):
        sy[2*i:2*i+2,2*i:2*i+2] = sigma[1,:,:]/2.0

    return sy

def get_sz(l):
    """
    Get the matrix form of spin angular momentum operator :math:`s_z` in the complex spherical harmonics basis.

    Parameters
    ----------
    l : int
        Quantum number of orbital angular momentum.

    Returns
    -------
    sz : 2d complex array.
        Matrix form of :math:`s_z`, the dimension is :math:`2(2l+1) \\times 2(2l+1)`.

        Orbital order is: \\|-l,up\\>, \\|-l,down\\>, ..., \\|+l, up\\>, \\|+l,down\\>
    """
  
    norbs = 2 * (2 * l + 1)
    sz = np.zeros((norbs, norbs),dtype=np.complex128) 
    sigma = get_pauli()
    for i in range(2*l+1):
        sz[2*i:2*i+2,2*i:2*i+2] = sigma[2,:,:]/2.0

    return sz

def euler_to_rmat(alpha, beta, gamma):
    """
    Given Euler angle: :math:`\\alpha, \\beta, \\gamma`, generate the :math:`3\\times 3` rotational matrix :math:`R`.

    Parameters
    ----------
    alpha : float
        Euler angle, in radian, [0, :math:`2\\pi`]

    beta : float   
        Euler angle, in radian, [0, :math:`\\pi`]

    gamma : float
        Euler angle, in radian, [0, :math:`2\\pi`]
   
    Returns
    ----------
    rmat : 2d float array
        The :math:`3\\times 3` rotational matrix.
    """

    rmat=np.zeros((3,3), dtype=np.float64)
    rmat[0,0] =  np.cos(alpha) * np.cos(beta) * np.cos(gamma) - np.sin(alpha) * np.sin(gamma)
    rmat[0,1] = -np.sin(gamma) * np.cos(alpha) * np.cos(beta) - np.sin(alpha) * np.cos(gamma)
    rmat[0,2] =  np.cos(alpha) * np.sin(beta)
    rmat[1,0] =  np.sin(alpha) * np.cos(beta) * np.cos(gamma) + np.cos(alpha) * np.sin(gamma)
    rmat[1,1] = -np.sin(gamma) * np.sin(alpha) * np.cos(beta) + np.cos(alpha) * np.cos(gamma)
    rmat[1,2] =  np.sin(alpha) * np.sin(beta)
    rmat[2,0] = -np.cos(gamma) * np.sin(beta)
    rmat[2,1] =  np.sin(beta) * np.sin(gamma)
    rmat[2,2] =  np.cos(beta)
    return rmat

def rmat_to_euler(rmat):
    """
    Given the :math:`3\\times 3` rotational matrix :math:`R`, return the Euler angles: :math:`\\alpha, \\beta, \\gamma`.

    Parameters
    ----------
    rmat :  2d float array
        The :math:`3\\times 3` rotational matrix :math:`R`.

    Returns
    ---------
    alpha : float
        Euler angle :math:`\\alpha` in radian, [0, :math:`2\\pi`].

    beta : float   
        Euler angle :math:`\\beta` in radian, [0, :math:`\\pi`].

    gamma : float
        Euler angle :math:`\\gamma` in radian, [0, :math:`2\\pi`]
   
    """

    if np.abs(rmat[2,2]) < 1.0:
        beta = np.arccos(rmat[2,2]) 

        cos_gamma = -rmat[2,0] / np.sin(beta)
        sin_gamma =  rmat[2,1] / np.sin(beta)
        gamma = where_is_angle(sin_gamma, cos_gamma)
        
        cos_alpha = rmat[0,2] / np.sin(beta)
        sin_alpha = rmat[1,2] / np.sin(beta)
        alpha = where_is_angle(sin_alpha, cos_alpha)
    else:
        if rmat[2,2] > 0:
            beta = 0.0
        else:
            beta = np.pi
        gamma = 0.0
        alpha = np.arccos(rmat[1,1])
    return alpha, beta, gamma

def where_is_angle(sina, cosa):
    """
    Given sine and cosine of an angle :math:`\\alpha`, return the angle :math:`\\alpha` range from [0, :math:`2\\pi`].

    Parameters
    ----------
    sina :  float
        :math:`\\sin(\\alpha)`.

    cosa :  float  
        :math:`\\cos(\\alpha)`.

    Returns
    ----------
    alpha : float
        The angle :math:`\\alpha` in radian [0, :math:`2\\pi`].
    """

    if cosa > 1.0:
        cosa =1.0
    elif cosa < -1.0:
        cosa = -1.0
    alpha = np.arccos(cosa)
    if sina < 0.0:
        alpha = 2.0 * np.pi - alpha
    return alpha

def dmat_spinor(alpha,beta,gamma):
    """
    Given three Euler angle: :math:`\\alpha, \\beta, \\gamma`, return the transformation
    matrix for :math:`\\frac{1}{2}`-spinor.
   
    Parameters
    ----------
    alpha : float
        Euler angle :math:`\\alpha` in radian [0, :math:`2\\pi`].

    beta : float
        Euler angle :math:`\\beta` in radian [0, :math:`\\pi`].

    gamma : float   
        Euler angle :math:`\\gamma` in radian [0, :math:`2\\pi`].
    
    Returns
    -------
    dmat :  2d complex array
        The :math:`2\\times 2` transformation matrix.
    """

    dmat = np.zeros((2,2), dtype=np.complex128)
    dmat[0,0] =  np.exp(-(alpha+gamma)/2.0 * 1j) * np.cos(beta/2.0) 
    dmat[0,1] = -np.exp(-(alpha-gamma)/2.0 * 1j) * np.sin(beta/2.0) 
    dmat[1,0] =  np.exp( (alpha-gamma)/2.0 * 1j) * np.sin(beta/2.0) 
    dmat[1,1] =  np.exp( (alpha+gamma)/2.0 * 1j) * np.cos(beta/2.0) 
    return dmat

def zx_to_rmat(z,x):
    """
    Given :math:`z` vector and :math:`x` vector, calculate :math:`y` vector which satisfies the right-hand Cartesian coordinate
    and normalize them to unit if needed, and then return the :math:`3\\times 3` rotational matrix :math:`R`.

    Parameters
    ----------
    z : 1d float array
        The :math:`z` vector.

    x : 1d float array
        The :math:`x` vector.
    
    Returns
    ---------
    rmat : 2d float array
        The :math:`3\\times 3` rotational matrix :math:`R`.
    """

    z = np.array(z, dtype=np.float64) 
    x = np.array(x, dtype=np.float64) 
    xx = x / np.sqrt(np.dot(x,x))
    zz = z / np.sqrt(np.dot(z,z))
    yy = np.cross(zz,xx)

    rmat = np.zeros((3,3), dtype=np.float64)
    rmat[:,0] = xx
    rmat[:,1] = yy
    rmat[:,2] = zz

    return rmat
