from rest_framework import serializers



class BMC_sera(serializers.Serializer):
	Gender=serializers.CharField(max_length=10)
	HeightCm=serializers.FloatField()
	WeightKg=serializers.FloatField()