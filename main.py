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

natParks = file_contents["np"]

print(natParks)

print(((natParks['Acadia'])["PreImg"])["img"])

main.add_url_rule('/', view_func = Basic.as_view('home','home','home.html'))
main.add_url_rule('/natPark', view_func = park.as_view('NationalPark','NationalPark','nationalPark.html',natParks))
main.add_url_rule('/swap', view_func = Basic.as_view('Swap','Swap','swap.html'))

if __name__ =='__main__':
    main.run(debug=True)     
