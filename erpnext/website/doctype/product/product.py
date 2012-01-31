class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl
		
	def validate(self):
		"""make page for this product"""
		import website.utils
		
		p = website.utils.add_page("Product " + self.doc.title)
		
		from jinja2 import Template
		import markdown2
		import os
		
		self.doc.long_description_html = markdown2.markdown(self.doc.long_description or '')
		
		with open(os.path.join(os.path.dirname(__file__), 'template.html'), 'r') as f:
			p.content = Template(f.read()).render(doc=self.doc)
		
		with open(os.path.join(os.path.dirname(__file__), 'product_page.js'), 'r') as f:
			p.script = Template(f.read()).render(doc=self.doc)
		
		p.save()
		
		website.utils.add_guest_access_to_page(p.name)
		self.doc.page_name = p.name
		del self.doc.fields['long_description_html']