import numpy as np
import pandas as pd
import os 




class BMI_calculation:
	def __init__(self,input_data):
		self.input_data=input_data
		self.cal_dict={'weight':['Underweight','Normal weight','Overweight'
		,'Moderately obese','Severely obese','Veryseverely obese'],
		'BMI_Range':[[0,18.4],[18.5,24.9],[25,29.9],[30,34.9],[35,39.9],[40,1000]],
		'Health_risk':['Malnutrition risk','Low risk','Enhanced risk','Medium risk',
		'High risk','Very high risk']}

	

	def bmi_formula(self):

		data=pd.DataFrame(self.input_data)

		data=np.array([data['Gender'].astype(str),data['HeightCm'].astype(float)/100,data['WeightKg'].astype(float)])
		data=np.append(data,[data[2]/data[1]],axis=0)
		cal=np.append(data,np.zeros((2,data.shape[1])),axis=0)



		for x,y,z in zip(self.cal_dict['weight'],self.cal_dict['BMI_Range'] ,self.cal_dict['Health_risk']):

			cal[4][np.logical_and(cal[3]>=y[0],cal[3]<=y[1])]=x
			cal[5][np.logical_and(cal[3]>=y[0], cal[3]<=y[1])]=z
		return cal
		

	def compute_and_csv(self):
		data=self.bmi_formula()
		dict={'Gender':data[0],'Height':data[1],'Weight':data[2],'Bmi':data[3],
		'Bmi categories':data[4],'Health risk':data[5]}
		try:
			pd.DataFrame(dict).to_csv('media/data.csv')

		except FileNotFoundError:
			os.makedirs('media')
			pd.DataFrame(dict).to_csv('media/data.csv')

			
		return data