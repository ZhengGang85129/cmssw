# /dev/CMSSW_2_1_0_pre6/HLT/V3 (CMSSW_2_1_0_pre6)

import FWCore.ParameterSet.Config as cms

block_hltDefaultOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*', 'keep FEDRawDataCollection_*_*_*', 'keep edmTriggerResults_*_*_*', 'keep triggerTriggerEvent_*_*_*', 'keep *_hltGtDigis_*_*', 'keep *_hltGctDigis_*_*', 'keep *_hltL1GtObjectMap_*_*', 'keep *_hltL1extraParticles_*_*' )
)



