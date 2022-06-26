from django.shortcuts import render
from .apps import CalculatorConfig
from .forms import CalculatorForm
import numpy as np

# Create your views here.
def CalculatorView(request):
    CalculatedGSM = 0
    if request.method == "POST":
        forms = CalculatorForm(request.POST)

        if forms.is_valid():
                shade = forms.cleaned_data['shade']
                enzyme = forms.cleaned_data['enzyme']
                # MachineDiameterXGauge = forms.cleaned_data['MachineDiameterXGauge']
                RequiredWidth  = forms.cleaned_data['RequiredWidth']
                StitchLength_mm = forms.cleaned_data['StitchLength_mm']
                AfterSlitingWidth = forms.cleaned_data['AfterSlitingWidth']
                Overfeed = forms.cleaned_data['Overfeed']
                SetWidh_Stenter_Machine = forms.cleaned_data['SetWidh_Stenter_Machine']
                GSMAfterStentering = forms.cleaned_data['GSMAfterStentering']
                LengthWiseShrinkage = forms.cleaned_data['LengthWiseShrinkage']
                LengthWiseShrinkage_1 = forms.cleaned_data['LengthWiseShrinkage_1']
                WidthWiseShrinkage = forms.cleaned_data['WidthWiseShrinkage']
                AngleOfSpirality_degree = forms.cleaned_data['AngleOfSpirality_degree']
                FinalWidh_Compacting_Machine = forms.cleaned_data['FinalWidh_Compacting_Machine']
                WidthWiseShrinkage_1= forms.cleaned_data['WidthWiseShrinkage']
                # AngleOfSpirality_degree= forms.cleaned_data['AngleOfSpirality_degree']
                AngleOfSpiralityDegree_1 = forms.cleaned_data['AngleOfSpiralityDegree_1']
                ThreadCount = forms.cleaned_data['ThreadCount']
                # MachineDiameterXGauge= CalculatorConfig.encoder_model.transform([MachineDiameterXGauge])
                input_list = [shade,enzyme,0,RequiredWidth,StitchLength_mm,AfterSlitingWidth,Overfeed,SetWidh_Stenter_Machine,GSMAfterStentering,LengthWiseShrinkage,WidthWiseShrinkage,AngleOfSpirality_degree,FinalWidh_Compacting_Machine,LengthWiseShrinkage_1,WidthWiseShrinkage_1,AngleOfSpiralityDegree_1,ThreadCount]
                input_array = np.array(input_list)
                input_array = input_array.reshape(1, -1)
                print(input_list)
                CalculatedGSM = CalculatorConfig.loaded_model.predict(input_array)
                CalculatedGSM = CalculatedGSM[0]

                

    else:
            forms = CalculatorForm()
        

    return render(request,'calculator.html',{'form':forms,'CalculatedGSM':CalculatedGSM})

