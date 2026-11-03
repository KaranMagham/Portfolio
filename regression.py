install.packages(c("ggplot2", "lmtest", "car", "MASS", "glmnet"))  //to install all required packages at once in r terminal


## Practical 1: Fundamentals of R Programming and Data Handling

Aim: To practice basic R commands, create common data structures and apply basic statistical functions.

Code:

```
x <- c(12, 15, 18, 20, 25)

mat <- matrix(1:9, nrow=3, ncol=3)

students <- data.frame(
  id=c(1,2,3),
  marks=c(78,85,69)
)

mean(x)
sum(x)
min(x)
max(x)
range(x)
var(x)
summary(x)
str(students)
```



## Practical 2: Data Import, Pre-processing and Manipulation using R

Aim: To import, inspect, clean and manipulate a dataset in R.

Code:

```
emp <- data.frame(
  EmpID = 1:6,
  Name = c("Aarav","Diya","Kabir","Meera","Diya","Rohan"),
  Age = c(28,34,NA,45,34,30),
  Department = c("IT","HR","Finance","IT","HR",NA),
  Salary = c(55000,62000,48000,NA,62000,51000)
)

write.csv(emp, "employee_data.csv", row.names=FALSE)

emp_data <- read.csv("employee_data.csv")

class(emp_data)
str(emp_data)
summary(emp_data)

emp$Age[is.na(emp$Age)] <- 0
emp$Department[is.na(emp$Department)] <- "Unknown"
emp$Salary[is.na(emp$Salary)] <- 0

emp$Age <- as.numeric(emp$Age)
emp$Department <- as.factor(emp$Department)

emp$Bonus <- emp$Salary * 0.10

names(emp)[names(emp) == "Name"] <- "EmployeeName"

emp$EmpID <- NULL

emp <- emp[!duplicated(emp), ]

emp
```



## Practical 3: Data Visualization and Exploratory Data Analysis using R

Aim: To visualize data and perform exploratory analysis before fitting a regression model.

Code:

```
install.packages("ggplot2")
library(ggplot2)

data(mtcars)
head(mtcars)

# Histogram
p <- ggplot(mtcars, aes(x=mpg)) +
  geom_histogram(bins=10, fill="skyblue",
                 color="black") +
  labs(title="Histogram of MPG",
       x="Miles Per Gallon",
       y="Frequency") +
  theme_minimal()

print(p)

# Boxplot
b <- ggplot(mtcars, aes(x=factor(cyl), y=mpg)) +
  geom_boxplot(fill="lightgreen") +
  labs(title="MPG by Cylinders") +
  theme_minimal()

print(b)

# Bar Chart
bar <- ggplot(mtcars, aes(x=factor(cyl))) +
  geom_bar(fill="orange") +
  labs(title="Cars by Cylinders") +
  theme_minimal()

print(bar)

# Pie Chart
data <- data.frame(
  category=c("A","B","C","D"),
  value=c(25,40,30,20)
)

pie <- ggplot(data, aes(x="", y=value, fill=category)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y") +
  theme_void()

print(pie)

# Scatter Plot
s <- ggplot(mtcars, aes(x=wt, y=mpg)) +
  geom_point(color="red", size=3) +
  labs(title="Weight vs MPG") +
  theme_minimal()

print(s)
```



## Practical 4: Simple Linear Regression using R

Aim: To fit a simple linear regression model, interpret its coefficients and predict response values.

Code:

```
data(mtcars)

head(mtcars)

model <- lm(mpg ~ hp, data=mtcars)

summary(model)

coef(model)

intercept <- coef(model)[1]
slope <- coef(model)[2]

cat("Regression Equation:\n")
cat("mpg =", intercept, "+", slope, "* hp\n")

# Plot
plot(mtcars$hp, mtcars$mpg,
     main="MPG vs Horsepower",
     xlab="Horsepower",
     ylab="Miles Per Gallon",
     pch=19)

abline(model)

# Prediction
new_car <- data.frame(hp=150)
predict(model, newdata=new_car)

# Multiple Predictions
new_cars <- data.frame(hp=c(100,150,200,250))

predicted_mpg <- predict(model, newdata=new_cars)

result <- data.frame(
  Horsepower=new_cars$hp,
  Predicted_MPG=predicted_mpg
)

print(result)
```





## Practical 5: Evaluation and Statistical Testing of Simple Linear Regression

Aim: To evaluate a simple regression model and perform statistical tests and confidence interval estimation.

Code:

```
data(mtcars)

model <- lm(mpg ~ hp, data=mtcars)

summary(model)

# R-squared
summary(model)$r.squared

# Adjusted R-squared
summary(model)$adj.r.squared

# T-test
summary(model)$coefficients

# F-test
summary(model)$fstatistic

# 95% Confidence Interval
confint(model)

# 99% Confidence Interval
confint(model, level=0.99)
```





## Practical 6: Multiple Linear Regression and Variable Selection using R

Aim: To fit a multiple linear regression model, interpret coefficients and explore variable-selection strategies.

Code:

```
data(mtcars)

# Model 1
model1 <- lm(mpg ~ wt, data=mtcars)

# Model 2
model2 <- lm(mpg ~ wt + hp, data=mtcars)

# Model 3
model3 <- lm(mpg ~ wt + hp + cyl, data=mtcars)

# Display Results
summary(model1)
summary(model2)
summary(model3)

# Compare R-squared
summary(model1)$r.squared
summary(model1)$adj.r.squared

summary(model2)$r.squared
summary(model2)$adj.r.squared

summary(model3)$r.squared
summary(model3)$adj.r.squared

# Compare Models
anova(model1, model2)
anova(model2, model3)

# Full Model
full_model <- lm(
  mpg ~ wt + hp + disp + cyl + drat +
    qsec + vs + am + gear + carb,
  data=mtcars
)

# Variable Selection
selected_model <- step(full_model, direction="both")

summary(selected_model)

# Diagnostics
par(mfrow=c(2,2))
plot(selected_model)
```





## Practical 7: Regression Model Validation and Residual Diagnostics

Aim: To calculate residual measures and use diagnostic plots to assess regression assumptions.

Code:

```
data(mtcars)

model1 <- lm(mpg ~ wt, data=mtcars)

# Residuals
residuals(model1)

# Standardized Residuals
rstandard(model1)

# Studentized Residuals
rstudent(model1)

# Diagnostic Plots
par(mfrow=c(2,2))

plot(model1, which=1)

par(mfrow=c(1,1))

par(mar=c(4,4,2,2))

plot(model1, which=2)

plot(model1, which=3)

plot(model1, which=5)

par(mfrow=c(1,1))
```





## Practical 8: Detection and Treatment of Regression Assumption Violations

Aim: To test for autocorrelation and heteroscedasticity and consider suitable remedial measures.

Code:

```
install.packages("lmtest")
library(lmtest)

data(mtcars)

model <- lm(mpg ~ wt + hp, data=mtcars)

# Durbin-Watson Test
dwtest(model)

# Breusch-Pagan Test
bptest(model)

# Residual Plot
plot(fitted(model), residuals(model),
     xlab="Fitted Values",
     ylab="Residuals")

abline(h=0, lty=2)
```





## Practical 9: Advanced Regression Techniques using R

Aim: To fit polynomial regression and weighted least squares models and compare model fit.

Code:

```
data(cars)

# Linear Regression
linear_model <- lm(dist ~ speed, data=cars)

# Polynomial Regression
poly_model <- lm(
  dist ~ speed + I(speed^2),
  data=cars
)

# Model Summary
summary(linear_model)
summary(poly_model)

# Compare Models
anova(linear_model, poly_model)

# Diagnostic Plot
plot(poly_model)

# Weighted Least Squares
wls_model <- lm(
  dist ~ speed,
  data=cars,
  weights=1/speed^2
)

summary(wls_model)
```





## Practical 10: Multicollinearity, Ridge Regression and Regression Case Study

Aim: To identify multicollinearity, fit ridge regression and apply a complete regression workflow to a real-world dataset.

Code:

```
install.packages(c("car", "MASS", "glmnet"))

library(car)
library(MASS)
library(glmnet)

data(mtcars)

# PART A: MULTICOLLINEARITY

ols <- lm(
  mpg ~ wt + hp + disp + qsec,
  data=mtcars
)

# Correlation Matrix
cor(mtcars[, c("wt","hp","disp","qsec")])

# VIF
vif(ols)


# PART B: RIDGE REGRESSION

x <- model.matrix(
  mpg ~ wt + hp + disp + qsec,
  data=mtcars
)[, -1]

y <- mtcars$mpg

set.seed(123)

cv_ridge <- cv.glmnet(x, y, alpha=0)

# Best Parameter
cv_ridge$lambda.min

# Ridge Coefficients
coef(cv_ridge, s="lambda.min")

# Predictions
predict(
  cv_ridge,
  newx=x[1:5, , drop=FALSE],
  s="lambda.min"
)


# PART C: REGRESSION CASE STUDY

set.seed(123)

train_rows <- sample(
  seq_len(nrow(mtcars)),
  size=floor(0.8 * nrow(mtcars))
)

train_data <- mtcars[train_rows, ]
test_data <- mtcars[-train_rows, ]

# Train Model
case_model <- lm(
  mpg ~ wt + hp + disp + qsec,
  data=train_data
)

summary(case_model)

# Prediction
actual_mpg <- test_data$mpg

predicted_mpg <- predict(
  case_model,
  newdata=test_data
)

# RMSE
rmse <- sqrt(mean(
  (actual_mpg - predicted_mpg)^2
))

# R-squared
r_squared <- 1 -
  sum((actual_mpg - predicted_mpg)^2) /
  sum((actual_mpg - mean(actual_mpg))^2)

cat("Test RMSE:", rmse, "\n")
cat("Test R-squared:", r_squared, "\n")

# Actual vs Predicted
results <- data.frame(
  Actual_MPG=actual_mpg,
  Predicted_MPG=as.numeric(predicted_mpg)
)

print(results)
```

Quick exam note: Practicals 3, 8 and 10 require packages. Install them once before running:

```
install.packages(c("ggplot2", "lmtest", "car", "MASS", "glmnet"))
```

Your PDF has 10 Regression Analysis practicals, and all 10 are covered above.&#x20;

Regression Analysis Using R Programming Complete Practical.pdf
