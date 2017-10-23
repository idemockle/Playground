# PCA

sigma <- 1/nrow(Xscaled) * t(Xscaled) %*% Xscaled
rs <- svd(sigma)
totald=sum(rs$d)
kept.var <- numeric(ncol(Xscaled))
runningsum <- 0
for (i in 1:640){runningsum <- runningsum + rs$d[i]; kept.var[i] <- runningsum}

ur <- rs$u[1:5]
Z <- Xscaled %*% ur
Xproj <- Z %*% t(ur)
