---
layout: post
subtitle: R Languages Notes
categories: [R]
header:
    image: header.jpg
    align:
    text: light
---

# R basic

## Functions

```R
library(summarytools)
Arrests %>% 
  dfSummary(col.widths = c(10,80,150,120,120,180,220)) %>% 
  view(method = "render")

is.na()
sum()

```
