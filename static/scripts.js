const select = document.getElementById('parkType')
var img = document.getElementById("miscParkImg")
var p = document.getElementById("miscParkInfo")
var h2 = document.getElementById("miscParkTitle")
var titles = document.getElementById("swapTitle")

select.addEventListener('change', displayPark)

function spefParkChoice(pic,blurb,title,alt){
    h2.innerHTML=title
    img.setAttribute('src',`static/images/${pic}.jpg`)
    img.setAttribute('alt',alt)
    p.innerHTML=blurb
    titles.innerHTML = title
}

function displayPark (){
    let choice = select.value
    if (choice=="nm"){
        let blurb="The Statue of Liberty is in New York state. It was a gift from the french and sits untop of a old star fort. You can go into the crown and get an intresting view. From the view you also can see the arm. On the way down you can see the access up to the arm but it is mainly closed."
        spefParkChoice("liberty1",blurb,"Statue of Liberty National Monument","Statue of Liberty arm from crown")
    }
    else if(choice=="npres"){
        let blurb="This park offers amazing oppurtunties to see swamp, praries, big cyrpess trees and wildlife. There is an amazing off roading oppurtnties right throught the swamp. On this theres tons of birds and alligators. You can also see the absoluetly massive cypress trees with the areial plants on them. The water is beyond clear and you can easily see many fish."
        spefParkChoice("bigCypress",blurb,'Big Cypress National Preserve',"A red tailed hawk in a tree")
    }
    else if(choice=="nra"){
        let blurb="The Delware Water Gap National Recreation Area is in both New jersey and Pennsylvania. It has numerous waterfalls, most of which are a short walk off the main road. Theres also great hiking oppurnties with wonderful views down into the gap. The main road also has very nice views"
        spefParkChoice("delawareWaterGap",blurb,"Delaware Water Gap National Recreation Area","Dingman falls")
    }
    else{
        spefParkChoice("acadia1","Select one","Select One","Picture of Acadia coast")
    }
}