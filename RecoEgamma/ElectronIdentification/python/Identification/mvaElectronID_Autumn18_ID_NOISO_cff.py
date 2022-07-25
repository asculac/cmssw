import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *
from os import path

mvaTag = "Autumn18IdNoIso"

weightFileDir = "RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Autumn_18_ID_NOISO"

mvaWeightFiles = cms.vstring(
     path.join(weightFileDir, "EB1_5.weights.xml.gz"), # EB1_5
     path.join(weightFileDir, "EB2_5.weights.xml.gz"), # EB2_5
     path.join(weightFileDir, "EE_5.weights.xml.gz"), # EE_5
     path.join(weightFileDir, "EB1_10.weights.xml.gz"), # EB1_10
     path.join(weightFileDir, "EB2_10.weights.xml.gz"), # EB2_10
     path.join(weightFileDir, "EE_10.weights.xml.gz"), # EE_10
     )

categoryCuts = cms.vstring(
     "pt < 10. & abs(superCluster.eta) < 0.800", # EB1_5
     "pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479", # EB2_5
     "pt < 10. & abs(superCluster.eta) >= 1.479", # EE_5
     "pt >= 10. & abs(superCluster.eta) < 0.800", # EB1_10
     "pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479", # EB2_10
     "pt >= 10. & abs(superCluster.eta) >= 1.479", # EE_10
     )

mvaEleID_Autumn18_ID_NOISO_HZZ_container = EleMVARaw_WP(
    idName = "mvaEleID-Autumn18-ID-NOISO-HZZ", mvaTag = mvaTag,
    cutCategory0 = "1.23224395464", # EB1_5
    cutCategory1 = "1.27981125918", # EB2_5
    cutCategory2 = "1.58892886041", # EE_5
    cutCategory3 = "-0.282180158595", # EB1_10
    cutCategory4 = "-0.329892323549", # EB2_10
    cutCategory5 = "-0.823446023944", # EE_10
    )


mvaEleID_Autumn18_ID_NOISO_producer_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    nCategories         = cms.int32(6),
    categoryCuts        = categoryCuts,
    weightFileNames     = mvaWeightFiles,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Autumn18_ID_NOISO_HZZ = configureVIDMVAEleID( mvaEleID_Autumn18_ID_NOISO_HZZ_container )

mvaEleID_Autumn18_ID_NOISO_HZZ.isPOGApproved = cms.untracked.bool(False)
