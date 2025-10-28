

def simple_interest(prin,ny,roi):
 """
 calculating SI
 :param prin:principal amount
 :param ny: no of years
 :param roi: rate of interest
 :return:si,amount

 """
 si=prin*ny*roi/100
 amt=prin+si
 return si,amt


def compound_interest(prin, t, roi):
 """
    calculating CI
    :param prin:principal amount
    :param ny: no of years
    :param roi: rate of interest
    :return:amount

"""
 amount=prin*((1+(roi/100))**(1*t))
 return amount