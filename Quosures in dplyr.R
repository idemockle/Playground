mydescribe <- function(df, varname){
  varname <- enquo(varname)
  df %>% summarize(nmeters=n_distinct(deviceid), npoints=n(), mean=mean(!!varname), stdev=sd(!!varname), min=min(!!varname), max=max(!!varname), range=max-min)
}
