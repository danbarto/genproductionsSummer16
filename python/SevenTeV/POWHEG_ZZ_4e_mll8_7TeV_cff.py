import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
                                     scriptName = cms.FileInPath("GeneratorInterface/LHEInterface/data/create_lhe_powheg.sh"),
                                     outputFile = cms.string("events_final.lhe"),
                                     numberOfParameters = cms.uint32(4),
                                     args = cms.vstring('slc5_ia32_gcc434/powheg/V1.0/src',
                                     'powhegboxv1.5_Feb2013',
                                     'ZZ',
                                     '/slc5_ia32_gcc434/powheg/V1.0/7TeV_Summer12/ZZ_4e_mll8_7TeV-powheg/v1/ZZ_4e_mll8_7TeV-powheg.input',
                                     ),
    nEvents = cms.uint32(50000)
                                            
                                             )

