from django.forms import ModelForm, fields
from django import forms

class CalculatorForm(forms.Form):
    shade = forms.FloatField(label="Shade %")
    enzyme = forms.FloatField(label="Enzyme %")
    # MachineDiameterXGauge = forms.CharField(label='Machine Diameter XGauge' , max_length=150)
    RequiredWidth  = forms.FloatField(label='Required Width')
    StitchLength_mm = forms.FloatField(label='Stitch Length (mm)')
    AfterSlitingWidth = forms.FloatField(label='After Sliting Width (cm)')
    Overfeed = forms.FloatField(label='Overfeed %')
    SetWidh_Stenter_Machine = forms.FloatField(label='Set Width (cm) (Stenter_Machine)')
    GSMAfterStentering = forms.FloatField(label='GSM After Stentering')
    LengthWiseShrinkage = forms.FloatField(label='Length Wise Shrinkage %')
    LengthWiseShrinkage_1 = forms.FloatField(label='Length Wise Shrinkage %(After Compacting)')
    WidthWiseShrinkage = forms.FloatField(label='Width Wise Shrinkage %')
    AngleOfSpirality_degree = forms.FloatField(label='Angle Of Spirality(Degree)')
    FinalWidh_Compacting_Machine = forms.FloatField(label='FinalWidth Compacting Machine (cm)')
    WidthWiseShrinkage_1= forms.FloatField(label='Width Wise Shrinkage % (After Compacting)')
    AngleOfSpiralityDegree_1 = forms.FloatField(label='Angle Of Spirality(Degree) (After Compacting)')
    ThreadCount = forms.FloatField(label='Thread Count')
    
    class Meta:
        labels = {
            'shade' : "Shade %",
            'enzyme' :"Enzyme %",
            'MachineDiameterXGauge' : 'Machine Diameter XGauge',
            'RequiredWidth': 'Required Width',
            'StitchLength_mm': 'Stitch Length (mm)',
            'Overfeed': 'Overfeed %',
            'SetWidh_Stenter_Machine': 'Set Widh (Stenter_Machine)',
            'GSMAfterStentering': 'GSM After Stentering',
            'LengthWiseShrinkage': 'Length Wise Shrinkage %',
            'LengthWiseShrinkage_1': 'Length Wise Shrinkage %(After Compacting)',
            'WidthWiseShrinkage': 'Width Wise Shrinkage %',
            'WidthWiseShrinkage_1': 'Width Wise Shrinkage % (After Compacting)',
            'AngleOfSpirality_degree': 'Angle Of Spirality(Degree)',
            'AngleOfSpiralityDegree_1': 'Angle Of Spirality(Degree) (After Compacting)',
            'ThreadCount':'Thread Count'

        }
