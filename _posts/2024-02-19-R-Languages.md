---
layout: post
subtitle: R Languages
categories: [R]
header:
    image: header.jpg
    align:
    text: light
---

# R basic

## Functions

``` R
dataset <- read.csv(file = "data/house-data.csv", 
                    header = TRUE, # 显示字段名
                    stringsAsFactors = TRUE, # 字符串转换为因子
                    na.strings = c("NA")) # 缺失值填充为NA
str(dataset)

library(summarytools) # install.packages("summarytools")
Arrests %>% 
  dfSummary(col.widths = c(10,80,150,120,120,180,220)) %>% # 设置列宽
  view(method = "render") # 设置显示方式

```

```R
is.na() # 判断是否有缺失值
sum() # 求和
str() # 查看数据结构
data() # 查看数据
head() # 查看前几行
summary() # 查看数据概况
dim() # 查看数据维度
duplicated() # 判断是否有重复值
dplyr::mutate(id = paste("Person",1:nrow(.), sep="-")) # 添加一列
any()
paste0()
sample()
set.seed()
runif()
filter()
dots()
hist()
floor()
data.frame()

levels(Arthritis$Improved) # 列出因子变量的水平（名称）
nlevels(Arthritis$Improved) # 返回因子变量的水平数
select() # 选择变量

table() # 统计因子变量的频数
table(useNA = "ifany") # 统计因子变量的频数，包括缺失值

proportions() # 计算因子变量的频率

library(graphics)
Arthritis %>% 
  select(Improved) %>% 
  table() %>% 
  barplot(main = "Improved")

Arthritis %>% 
  select(Improved) %>% 
  table() %>% 
  graphics::pie(main = "Improved")

# Bar chart
Arthritis %>% 
  select(Improved, Treatment) %>% 
  table() %>% 
  barplot(beside = TRUE, col = c("red","green", "blue"), main = "Improved")
legend("top", legend = c("None", "Some", "Marked"), col = c("red","green", "blue"), pch=15)

# Stacked bar chart
Arthritis %>% 
  select(Improved, Treatment) %>% 
  table() %>% 
  barplot(beside = TRUE, col = c("red","green", "blue"), main = "Improved")
legend("top", legend = c("None", "Some", "Marked"), col = c("red","green", "blue"), pch=15)

# Mosaic chart
Arthritis %>% 
  select(Treatment, Improved) %>% 
  table() %>% 
  mosaicplot(main = "Arthritis")
```

## Random number

> runif(n, min = 0, max = 1)

Arguments

n number of observations. If length(n) > 1, the length is taken to be the number required.
min, max lower and upper limits of the distribution. Must be finite.
If min or max are not specified they assume the default values of 0 and 1 respectively. The uniform distribution has density f(x) = 1/(max-min) for min ≤ x ≤ max.

