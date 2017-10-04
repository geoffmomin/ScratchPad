# Chi-Squared Test for Fluctuations

flux = [639, 680, 609, 576, 660, 648, 572, 587, 666, 545, 578, 648, 589, 710, 705, 678, 664, 653, 609, 575, 631, 672,
        671, 581, 622, 588, 553, 657, 633, 642, 598, 670, 654, 730, 725, 610, 638, 538, 687, 512]
mean = 627.575
n = 40
i = 0
chi = 0

while i <= 39:
    chi = chi + ((flux[i]-mean)**2)/mean
    print(chi)
    i += 1

reduced = chi/(n-1)
print(chi)
print(reduced)
