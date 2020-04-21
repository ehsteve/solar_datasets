Differential Emission Measure of a solar flare
==============================================

.. plot::
    :include-source:

    import matplotlib.pyplot as plt
    import astropy.units as u
    from astropy.visualization import quantity_support
    quantity_support()

    import solar_datasets as sd
    data = sd.load_dataset('dem_SOL1995-08-09_flare.csv')

    plt.title(data.meta['description'])
    plt.plot(data['temperature'], data['dem'])
    plt.xlabel('Log(Temperature[K]')
    plt.show()