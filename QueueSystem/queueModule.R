createQueue <- function(size){
  q <- list()
  q <- append(q, size)
  return(q)
}

enqueue <- function(q, element){
  q_len = length(q) - 1
  max_len = as.numeric(q[1])
  #cat("queue len:", q_len, end="\n")
  #cat("queue max len:", as.numeric(max_len), end="\n")
  if (q_len < max_len)
    return(append(q, element))
  else
    cat("Error! Queue is FULL!!!\nReturned: ")
}

peek <- function(q){
  q_len = length(q) - 1
  if( q_len == 0 )
    cat("Error! Queue is Empty.\n")
  else
    return(as.numeric(q[2]))
}

pop <- function(q){
  q_len = length(q) - 1
  if( q_len == 0 )
    cat("Error! Queue is Empty.\n")
  else{
    if( q_len == 1 )
      q_new <- q[2]
    else
      q_new <- append(q[1], q[2:q_len + 1])
  }
  return(q_new)
}

prnt_queue <- function(q){
  q_len = length(q) - 1
  if( q_len == 0)
    cat("Queue is empty, Nothing to print.\n")
  else{
    cat("Queue(Size=",length(q) - 1,"): ", sep="")
    for( i in 2:length(q)){
      cat(as.numeric(q[[i]]),", ", sep ="")
    }
    cat("\n")
  }
}

isEmpty <- function(q){
  q_len = length(q) - 1
  if( q_len == 0 )
    return(TRUE)
  else
    return(FALSE)
}

isFull <- function(q){
  q_len = length(q) - 1
  max_len = as.numeric(q[1])
  if( q_len == max_len )
    return(TRUE)
  else
    return(FALSE)
}

getQueueSize <- function(q){
  return(length(q) - 1)
}

q <- createQueue(3)
q <- enqueue(q, 4)
prnt_queue(q)




