from IPython.display import display
import ipywidgets as widgets



class Test:

	def __init__(self):
		pass
	
	def on_button_clicked(self,b):
			print(self.text.value)
				
	def get_list(self):
		# for i in range(10):	
		out = widgets.Output(layout={'border': '1px solid black'})
		with out:
			for i in range(10):
				# print(i, 'Hello world!')
				print("> Usecase name{} (Usecase {})\n".format(i,i))
				
		cb = widgets.Checkbox(
			value=False,
			description='Check me',
			disabled=False,
			indent=False
		)
		self.text = widgets.Text(
			placeholder='Enter Usecase ID',
			continuous_update = False
		)
		button = widgets.Button(description="Click Me!")
		output = widgets.Output()
		display(out, output)
		display(self.text, output)
		display(button, output)
		display(cb, output)
		button.on_click(self.on_button_clicked)
		
	def submit_files(self):
		import os
		output = widgets.Output()
		cb_list = []
		for i in os.listdir():
				cb = widgets.Checkbox(
					value=False,
					description=i,
					disabled=False,
					indent=False
				)
				cb_list.append(cb)
				display(cb,output)
			submit
		submit_command_txt = self.text = widgets.Text(
			placeholder='Enter Model Execution Command',
			continuous_update = False
		)
		button.on_click(self.on_button_clicked)
				
	def on_file_submission(self,b):
		
		
		
