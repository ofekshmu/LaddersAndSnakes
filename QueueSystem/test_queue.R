
source("QueueModule.R") # Make sure to change directory accordingly 
library(testthat)

test_that("first_tests", {
  q <- create_queue(4)
  prnt_queue(q)
  expect_equal(get_queue_size(q), 0)
  q <- enqueue(q, 2)
  prnt_queue(q)
  expect_equal(get_queue_size(q), 1)
  expect_equal(peek(q), 2)
  q <- pop(q)
  cat("Error! Queue is Empty. == ")
  expect_equal(get_queue_size(q), 0)
  expect_equal(peek(q), NULL)
  
})
