from django.shortcuts import render
from django.http import HttpResponse

from .forms import UIATSForm
from .UIATS_fuzzy import UIATS


def uiats_form(request):
    valid_submission = False
    conclusion = ""
    repairScore = 0
    conservativeManagementScore = 0
    if request.method == "POST":
        form = UIATSForm(request.POST)
        
        if form.is_valid():

            age = float(form.cleaned_data['age'])
            lifeExpectancy = float(form.cleaned_data['lifeExpectancy']) 
            maxDiameter = float(form.cleaned_data['maxDiameter'])

            location = int(form.cleaned_data['location'])

            prevSAH = float(form.cleaned_data['prevSAHConf']) / 100 if form.cleaned_data['prevSAH'] else 0.0
            famSAH = float(form.cleaned_data['famSAHConf']) / 100 if form.cleaned_data['famSAH'] else 0.0
            jfiEth = float(form.cleaned_data['jfiEthConf']) / 100 if form.cleaned_data['jfiEth'] else 0.0
            smoking = float(form.cleaned_data['smokingConf']) / 100 if form.cleaned_data['smoking'] else 0.0
            hypertension = float(form.cleaned_data['hypertensionConf']) / 100 if form.cleaned_data['hypertension'] else 0.0
            kidneyDisease = float(form.cleaned_data['kidneyDiseaseConf']) / 100 if form.cleaned_data['kidneyDisease'] else 0.0
            drugAbuse = float(form.cleaned_data['drugAbuseConf']) / 100 if form.cleaned_data['drugAbuse'] else 0.0
            alcoholAbuse = float(form.cleaned_data['alcoholAbuseConf']) / 100 if form.cleaned_data['alcoholAbuse'] else 0.0

            cranialNerveDeficit = float(form.cleaned_data['cranialNerveDeficitConf']) / 100 if form.cleaned_data['cranialNerveDeficit'] else 0.0 
            massEffect = float(form.cleaned_data['massEffectConf']) / 100 if form.cleaned_data['massEffect'] else 0.0
            thromboembolicEvents = float(form.cleaned_data['thromboembolicEventsConf']) / 100 if form.cleaned_data['thromboembolicEvents'] else 0.0
            epilepsy = float(form.cleaned_data['epilepsyConf']) / 100 if form.cleaned_data['epilepsy'] else 0.0

            fearOfRupture = float(form.cleaned_data['fearOfRuptureConf']) / 100 if form.cleaned_data['fearOfRupture'] else 0.0
            multiplicity = float(form.cleaned_data['multiplicityConf']) / 100 if form.cleaned_data['multiplicity'] else 0.0

            neurocognitiveDisorder = float(form.cleaned_data['neurocognitiveDisorderConf']) / 100 if form.cleaned_data['neurocognitiveDisorder'] else 0.0
            coagulopathies = float(form.cleaned_data['coagulopathiesConf']) / 100 if form.cleaned_data['coagulopathies'] else 0.0
            psychiatricDisorder = float(form.cleaned_data['psychiatricDisorderConf']) / 100 if form.cleaned_data['psychiatricDisorder'] else 0.0

            irregularity = float(form.cleaned_data['irregularityConf']) / 100 if form.cleaned_data['irregularity'] else 0.0
            largeSizeOrAspectRatio = float(form.cleaned_data['largeSizeOrAspectRatioConf']) / 100 if form.cleaned_data['largeSizeOrAspectRatio'] else 0.0

            serialImagingGrowth = float(form.cleaned_data['serialImagingGrowthConf']) / 100 if form.cleaned_data['serialImagingGrowth'] else 0.0
            serialImagingFormation = float(form.cleaned_data['serialImagingFormationConf']) / 100 if form.cleaned_data['serialImagingFormation'] else 0.0
            CSVD = float(form.cleaned_data['CSVDConf']) / 100 if form.cleaned_data['CSVD'] else 0.0

            complexityRelatedRisk = float(form.cleaned_data['complexityRelatedRiskConf']) / 100 if form.cleaned_data['complexityRelatedRisk'] else 0.0

            uiats = UIATS(age, lifeExpectancy, maxDiameter, location, prevSAH=prevSAH, famSAH=famSAH, jfiEth=jfiEth, smoking=smoking, hypertension=hypertension, kidneyDisease=kidneyDisease, \
                drugAbuse=drugAbuse, alcoholAbuse=alcoholAbuse, cranialNerveDeficit=cranialNerveDeficit, massEffect=massEffect, thromboembolicEvents=thromboembolicEvents, epilepsy=epilepsy, \
                    fearOfRupture=fearOfRupture, multiplicity=multiplicity, neurocognitiveDisorder=neurocognitiveDisorder, coagulopathies=coagulopathies, psychiatricDisorder=psychiatricDisorder, \
                        irregularity=irregularity, largeSizeOrAspectRatio=largeSizeOrAspectRatio, serialImagingGrowth=serialImagingGrowth, serialImagingFormation=serialImagingFormation, CSVD=CSVD, \
                            complexityRelatedRisk= complexityRelatedRisk)
            
            repairScore = round(uiats.totalRepairScore, 2)
            conservativeManagementScore = round(uiats.totalConservativeManagementScore, 2)

            if (uiats.totalRepairScore - uiats.totalConservativeManagementScore > 3):
                conclusion = "The unruptured intracranial aneurysm treatment score therefore recommends aneurysm repair."
            elif (uiats.totalRepairScore - uiats.totalConservativeManagementScore < -3):
                conclusion = "The unruptured intracranial aneurysm treatment score therefore recommends aneurysm conservative management."
            else:
                conclusion = """The unruptured intracranial aneurysm treatment score therefore cannot make a clear recommendation. 
                    Additional factors should be considered when choosing a treatment option."""

            valid_submission = True

    else:
        form = UIATSForm()

    return render(request, 'uiats_fuzzy/uiats_form.html', {'form': form, 'valid_submission': valid_submission, 'repairScore': repairScore, 
    'conservativeManagementScore': conservativeManagementScore, 'conclusion': conclusion})