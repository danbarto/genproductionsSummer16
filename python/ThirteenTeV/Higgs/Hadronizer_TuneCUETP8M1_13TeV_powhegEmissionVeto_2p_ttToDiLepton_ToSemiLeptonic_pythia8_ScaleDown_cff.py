# Based on https://github.com/cms-sw/genproductions/blob/3b33b1e47f34941b84b6a582839bb8e5c5b05c16/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_powhegEmissionVeto_1p_LHE_pythia8_cff.py

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '23:mMin = 0.05',      # Solve problem with mZ cut                                   
    	    '24:mMin = 0.05',      # Solve problem with mW cut
            'TimeShower:mMaxGamma = 1.0',#cutting off lepton-pair production 
##in the electromagnetic shower
##to not overlap with ttZ/gamma* samples

  #ScaleDown Pythia8 parameters
  #'SigmaProcess:renormMultFac = 0.25', #Only for internal pythia hard processes
  #'SigmaProcess:factorMultFac = 0.25', #Only for internal pythia hard processes
	    'TimeShower:renormMultFac   = 0.25',	#FSR
  	    'TimeShower:factorMultFac   = 0.25',	#FSR
  	    'SpaceShower:renormMultFac  = 0.25',	#ISR
            'SpaceShower:factorMultFac  = 0.25',        #ISR

          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)
