Differential Emission Measure of the Quiet Sun
==============================================

.. plot::
    :include-source:

    import matplotlib.pyplot as plt
    import astropy.units as u
    from astropy.visualization import quantity_support
    quantity_support()

    import solar_datasets as sd
    data = sd.load_dataset('dem_quiet_sun.csv')

    plt.title(data.meta['description'])
    plt.plot(data['temperature'], data['dem'])
    plt.xlabel('Log(Temperature[K]')
    plt.show()