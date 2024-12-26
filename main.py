from flask import Flask, render_template
from flask.views import View

main=Flask(__name__)

class Basic(View):
    def __init__(self,name,template_name):
        self.name=name
        self.template_name = template_name
        self.nav_items=[
            {'name':'Home','url':'/'},
            {'name':'Teams','url':'/team'},
            {'name':'Sign Up','url':'/signup'},
            {'name':'About Us','url':'/aboutus'},
            {'name':'e-Mitre','url':'/emitre'}
        ]
    
    def dispatch_request(self):
        return render_template(
            self.template_name,
            nav_items=self.nav_items,
            name=self.name
        )

main.add_url_rule('/','home')

 
#main.add_url_rule(temp['route'], view_func = Basic.as_view(temp['name'],temp['name'], temp['tempName']))


if __name__ =='__main__':
    main.run(debug=True)     
