
    
def abcal(env_type = None,h_tx = None,h_rx = None): 
    if (env_type == 1):
        p00 = 11.65
        p10 = 0.09602
        p01 = - 0.5132
        p20 = - 0.0005337
        p11 = 0.00016
        p02 = 0.004121
        p30 = 1.29e-06
        p21 = - 2.302e-06
        p12 = - 3.251e-06
        p03 = 4.431e-06
        x = h_tx
        y = h_rx
        a = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
        p00 = 0.2563
        p10 = - 0.003585
        p01 = 0.02042
        p20 = 3.678e-05
        p11 = - 0.0004602
        p02 = 0.001625
        p30 = - 7.687e-08
        p21 = 4.084e-07
        p12 = 5.602e-06
        p03 = - 3.432e-05
        b = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    else:
        if (env_type == 2):
            p00 = 8.931
            p10 = 0.07222
            p01 = - 0.315
            p20 = - 0.0002272
            p11 = - 0.002187
            p02 = 0.0008611
            p30 = 3.317e-07
            p21 = 2.134e-06
            p12 = 1.989e-05
            p03 = 3.546e-05
            x = h_tx
            y = h_rx
            a = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
            p00 = 0.5749
            p10 = - 0.0142
            p01 = 0.06195
            p20 = 0.0001321
            p11 = - 0.0008461
            p02 = 0.001114
            p30 = - 3.158e-07
            p21 = 9.695e-07
            p12 = 1.031e-05
            p03 = - 3.711e-05
            b = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
        else:
            if (env_type == 3):
                p00 = 5.801
                p10 = 0.01647
                p01 = - 0.5252
                p20 = - 6.775e-05
                p11 = - 0.0005364
                p02 = 0.01483
                p30 = 1.087e-07
                p21 = 7.979e-07
                p12 = 4.8e-06
                p03 = - 0.0001331
                x = h_tx
                y = h_rx
                a = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
                p00 = 1.175
                p10 = - 0.02026
                p01 = 0.08833
                p20 = 0.0001719
                p11 = - 0.0005683
                p02 = - 0.001965
                p30 = - 4.297e-07
                p21 = 4.368e-07
                p12 = 8.604e-06
                p03 = 3.147e-06
                b = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
            else:
                p00 = 11.65
                p10 = 0.09602
                p01 = - 0.5132
                p20 = - 0.0005337
                p11 = 0.00016
                p02 = 0.004121
                p30 = 1.29e-06
                p21 = - 2.302e-06
                p12 = - 3.251e-06
                p03 = 4.431e-06
                x = h_tx
                y = h_rx
                a = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
                p00 = 0.2563
                p10 = - 0.003585
                p01 = 0.02042
                p20 = 3.678e-05
                p11 = - 0.0004602
                p02 = 0.001625
                p30 = - 7.687e-08
                p21 = 4.084e-07
                p12 = 5.602e-06
                p03 = - 3.432e-05
                b = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p30 * x ** 3 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    
    if (a < 0):
        a_para = 0
    else:
        a_para = a
    
    if (b < 0):
        b_para = 0
    else:
        b_para = b
    
    return a_para,b_para
    
    return a_para,b_para