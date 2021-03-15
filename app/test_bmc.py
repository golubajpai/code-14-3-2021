from django.test import TestCase
import numpy as np
import pandas as pd

class BMCTest(TestCase):
    """ Test module """
    dummy_data=None

    def setUp(self):
        '''Preparing data for 2 lac records '''


        height=(np.random.uniform(150.1, 180.2, 200000))
        weights=(np.random.uniform(50.1,200,200000))
        Gendar=(np.random.choice(["Male","Female"], 200000))
        dataframe=pd.DataFrame({"HeightCm":height,"WeightKg":weights,"Gender":Gendar})
        self.dummy_data=dataframe.to_dict('records')
        
        

    def test_requests(self):
        url=''
        response = self.client.post(url, self.dummy_data,content_type='application/json')
        assert response.status_code==200

