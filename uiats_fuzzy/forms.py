from django import forms


class UIATSForm(forms.Form):
    age = forms.DecimalField(label="Patient age", min_value=0, decimal_places=1)
    lifeExpectancy = forms.DecimalField(label="Life expectancy of patient", min_value=0, decimal_places=1)
    maxDiameter = forms.DecimalField(label="Maximum diameter of aneurysm", min_value=0, decimal_places=2)
    location = forms.ChoiceField(label="Location of aneurysm", choices=[
        (0, "BasA bifurcation"),
        (1, "Vertebral/basilar artery"),
        (2, "AcomA or PcomA")
    ])

    prevSAH = forms.BooleanField(label="Previous subarachnoid hemorrhage from a different aneurysm", required=False)
    prevSAHConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    famSAH = forms.BooleanField(label="Familial intracranial aneurysms or subarachnoid hemorrhage", required=False)
    famSAHConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    jfiEth = forms.BooleanField(label="Japanese, Finnish or Inuit ethnicity", required=False)
    jfiEthConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    smoking = forms.BooleanField(label="Current cigarette smoking", required=False)
    smokingConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    hypertension = forms.BooleanField(label="Hypertension (systolic blood pressure > 140 mm Hg)", required=False)
    hypertensionConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    kidneyDisease = forms.BooleanField(label="Autosomal-polycystic kidney disease", required=False)
    kidneyDiseaseConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    drugAbuse = forms.BooleanField(label="Current drug abuse (cocaine, amphetamine)", required=False)
    drugAbuseConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    alcoholAbuse = forms.BooleanField(label="Current alcohol abuse", required=False)
    alcoholAbuseConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)


    cranialNerveDeficit = forms.BooleanField(label="Cranial nerve deficit", required=False)
    cranialNerveDeficitConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    massEffect = forms.BooleanField(label="Clinical or radiological mass effect", required=False)
    massEffectConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    thromboembolicEvents = forms.BooleanField(label="Thromboembolic events from the aneurysm", required=False)
    thromboembolicEventsConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    epilepsy = forms.BooleanField(label="Epilepsy", required=False)
    epilepsyConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)


    fearOfRupture = forms.BooleanField(label="Reduced quality of life due to fear of rupture", required=False)
    fearOfRuptureConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    multiplicity = forms.BooleanField(label="Aneurysm multiplicity", required=False)
    multiplicityConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)


    neurocognitiveDisorder = forms.BooleanField(label="Neurocognitive disorder", required=False)
    neurocognitiveDisorderConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    coagulopathies = forms.BooleanField(label="Coagulopathies, thrombophilic diseases", required=False)
    coagulopathiesConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    psychiatricDisorder = forms.BooleanField(label="Psychiatric disorder", required=False)
    psychiatricDisorderConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)


    irregularity = forms.BooleanField(label="Irregularity or lobulation", required=False)
    irregularityConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    largeSizeOrAspectRatio = forms.BooleanField(label="Size ratio > 3 or aspect ratio > 1.6", required=False)
    largeSizeOrAspectRatioConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)


    serialImagingGrowth = forms.BooleanField(label="Aneurysm growth on serial imaging", required=False)
    serialImagingGrowthConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    serialImagingFormation = forms.BooleanField(label="Aneurysm de novo formation on serial imaging", required=False)
    serialImagingFormationConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    CSVD = forms.BooleanField(label="Contralateral stenoocclusive vessel disease", required=False)
    CSVDConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)

    
    complexityRelatedRisk = forms.BooleanField(label="High aneurysm complexity related risk", required=False)
    complexityRelatedRiskConf = forms.IntegerField(label="Modifier", min_value=0, max_value=100, initial=100, required=False)
