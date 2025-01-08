# Basic R Program to Demonstrate Basic Features

# 1. Variables and Data Types
num <- 10            # Numeric
char <- "Hello"      # Character
bool <- TRUE         # Logical (Boolean)
pi_value <- pi       # Constant

# Printing variables
cat("Numeric value: ", num, "\n")
cat("Character value: ", char, "\n")
cat("Boolean value: ", bool, "\n")
cat("Pi value: ", pi_value, "\n")

# 2. Functions
# Function to add two numbers
add_numbers <- function(a, b) {
  result <- a + b
  return(result)
}

# Function call
sum_result <- add_numbers(5, 7)
cat("Sum of 5 and 7 is: ", sum_result, "\n")

# Function to calculate the factorial of a number
factorial_calc <- function(n) {
  if (n == 0) {
    return(1)
  } else {
    return(n * factorial_calc(n - 1))
  }
}

# Function call
fact_result <- factorial_calc(5)
cat("Factorial of 5 is: ", fact_result, "\n")

# 3. Control Structures (if-else)
x <- 20
if (x > 10) {
  cat("x is greater than 10\n")
} else {
  cat("x is less than or equal to 10\n")
}

# 4. Loops (for loop, while loop)
# For loop to print numbers 1 to 5
cat("For loop output:\n")
for (i in 1:5) {
  cat(i, "\n")
}

# While loop to print numbers 6 to 10
cat("While loop output:\n")
i <- 6
while (i <= 10) {
  cat(i, "\n")
  i <- i + 1
}

# 5. Data Structures
# Vector: A one-dimensional array
numbers <- c(1, 2, 3, 4, 5)
cat("Vector:", numbers, "\n")

# List: A collection of different data types
my_list <- list(name = "Alice", age = 25, height = 5.5, is_student = TRUE)
cat("List:", my_list, "\n")

# Matrix: A two-dimensional array
matrix_data <- matrix(1:9, nrow = 3, ncol = 3)
cat("Matrix:\n")
print(matrix_data)

# Data Frame: A table-like structure
data_frame <- data.frame(
  Name = c("John", "Jane", "Tom"),
  Age = c(23, 25, 22),
  Grade = c("A", "B", "A")
)
cat("Data Frame:\n")
print(data_frame)

# 6. Basic Plotting
# Scatter plot of two vectors
x_vals <- c(1, 2, 3, 4, 5)
y_vals <- c(2, 4, 6, 8, 10)

plot(x_vals, y_vals, main = "Scatter plot of X vs Y", xlab = "X", ylab = "Y", col = "blue", pch = 16)

# 7. String Manipulation
# Concatenating strings
greeting <- paste("Hello", "World", sep = " ")
cat("Concatenated string: ", greeting, "\n")

# String length
str_length <- nchar(greeting)
cat("Length of string: ", str_length, "\n")

# Substring extraction
substring_result <- substr(greeting, 1, 5)
cat("Substring (first 5 characters): ", substring_result, "\n")

# 8. Reading and Writing Data (CSV example)
# Writing a data frame to a CSV file
write.csv(data_frame, "data.csv", row.names = FALSE)

# Reading the data back from the CSV file
read_data <- read.csv("data.csv")
cat("Read data from CSV file:\n")
print(read_data)

# 9. Handling NA (Missing Values)
# Creating a vector with NA values
na_vector <- c(1, 2, NA, 4, 5)
cat("Vector with NA values: ", na_vector, "\n")

# Removing NA values from the vector
cleaned_vector <- na.omit(na_vector)
cat("Vector after removing NA: ", cleaned_vector, "\n")

# 10. Apply functions (apply, lapply, sapply)
# Using apply to find row sums of a matrix
row_sums <- apply(matrix_data, 1, sum)
cat("Row sums of the matrix:", row_sums, "\n")

# Using lapply to find the length of each element in the list
list_lengths <- lapply(my_list, length)
cat("Length of each list element:", list_lengths, "\n")

# Using sapply to find the length of each element in the list (simplified output)
list_lengths_simplified <- sapply(my_list, length)
cat("Length of each list element (simplified):", list_lengths_simplified, "\n")

# 11. Date and Time Operations
# Get the current date and time
current_time <- Sys.time()
cat("Current Date and Time: ", current_time, "\n")

# Formatting date
formatted_date <- format(current_time, "%Y-%m-%d %H:%M:%S")
cat("Formatted Date and Time: ", formatted_date, "\n")

# 12. Error Handling (tryCatch)
safe_division <- function(x, y) {
  result <- tryCatch({
    x / y
  }, warning = function(w) {
    cat("Warning: Division by zero\n")
    return(NA)
  }, error = function(e) {
    cat("Error: ", e$message, "\n")
    return(NA)
  })
  return(result)
}

# Testing error handling
cat("Result of safe division (10 / 2): ", safe_division(10, 2), "\n")
cat("Result of safe division (10 / 0): ", safe_division(10, 0), "\n")

# 13. Factor Variable Example
# Creating a factor
status <- factor(c("Yes", "No", "Yes", "Yes", "No"))
cat("Factor variable:\n")
print(status)
cat("Levels of the factor: ", levels(status), "\n")
cat("Count of each level:\n")
print(table(status))

