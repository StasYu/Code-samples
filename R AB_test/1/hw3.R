setwd("/Users/stanislavsergeevich/Rstudio/Homework/AB_test/3")
library("readxl")
library("tidyverse")
dat <- read_excel("data_jewelry.xlsx")

a_dat <- dat %>% filter(Variant == 90 )
b_dat <- dat %>% filter(Variant == 10)

a_cnt <- a_dat[["cnt(addToCart)"]]
b_cnt <- b_dat[["cnt(addToCart)"]]

a_sum <- a_dat[["sum(addToCartItems)"]]
b_sum <- b_dat[["sum(addToCartItems)"]]


diff_control <- mean(b_cnt - a_cnt)
diff_sum_control <- mean(b_sum - a_sum)
mean(a_cnt)

n <- 1000
dif_list <- rep(NA, n)

for (i in 1:n){
  a_temp <- sample(a_cnt, replace=TRUE)
  b_temp <- sample(b_cnt, replace=TRUE)
  diff_temp <- mean(b_temp - a_temp)
  dif_list[i] <- diff_temp
}


dif_list <- data.frame(dif=dif_list)
dif_list$centered <- dif_list$dif - mean(dif_list$dif)
p_value <- sum(dif_list$centered >= diff_control) / n

sum(dif_list$centered >= diff_control)

str(dif_list)
ggplot(data = dif_list, aes(x=centered)) +
  geom_histogram(fill="lightblue", color="navy") + 
  geom_vline(xintercept = diff_control, color="red")

#делаем вывод что количество заказов не поменялось при уровне значимости 5%, pvalue = 0.445 > 0.05
dif_list2 <- rep(NA, n)

for(i in 1:n){
  sum_temp1 <- sample(a_sum, replace = TRUE)
  sum_temp2 <- sample(b_sum, replace = TRUE)
  temp_dif <- mean(sum_temp2 - sum_temp1)
  dif_list2[i] <- temp_dif
}

dif_list2 <- data.frame(dif=dif_list2)
dif_list2$cent <- dif_list2$dif - mean(dif_list2$dif)

pvalue2 <- sum(dif_list2$cent >= diff_sum_control) / n
