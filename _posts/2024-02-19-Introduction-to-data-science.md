---
layout: post
subtitle: Introduction to Data Science
categories: [R]
header:
    image: header.jpg
    align:
    text: light
---

# Introduce data science

## Basic Concepts

### Cases and Variables

* Cases aka rows, observations, records, units, instances
  
* Variables aka columns, fields, attributes, features, measurements, properties, parameters
* Variables can be classified as:
  * Categorical (qualitative) variables (aka factors, discrete)
    * Nominal variables (no order) 
    * Ordinal variables (order)
    * Cyclic variables (circular order, e.g. days of the week, months of the year, etc.
  * Quantitative (numerical) variables
    * continuous variables
    * discrete variables
  
* cardinality: the number of distinct values in a variable
  * Cardinality of a variable = number of unique values of a variable
  
* Variable roles
  * Explanatory aka x, predictor, independent, input variable
  * Response aka y, target, dependent, outcome, output variable
  * Identifiers aka key, index, unique identifier, unique key, unique index, row name, ID
  
* Confounding - a third variable that affects the relationship between the explanatory and response variables
  * aka lurking, hidden, nuisance, spurious variable
  
* Assocation & Causation
  * Association: a statistical relationship between two variables
  * Causation: a cause-and-effect relationship between two variables
  
* Randomised experiment
  * Control group is that which receives no treatment
  * Treatment group is that which receives the treatment
  * give a placebo is that which receives a fake treatment
  
* Observational & Experimental Studies
  * Observational study: the researcher observes and measures the variables of interest, but does not attempt to influence the responses
  * Experimental study: the researcher applies a treatment and then observes the effect of the treatment on the response variable
  
* Population & Sample
  * Population: the entire group of individuals or instances about whom we hope to learn
  * Sample: a subset of the population
    * Sampling bias: a sample that is not representative of the population
    * Response Bias is a systematic favouring of certain outcomes that occurs when random individuals do not respond truthfully or are asked misleading questions in a study.
    * Non-Response Bias is a systematic favouring of certain outcomes that occurs when random individuals who choose to participate in a study differ from those who choose not to participate.
    * How to avoid sampling bias?
      * Random sampling
      * Stratified sampling
      * Cluster sampling
      * Systematic sampling
      * Multistage sampling
      * Convenience sampling
      * Voluntary response sampling
      * Quota sampling
      * Snowball sampling
      * Purposive sampling
      * Judgmental sampling
      * Convenience sampling
      * Self-selection sampling
      * Non-probability sampling
      * Probability sampling
      * Simple random sampling
      * Systematic random sampling
      * Stratified random sampling
      * Cluster random sampling
      * Multistage random sampling
    * Haphazard and Random

* Simple Random Sample
  
## Basic R
