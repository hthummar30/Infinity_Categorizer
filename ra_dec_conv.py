def ra_dec_conv(RA, DEC):
    '''
    this function converts RA and DEC in 'hh:mm:ss.s -dd:mm:ss.s' to degrees.
    ra_dec_conv('00:00:00.4', '-10:22:25.7')
    
    '''
    RAs = RA[-4:]
    RAm = RA[-7:-5]
    RAh = RA[-10:-8]
    if RAh == '':
        RAh = '00'
    ra_d = 15*(float(RAh) + float(RAm)/60 + float(RAs)/3600)

    DECs = DEC[-4:]
    DECm = DEC[-7:-5]
    DECd = DEC[-10:-8]
    y = DEC[-11:-10]
    if y == '-':
        sign = -1
    if y == '+':
        sign = +1
    dec_d = (sign*(float(DECd) + float(DECm)/4 + float(DECs)/240))
    
    return (ra_d, dec_d)
