---
layout: post
subtitle: Based on Lectuer handout & Learnning processes
categories: [R]
header:
    image: header.jpg
    align:
    text: light
---

# Introduction to Data Science

## Basic Concepts

### Cases

> Cases aka rows, observations, records, units, instances

### Variables

> Variables aka columns, fields, attributes, features, measurements, properties, parameters

#### Variables Categories

- Categorical (qualitative) variables (aka factors, discrete)
  - Nominal variables (no order) 
  - Ordinal variables (order)
  - Cyclic variables (circular order, e.g. days of the week, months of the year, etc.
- Quantitative (numerical) variables
  - continuous variables
  - discrete variables

#### Variable roles

- Explanatory aka x, predictor, independent, input variable
- Response aka y, target, dependent, outcome, output variable
- Identifiers aka key, index, unique identifier, unique key, unique index, row name, ID
- Confounding - a third variable that affects the relationship between the explanatory and response variables aka lurking, hidden, nuisance, spurious variable

#### Assocation & Causation

- Association: a statistical relationship between two variables
- Causation: a cause-and-effect relationship between two variables

### Randomised experiment

- The control group is that which receives no treatment
- The treatment group is that which receives the treatment
- A placebo is that which receives a fake treatment

### Observational & Experimental Studies

- Observational study: the researcher observes and measures the variables of interest, but does not attempt to influence the responses
- Experimental study: the researcher applies a treatment and then observes the effect of the treatment on the response variable

### cardinality: the number of distinct values in a variable

> The cardinality of a variable = number of unique values of a variable

### Population & Sample

- Population: the entire group of individuals or instances about whom we hope to learn
- Sample: a subset of the population
  - Sampling bias: a sample that is not representative of the population
  - Response Bias is a systematic favouring of certain outcomes that occurs when random individuals do not respond truthfully or are asked misleading questions in a study.
  - Non-Response Bias is a systematic favouring of certain outcomes that occurs when random individuals who choose to participate in a study differ from those who choose not to participate.
  - Haphazard and Random

### Simple Random Sample

### Standard Deviation

  > The standard deviation is a measure of the amount of variation or dispersion of a set of values.

#### Features

A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range. 数据分散，开口比较宽

#### Sample Standard deviation (SD)

```R
# 计算样本标准差
sample_sd <- sd(x)

# 计算总体标准差
population_sd <- sqrt(var(x))
# 或者
population_sd <- sd(x, na.rm = TRUE)
```

### Z Score # needs to be able to calculate this by the z-score table

  > A Z-score is a numerical measurement that describes a value's relationship to the mean of a group of values. Z-score is measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean.

### Mode

```R
# Calculate Mode
Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

data <- c(2, 19, 44, 44, 44, 51, 56, 78, 86, 99, 99)
mode_value <- Mode(data)
```

### Median

```R
data <- c(23, 24, 26, 26, 28, 29, 30, 31, 33, 34)
result <- median(data)
```

#### Weighted Median

> Weighted Median `weighted.median(values, weights)` # values and weights are vectors of the same length

### Mean

#### Arithmetic Mean

```R
x <- c(3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 59, 23)
mean(x)
```

#### Geometric Mean

```R
x <- c(8, 9, 4, 1, 6, 4, 6, 2, 5)
exp(mean(log(x)))  # one method
prod(x)^(1/length(x))  # second method
psych::geometric.mean(x) # third method
```

#### Weighted Mean

```R
x <- c(3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 59, 23)
weights <- c(3.1, 1.3, 2.4, 1.0, 3.5, 3.5, 1.1, 1.3, 1.6, 1.9, 4.1, 2.4, 1.4, 0.2)
weightedMean(x, weights)
```

#### Harmonic Mean

```R
x <- c(8, 9, 4, 1, 6, 4, 6, 2, 5)
1/mean(1/x) # one method
psych::harmonic.mean(x) # second method
```

#### Trimmed Mean 修剪平均值

```R
    data <- c(2, 3, 5, 6, 7, 8, 9, 10, 12, 15)
    # 计算需要剔除的极端值的数量
    trim_amount <- round(length(data) * 0.05)
    # 对数据进行排序
    sorted_data <- sort(data)
    # 剔除最低和最高的5%的数据
    trimmed_data <- sorted_data[(trim_amount + 1):(length(sorted_data) - trim_amount)]
    # 计算修剪均值
    trimmed_mean <- mean(trimmed_data)

    # another method is use Mean function with trim argument can from 0.1 to 0.5
```

### Range

> highest minus the lowest

```R
# 定义一个向量
x <- c(2, 3, 5, 6, 7, 8, 9, 10, 12, 15)
# 计算范围
range_x <- range(x) # 返回最小值和最大值
```

#### Inter-quartile range (IQR)

> 75th percentile minus the 25th percentile

```R
# quantile函数 example
x <- c(2, 3, 5, 6, 7, 8, 9, 10, 12, 15)
quantile(x, probs = c(0.25, 0.75)) # 返回第一个四分位数和第三个四分位数
```

### Median absolute deviation (MAD)

```R
mad(students$score)
# or
1.4826 * median( abs(students$score - median(students$score)) )
```

### Average absolute deviation (from the mean)

```R
lsr::aad(students$score) 
# or

# 定义一个向量
x <- c(2, 3, 5, 6, 7, 8, 9, 10, 12, 15)
# 计算均值
mean_x <- mean(x)
# 计算每个数据点与均值之间的绝对偏差
absolute_deviations <- abs(x - mean_x)
# 计算平均绝对偏差
average_absolute_deviation <- mean(absolute_deviations)
```

### Covariance 协方差

> 衡量两个变量之间的线性关系：协方差的正负号表示了两个变量之间的线性关系的方向，即正协方差表示正相关关系，负协方差表示负相关关系，而接近零的协方差则表示变量之间基本没有线性关系。
> 衡量变量之间的相关性强弱：协方差的绝对值大小表示了两个变量之间的相关性强度，绝对值越大表示相关性越强。

```R
# 定义两个随机变量
x <- c(1, 2, 3, 4, 5)
y <- c(2, 3, 5, 7, 6)

# 计算协方差
covariance_xy <- cov(x, y)

# 输出结果
print(covariance_xy)
```

### Correlation coefficient 相关系数

The covariance is also related to the correlation coefficient, which is a measure of the linear relationship between two variables. The correlation coefficient is calculated by dividing the covariance by the product of the standard deviations of the two variables.

formula: x,y的协方差等于x,y的相关系数乘以x,y的标准差的乘积

```R
# 定义两个随机变量
x <- c(1, 2, 3, 4, 5)
y <- c(2, 3, 5, 7, 6)

# 计算相关系数
correlation_xy <- cor(x, y)

# 输出结果
print(correlation_xy)
```

### Covariance Matrix 协方差矩阵

```R
# 定义一个多维随机变量数据集
data <- matrix(c(1, 2, 3, 4, 5, 2, 3, 5, 7, 6), nrow = 5, byrow = TRUE)

# 计算协方差矩阵
covariance_matrix <- cov(data)

# 输出结果
print(covariance_matrix)
```

### Variation Ratio: proportion of cases different to the mode

```R
variationRatio <- function(x) {
  freq <- table(x)                   #tabulate the frequencies 
  maxfreq <- max(freq)               #record maximum freq
  vr <- 1 - maxfreq / sum(freq)
  vr                                 #return result
}
```

### Find high outliers and low outliers

```R
# 生成一组随机数据
data <- rnorm(100)

# 计算上四分位数（Q1）和下四分位数（Q3）
Q1 <- quantile(data, 0.25)
Q3 <- quantile(data, 0.75)

# 计算四分位距（IQR）
IQR <- Q3 - Q1

# 定义高异常值和低异常值的阈值
high_threshold <- Q3 + 1.5 * IQR
low_threshold <- Q1 - 1.5 * IQR

# 找到高异常值和低异常值
high_outliers <- data[data > high_threshold]
low_outliers <- data[data < low_threshold]
```

### An example function to find outliers distribution

```R
find_outlier_position <- function(min_val, q1, median_val, q3, max_val) {
  # 计算箱型图的 IQR（四分位距）
  iqr <- q3 - q1
  
  # 计算异常值的上限和下限
  lower_bound <- q1 - 1.5 * iqr
  upper_bound <- q3 + 1.5 * iqr
  
  # 判断最小值和最大值是否在异常值的范围内
  is_lower_outlier <- min_val < lower_bound
  is_upper_outlier <- max_val > upper_bound
  
  # 根据异常值的情况返回结果
  if (is_lower_outlier & is_upper_outlier) {
    return("Both Sides")  # 两边都有异常值
  } else if (is_lower_outlier) {
    return("Lower Side")  # 最下面有异常值
  } else if (is_upper_outlier) {
    return("Upper Side")  # 最上面有异常值
  } else {
    return("No Outlier")  # 没有异常值
  }
}
```

## Some Models

### ARIMA Model

> ARIMA (AutoRegressive Integrated Moving Average) is a generalization of an autoregressive moving average (ARMA) model. Both of these models are fitted to time series data either to better understand the data or to predict future points in the series (forecasting).

## Basic R

### Shortcuts

```bash
option + - : <-
ctrl + shift + m : %*% aka |>
```

### Tidyverse - dplyr

#### Rows

- `filter()` - to select rows based on some conditions
  
```R
# < > <= >= == != %in% & | ! condition on columns/variables
flights |> 
    filter(month == 1 & day == 1)
    # or combining | and ==: %in%
    filter(month %in% c(1, 2))
```

- `arrange()` - to reorder rows based on some variable

```R
# It's functionality same as order by in SQL
flights |>
  arrange(year, month, day, desc(dep_time))
```

- `distinct()` - to select unique rows

```R
flights |> 
  distinct(origin, dest)
flights |> 
  distinct(origin, dest, .keep_all = TRUE)
flights |>
  count(origin, dest, sort = TRUE)
```

- `mutate()` - to add new variables

```R
flights |> 
  mutate(speed = distance / air_time * 60)
  # .before = 1, .after = day, .keep = "used"
```

- `select()` - to select columns

```R
flights |> 
  select(year:day, dep_delay, arr_delay) # select columns from year to day
flights |>
    select(starts_with("arr"), ends_with("time")) # select columns with "arr" in the name
flights |>
    select(contains("arr")) # select columns with "arr" in the name
flights |>
    select(where(is.character)) # select columns with character type
flights |>
    select(-contains("arr")) # remove columns
```

- `relocate()` - to move columns

```R
flights |>
    relocate(dep_delay, .after = day)
```

- `rename()` - to rename columns

```R
flights |>
    rename(dep_delay = dep_time)
```

- `group_by() and summarize()` - to group rows

```R
flights |> 
  group_by(month) |> # can be multiple variables
  summarize(
    avg_delay = mean(dep_delay, na.rm = TRUE),
    n = n() # which returns the number of rows in each group
  )
```

- `slice()` - to select rows by their positions

df |> slice_head(n = 1) takes the first row from each group.
df |> slice_tail(n = 1) takes the last row in each group.
df |> slice_min(x, n = 1) takes the row with the smallest value of column x.
df |> slice_max(x, n = 1) takes the row with the largest value of column x.
df |> slice_sample(n = 1) takes one random row.

- `ungroup()` - to remove grouping 取消已分组

```R
flights |> 
  group_by(year, month, day) |> 
  ungroup()


near(x, c(1, 2)) # compare float numbers

```

- `is.na()` - works with any type of vector and returns TRUE for missing values and FALSE for everything else:

```R
flights |> 
  filter(is.na(dep_time))
```

- `if_else()` - a vectorized if() function that is useful when working with data frames:

```R
flights |> 
  mutate(dep_type = if_else(dep_time < 1200, "morning", "afternoon"))
```

- `case_when()` - a vectorized version of ifelse() that is useful when working with data frames:

```R
flights |> 
  mutate(dep_type = case_when(
    dep_time < 600 ~ "early",
    dep_time < 1200 ~ "morning",
    dep_time < 1800 ~ "afternoon",
    TRUE ~ "evening"
  ))
```

## Confidende Interval

I am using `wagon` dataset to calculate the confidence interval.

### Some function

```R
get_mean_se <- function(x, repeats = 1000, size = 10, replace = FALSE){
  # get the standard error of mean sampling
  # x: variable interested
  # repeats: number of sampling iterations
  # size: sample size
  # replace: sampling method
  se <- sd(replicate(repeats, mean(sample(x, size, replace = replace))))
  return(se)
}

get_prop_se <- function(x, c, repeats = 1000, size = 10, replace = FALSE){
  # get the standard error of proportion sampling
  # x: variable interested
  # c: category interested
  # repeats: number of sampling iterations
  # size: sample size
  # replace: sampling method
  se <- sd(replicate(repeats, sum(sample(x, size, replace = replace) == c)/size))
  return(se)
}
```

### An example

```R
# get the mean of price
xbar <- mean(wagon$price)

# using bootstrap to get the standard error
se <- get_mean_se(x = wagon$price, size = length(wagon$price), replace = TRUE)

ci <- c(xbar-2*se, xbar+2*se) # Using vector in R to mimic tuple in Python
sprintf("We are 95%% confident that the true price of this certain type of used sports wagon is between $%.0f and $%.0f.", ci[1], ci[2])
```

### Using Percentile Method to calculate the confidence interval

```R
# bootstrap distribution
boot.wagon <- replicate(1000, mean(sample(wagon$price, 67, replace = TRUE)))


data.frame(boot.wagon)
hist(boot.wagon)
# 95% confidence interval is from 2.5th percentile to 97.5th percentile
quantile(x = boot.wagon, probs = c(0.025, 0.975))
```
