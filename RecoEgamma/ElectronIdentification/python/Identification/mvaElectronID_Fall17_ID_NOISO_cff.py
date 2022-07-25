import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *
from os import path

mvaTag = "Fall17IdNoIso"

weightFileDir = "RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall_17_ID_NOISO"

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

mvaEleID_Fall17_ID_NOISO_HZZ_container = EleMVARaw_WP(
    idName = "mvaEleID-Fall17-ID-NOISO-HZZ", mvaTag = mvaTag,
    cutCategory0 = "1.24543251867", # EB1_5
    cutCategory1 = "1.25630711864", # EB2_5
    cutCategory2 = "1.54893999102", # EE_5
    cutCategory3 = "-0.305655752031", # EB1_10
    cutCategory4 = "-0.357634905516", # EB2_10
    cutCategory5 = "-0.86745660378", # EE_10
    )


mvaEleID_Fall17_ID_NOISO_producer_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    nCategories         = cms.int32(6),
    categoryCuts        = categoryCuts,
    weightFileNames     = mvaWeightFiles,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Fall17_ID_NOISO_HZZ = configureVIDMVAEleID( mvaEleID_Fall17_ID_NOISO_HZZ_container )

mvaEleID_Fall17_ID_NOISO_HZZ.isPOGApproved = cms.untracked.bool(False)
