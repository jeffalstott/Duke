def mat(name, array='M1L'):
    from scipy.io import loadmat
    from numpy import zeros
    if name=='Kudzu':
        path = '/data/alstottj/Duke/Kudzu/ku122005/lfp/cont-vars/'
    elif name=='Tatiana':
        path = '/data/alstottj/Duke/Tatiana/ta012405/lfp/cont-vars/'

    filename = path+array+'.mat'
    matfile = loadmat(filename)

    n_channels=0
    for i in matfile.keys():
        if i.startswith('AD'):
            n_channels+=1

    time_points = max(matfile['AD01'].shape)

    data = zeros(n_channels,time_points)
    for i in range( n_channels):
        var = 'AD'+str(i+1).zfill(2)
        data[i] = matfile[var].flatten()

    return data
