# Sample code from Risk Management

y=seq(30,170,.1)
f1=dnorm(y,70,10)
f2=dnorm(y,80,14)
f3=dnorm(y,110,20)

#Plotting the data

plot(y,f1,typ="l",col="darkgreen",lwd=2)
lines(y,f2,col="darkred",lwd=2)
lines(y,f3,col="darkblue",lwd=2)

f1a=dnorm(y,70,10)*.7
f2a=dnorm(y,80,14)*.2
f3a=dnorm(y,110,20)*.1

plot(y,f1a,typ="l",col="darkgreen",lwd=2)
lines(y,f2a,col="darkred",lwd=2)
lines(y,f3a,col="darkblue",lwd=2)

abline(v=90)

g1=dnorm(90,70,10)*.7
g2=dnorm(90,80,14)*.2
g3=dnorm(90,110,20)*.1

g=(g1+g2+g3)

p1=g1/g
p2=g2/g
p3=g3/g

p1+p2+p3

#Updating with whacky prior

prior=function(p) (dbeta(p,.5,3)+dbeta(p,2,.1))*(p<.4 | p>.6)

like=function(p) p*(1-p)

p=seq(.01,.99,.001)
plot(p,prior(p),typ='l',axes=F,col='darkred',lwd=2)
axis(1)
lines(p,10*like(p),col='darkblue',lwd=2)
lines(p,10*like(p)*prior(p),col='darkgreen',lwd=2,lty=2)

