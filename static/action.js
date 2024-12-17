function getFormInput(){
    const inputs = new URLSearchParams(window.location.search)
    return{
        name: inputs.get("name"),
        email: inputs.get("email"),
        like: inputs.get("like")
    }
}

function displayMSG() {
    const {name, email, like} = getFormInput()
    const message = document.getElementById("message")

    if (like === "on"){
        message.innerHTML=`Thank you, ${name} for liking the bug`
    }
    else{
        message.innerHTML=`${name} how could you not like the bug`
    }
}

document.addEventListener("DOMContentLoaded", displayMSG)