#' Creates a queue of maximum size - @size
create_queue <- function(size) {
  q <- list()
  q <- append(q, size)
  return(q)
}

#' Inserts an Element to the back of the queue.
#' new q is returned.
#' If queue is full, a message is printed (same queue is returned)
enqueue <- function(q, element) {
  q_len <- length(q) - 1
  max_len <- as.numeric(q[1])
  # cat("queue len:", q_len, end="\n")
  # cat("queue max len:", as.numeric(max_len), end="\n")
  if (q_len < max_len)
    return(append(q, element))
  else
    cat("Enqueue Error: Queue is FULL -", q_len, "\\", max_len, "\n")
    return(q)
}

#' Return the Element, at the queues FRONT.
#' If Queue is empty, return -1.
peek <- function(q) {
  q_len <- length(q) - 1
  if (q_len == 0) {
    cat("Error! Queue is Empty.\n")
    return(NULL) # do not return -1 (The Queue is an Integer queue)
  }
  else
    return(as.numeric(q[2]))
}

#' Returns A new queue after REMOVING the front element.
#' If the queue is empty, the same queue object is returned.
pop <- function(q) {
  q_len <- length(q) - 1
  if (q_len == 0) {
    q_new <- q
    cat("Pop Error: Queue is Empty.\n")
  }
  else{
    if (q_len == 1)
      q_new <- q[1]
    else # no. of elements > 1
      q_new <- append(q[1], q[2:q_len + 1])
  }
  return(q_new)
}

#' Prints the elements in queue and its size.
prnt_queue <- function(q) {
  q_len <- length(q) - 1
  if (q_len == 0)
    cat("Queue is empty, Nothing to print.\n")
  else{
    cat("Queue(Size=", length(q) - 1, "): ", sep = "")
    for (i in 2:length(q)) {
      cat(as.numeric(q[[i]]), ", ", sep = "")
    }
    cat("\n")
  }
}

#' Returns True if the queue is empty and False otherwise.
is_empty <- function(q) {
  q_len <- length(q) - 1
  if (q_len == 0)
    return(TRUE)
  else
    return(FALSE)
}

#' Returns True if the queue is full and False otherwise.
is_full <- function(q) {
  q_len <- length(q) - 1
  max_len <- as.numeric(q[1])
  if (q_len == max_len)
    return(TRUE)
  else
    return(FALSE)
}

#' Returns the current size of the queue.
get_queue_size <- function(q) {
  return(length(q) - 1)
}