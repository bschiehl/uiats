from enum import Enum, unique
from .FuzzySetMembershipFunctions import ageYoungMembership, lifeExpectancyLowMembership, maxDiameterLargeMembership, ageRiskHighMembership, sizeRiskHighMembership

@unique
class uiaLocation(Enum):
    BASA_BIFURCATION = 0
    VERTEBRAL_BASILAR_ARTERY = 1
    ACOMA_PCOMA = 2

# implementation of the unruptured intracranial aneurysm treatment score that makes use of fuzzy sets to smoothe out the transitions between classifications
class UIATS:
    def __init__(self, age, lifeExpectancy, maxDiameter, location, prevSAH=0, famSAH=0, jfiEth=0, smoking=0, \
        hypertension=0, kidneyDisease=0, drugAbuse=0, alcoholAbuse=0, cranialNerveDeficit=0, massEffect=0, thromboembolicEvents=0, \
            epilepsy=0, fearOfRupture=0, multiplicity=0, neurocognitiveDisorder=0, coagulopathies=0, psychiatricDisorder=0, irregularity=0, \
                largeSizeOrAspectRatio=0, serialImagingGrowth=0, serialImagingFormation=0, CSVD=0, complexityRelatedRisk=0):
        self.age = age
        self.lifeExpectancy = lifeExpectancy
        self.maxDiameter = maxDiameter
        self.location = uiaLocation(location)
        self.prevSAH = prevSAH
        self.famSAH = famSAH
        self.jfiEth = jfiEth
        self.smoking = smoking
        self.hypertension = hypertension
        self.kidneyDisease = kidneyDisease
        self.drugAbuse = drugAbuse
        self.alcoholAbuse = alcoholAbuse
        self.cranialNerveDeficit = cranialNerveDeficit
        self.massEffect = massEffect
        self.thromboembolicEvents = thromboembolicEvents
        self.epilepsy = epilepsy
        self.fearOfRupture = fearOfRupture
        self.multiplicity = multiplicity
        self.neurocognitiveDisorder = neurocognitiveDisorder
        self.coagulopathies = coagulopathies
        self.psychiatricDisorder = psychiatricDisorder
        self.irregularity = irregularity
        self.largeSizeOrAspectRatio = largeSizeOrAspectRatio
        self.serialImagingGrowth = serialImagingGrowth
        self.serialImagingFormation = serialImagingFormation
        self.CSVD = CSVD
        self.complexityRelatedRisk = complexityRelatedRisk

    @property
    def totalRepairScore(self):
        def _ageScore():
            return ageYoungMembership(self.age) * 4

        def _riskFactorIncidenceScore():
            score = 0
            score += 4 * self.prevSAH
            score += 3 * self.famSAH
            score += 2 * self.jfiEth
            score += 3 * self.smoking
            score += 2 * self.hypertension
            score += 2 * self.kidneyDisease
            score += 2 * self.drugAbuse
            score += 1 * self.drugAbuse
            return score
        
        def _relatedSymptomsScore():
            score = 0
            score += 4 * self.cranialNerveDeficit
            score += 4 * self.massEffect
            score += 3 * self.thromboembolicEvents
            score += 1 * self.epilepsy
            return score
    
        def _otherPatientFactorsScore():
            score = 0
            score += 2 * self.fearOfRupture
            score += 1 * self.multiplicity
            return score

        def _maxDiameterScore():
            return maxDiameterLargeMembership(self.maxDiameter) * 4   
        
        def _morphologyScore():
            score = 0
            score += 3 * self.irregularity
            score += 1 * self.largeSizeOrAspectRatio
            return score

        def _locationScore():
            if (self.location == uiaLocation.BASA_BIFURCATION):
                return 5
            elif (self.location == uiaLocation.VERTEBRAL_BASILAR_ARTERY):
                return 4
            elif (self.location == uiaLocation.ACOMA_PCOMA):
                return 2
        
        def _otherAneurysmFactorsScore():
            score = 0    
            score += 4 * self.serialImagingGrowth
            score += 3 * self.serialImagingFormation
            score += 1 * self.CSVD
            return score
        
        return _ageScore() + _riskFactorIncidenceScore() + _relatedSymptomsScore() + _otherPatientFactorsScore() + _maxDiameterScore() + _morphologyScore() + \
            _locationScore() + _otherAneurysmFactorsScore()
    
    @property
    def totalConservativeManagementScore(self):
        def _lifeExpectancyScore():
            return lifeExpectancyLowMembership(self.lifeExpectancy) * 3 + 1
    
        def _comorbidDiseaseScore():
            score = 0
            score += 3 * self.neurocognitiveDisorder
            score += 2 * self.coagulopathies
            score += 2 * self.psychiatricDisorder
            return score

        def _ageRelatedRiskScore():
            return ageRiskHighMembership(self.age) * 5

        def _sizeRelatedRiskScore():
            return sizeRiskHighMembership(self.maxDiameter) * 5
        
        def _complexityRelatedRiskScore():
            return self.complexityRelatedRisk * 3
        
        return 5 + _lifeExpectancyScore() + _comorbidDiseaseScore() + _ageRelatedRiskScore() + _sizeRelatedRiskScore() + _complexityRelatedRiskScore()
