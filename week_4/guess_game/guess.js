const randomNumber=Math.floor(Math.random()*100) +1

let attempt = 0

function checkGuess(){
    const guess= parseInt(document.getElementById("guessField").value)
    attempt++

    if(isNaN(guess) || guess < 1 || guess > 100){
        setMessage("Please enter a valid number")
        return
    }
//triple equal sign is for comparison
    if(guess ===  randomNumber){
        setMessage("You Win")
    }else if(guess < randomNumber){
        setMessage("WRONG, go higher")
    }else if(guess > randomNumber){
        setMessage("WRONG,go lower")   
    }

    function setMessage(message){
        document.getElementById("message").textContent = message
    }

}