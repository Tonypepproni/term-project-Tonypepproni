from flask import Flask, render_template
from flask.views import View
import json

main=Flask(__name__)

class Basic(View):
    def __init__(self,name,template_name):
        self.name=name
        self.template_name = template_name
        self.nav_items=[
            {'name':'Home','url':'/'},
            {'name':'National Parks','url':'/natPark'},
            {'name':'Monuments','url':'/natMonument'},
            {'name':'Historical Parks','url':'/history'},
            {'name':'Water & Trails','url':'/Wat&Tra'},
            {'name':'Recration & Preserve','url':'/Rec&Pre'},
            {'name':'Miscelleous','url':'/misc'},
        ]
    
    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name
        )
    
class park(Basic):
    def __init__(self, name, template_name, park):
        super().__init__(name, template_name)
        self.park = park

    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name,
            parks=self.park            
        )

with open("static/info/parks.json") as parkInfo:
    file_contents= json.load(parkInfo)

with open("static/info/pages.json") as templates:
    temps = json.load(templates)

natParks = file_contents["np"]
natParkKeys=list(natParks.keys())
natParkCount=0

for i in temps:
    temp = temps[i] 

    if temp['type'] == "Basic":
        main.add_url_rule(temp['route'], view_func=Basic.as_view(temp['name'], temp['name'], temp["tempName"]))
    elif temp['type'] == "park":
        singlePark=natParks[(natParkKeys[natParkCount])]
        natParkCount+=1
        main.add_url_rule(temp['route'], view_func=park.as_view(temp['name'], temp['name'], temp["tempName"],singlePark))
    elif temp['type'] == 'genPark':
        main.add_url_rule(temp['route'], view_func=park.as_view(temp['name'], temp['name'], temp['tempName'], natParks))


if __name__ =='__main__':
    main.run(debug=True)     
