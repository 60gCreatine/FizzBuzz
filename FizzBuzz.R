# FizzBuzz in R
# %% checks for the remainder, and == 0 confirms there is no remainder, meaning the number is divisible.
for (i in 1:100) {
  Sys.sleep(0.3)
  if (i %% 3 == 0 & i %% 5 == 0){
    cat("FizzBuzz\n")
  } else if (i %% 3 == 0) {
    cat("Fizz\n")
  } else if (i %% 5 == 0) {
     cat("Buzz\n")
  } else {
    cat(paste0(i,"\n"))
  }
}
