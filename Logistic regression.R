library(ggplot2)
library(dplyr)

mydata <- tibble(
    x0 = rep(1,10),
    x1 = c(1:5, 1:5),
    x2 = c(1:5, (1:5)+2),
    y = c(rep(0,5),rep(1,5))
    )

# Logistic Regression function
glmres <- glm(y ~ . - 1, data = mydata)

yint <- (.5-glmres$coefficients["x0"])/glmres$coefficients["x2"]
slope = -glmres$coefficients["x1"]/glmres$coefficients["x2"]
ggplot(mydata, aes(x1, x2, color = as.factor(y))) + geom_point() + geom_abline(slope = slope, intercept = yint)


numpts <- 300
glmmesh <- data.frame(
                x1 = rep(seq(3.5, 6.5, length.out = numpts), each = numpts),
                x2 = rep(seq(3.5, 6.5, length.out = numpts), times = numpts)
           ) %>% 
           mutate(y = rowSums(t(glmres$coefficients *
                              t(matrix(c(
                                       rep(1,numpts^2),
                                       x1,
                                       x2
                                     ),
                                     ncol = 3
                              )))
                      ),
                  ybin = round(y)
           )

f = function(x,y) {
    return(glmres$coefficients[1] +
               glmres$coefficients[2]*x +
               glmres$coefficients[3]*y)
}

# The stock contour function seems to be more reliable than the 
# ggplot one, or maybe I'm missing something
contourdata <- list(x = seq(3.5, 6.5, length.out = numpts),
                    y = seq(3.5, 6.5, length.out = numpts))
contourdata$z <- outer(contourdata$x, contourdata$y, f)

contour(contourdata, levels = .5)

ggplot() +
    geom_point(
        data = mydata,
        mapping = aes(
                    x = x1,
                    y = x2,
                    color = as.factor(y)
                    )
    ) +
    geom_contour(aes(x = x1, y = x2, z = ybin), data = glmmesh, bins = 2)