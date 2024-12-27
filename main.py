from flask import Flask, render_template
from flask.views import View

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

main.add_url_rule('/', view_func = Basic.as_view('home','home','home.html'))
main.add_url_rule('/nationalPark', view_func = Basic.as_view('NationalPark','NationalPark','nationalPark.html'))
main.add_url_rule('/swap', view_func = Basic.as_view('Swap','Swap','swap.html'))

if __name__ =='__main__':
    main.run(debug=True)     
