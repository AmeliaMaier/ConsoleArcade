trim <- function (x){ gsub("^\\s+|\\s+$", "", x)}

print.main.menu <- function(main.menu, menu.options){
  count <- 1
  print(" ----------- Console Arcade ----------- ")
  for(option in main.menu){
    cat(menu.options[count], ": ", main.menu[count], "\n")
    count = count + 1
  }
}

hangman.rungame <- function(){
  
}

guess.my.number.checkguess <- function(ran.num, past.diff, turn, user.num){
  current.diff <- abs(ran.num - user.num)
  if (current.diff == 0){
    print('That is correct. You must be psychic.')
    return(0)
  }
  if (turn == 1){
    if (current.diff <= 10){
      print('So close. You are hot.')
    } else{
      print('Try again; you are cold.')
    }
    return(current.diff)
  }
  if (past.diff >= current.diff){
    print('Getting warmer')
  }else if (past.diff == current.diff){
    print('No change')
  }else{
    print("You are getting colder")
  }
  return(current.diff)
}

guess.my.number.rungame <- function(){
  ran.num <- sample(1:100, 1)
  past.diff <- 0
  turn <- 1
  repeat{
    user.input <- ''
    while(!grepl("^[0-9]+$",user.input) || user.input =="Q"){
      user.input <- trim(readline('Guess my number or enter Q to quit: '))
    }
    if (user.input == "Q"){
      break
    }
    past.diff <- guess.my.number.checkguess(ran.num, past.diff, turn, as.integer(user.input))
    if(past.diff == 0){
      break
    }
    turn = turn + 1
  }
}

yohaku.rungame <- function(){
  
}

main <- function(){
  main.menu <- c('Hangman', 'Guess My Number', 'Yohaku','Quit')
  menu.options <- c('1', '2', '3', 'Q')
  repeat{
    user_input <- ''
    print.main.menu(main.menu, menu.options)
    while (trim(user_input) %in% menu.options == FALSE){
      user_input <- readline('Enter the numer for the game you would like to play. ')
    }
    if (trim(user_input) == 'Q'){
      break
    }
    if (trim(user_input) == '1'){
      hangman.rungame()
    } else if (trim(user_input) == '2'){
      guess.my.number.rungame()
    }else if (trim(user_input) == '3'){
      yohaku.rungame()
    }
  }
}

main()
