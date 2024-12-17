document.getElementById("darkMode").addEventListener("click",darkmode)

const nav = document.querySelector("nav")
const footer = document.querySelector("footer")
const natParks = document.querySelectorAll(".natPark")
const natParkImg = document.querySelector(".natParkImg")
const navItems = document.querySelectorAll(".navItem")
const navTexts = document.querySelectorAll(".navItem > a")
const foTexts = document.querySelectorAll("#allLinks a")

function darkmode(){
    document.body.style.backgroundColor= "#222222"
    document.body.style.color = "#E#E#E#"

    nav.style.borderColor = "#545E8C"
    footer.style.borderColor = "#545E8C"

    if (natParks) {
        natParks.forEach(natPark => {
            natPark.style.borderColor = "#545E8C"
        })
    }

    document.querySelector(".mainImg").style.borderColor="#E8BEEE"

    if (natParkImg){
        natParkImg.style.borderColor="#E8BEEE"
    }

    navItems.forEach(navItem => {
        navItem.style.backgroundColor="#004592"
    })

    navTexts.forEach(navText => {
        navText.style.color="#BE8BB8"
    })

    foTexts.forEach(foText => {
        foText.style.color="#BE8BB8"
    })
}