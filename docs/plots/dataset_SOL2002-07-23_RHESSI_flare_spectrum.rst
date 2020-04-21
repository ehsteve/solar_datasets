RHESSI Spectrum of an X-class flare
===================================

.. plot::
    :include-source:

    import matplotlib.pyplot as plt
    import astropy.units as u
    from astropy.visualization import quantity_support
    quantity_support()

    import solar_datasets as sd
    data = sd.load_dataset('SOL2002-07-23_RHESSI_flare_spectrum.csv')

    plt.title(data.meta['description'])
    plt.plot(data['bin_mean'], data['flux'])
    plt.yscale('log')
    plt.xscale('log')
    plt.show()