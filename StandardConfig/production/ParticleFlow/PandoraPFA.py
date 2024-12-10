#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

MyDDMarlinPandora = MarlinProcessorWrapper("MyDDMarlinPandora")
MyDDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "CoilName": ["Coil"],
    "CreateGaps": ["false"],
    "DigitalMuonHits": ["0"],
    "ECalBarrelDetectorName": ["EcalBarrel"],
    "ECalCaloHitCollections": [
        "EcalBarrelCollectionRec",
        "EcalBarrelCollectionGapHits",
        "EcalEndcapsCollectionRec",
        "EcalEndcapsCollectionGapHits",
        "EcalEndcapRingCollectionRec",
    ],
    "ECalEndcapDetectorName": ["EcalEndcap"],
    "ECalMipThreshold": ["0.5"],
    "ECalOtherDetectorNames": ["EcalPlug", "Lcal", "BeamCal"],
    "ECalToEMGeVCalibration": [CONSTANTS["PandoraEcalToEMScale"]],
    "ECalToHadGeVCalibrationBarrel": [CONSTANTS["PandoraEcalToHadBarrelScale"]],
    "ECalToHadGeVCalibrationEndCap": [CONSTANTS["PandoraEcalToHadEndcapScale"]],
    "ECalToMipCalibration": [CONSTANTS["PandoraEcalToMip"]],
    "FinalEnergyDensityBin": ["30"],
    "HCalBarrelDetectorName": ["HcalBarrel"],
    "HCalCaloHitCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
    "HCalEndcapDetectorName": ["HcalEndcap"],
    "HCalMipThreshold": ["0.3"],
    "HCalOtherDetectorNames": ["HcalRing", "LHcal"],
    "HCalToEMGeVCalibration": [CONSTANTS["PandoraHcalToEMScale"]],
    "HCalToHadGeVCalibration": [CONSTANTS["PandoraHcalToHadScale"]],
    "HCalToMipCalibration": [CONSTANTS["PandoraHcalToMip"]],
    "KinkVertexCollections": ["KinkVertices"],
    "LCalCaloHitCollections": ["LCAL"],
    "LHCalCaloHitCollections": ["LHCAL"],
    "MCParticleCollections": ["MCParticle"],
    "MaxBarrelTrackerInnerRDistance": ["105.0"],
    "MaxClusterEnergyToApplySoftComp": ["1000"],
    "MaxHCalHitHadronicEnergy": ["1000000."],
    "MinCleanCorrectedHitEnergy": ["0.1"],
    "MinCleanHitEnergy": ["0.5"],
    "MinCleanHitEnergyFraction": ["0.01"],
    "MuonBarrelDetectorName": ["YokeBarrel"],
    "MuonCaloHitCollections": ["MUON"],
    "MuonEndcapDetectorName": ["YokeEndcap"],
    "MuonOtherDetectorNames": [],
    "MuonToMipCalibration": [CONSTANTS["PandoraMuonToMip"]],
    "NEventsToSkip": ["0"],
    "PFOCollectionName": ["PandoraPFOs"],
    "PandoraSettingsXmlFile": [CONSTANTS["PandoraSettingsFile"]],
    "ProngVertexCollections": ["ProngVertices"],
    "RelCaloHitCollections": [
        "EcalBarrelRelationsSimRec",
        "EcalEndcapsRelationsSimRec",
        "EcalEndcapRingRelationsSimRec",
        "HcalBarrelRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
        "RelationMuonHit",
        "RelationLHcalHit",
        "RelationLcalHit",
    ],
    "RelTrackCollections": ["MarlinTrkTracksMCTruthLink"],
    "SoftwareCompensationEnergyDensityBins": [
        "0",
        "2",
        "5",
        "7.5",
        "9.5",
        "13",
        "16",
        "20",
        "23.5",
        "28",
    ],
    "SoftwareCompensationWeights": [CONSTANTS["PandoraSoftwareCompensationWeights"]],
    "SplitVertexCollections": ["SplitVertices"],
    "StartVertexAlgorithmName": ["PandoraPFANew"],
    "StartVertexCollectionName": ["PandoraPFANewStartVertices"],
    "TrackCollections": ["MarlinTrkTracks"],
    "TrackCreatorName": ["DDTrackCreatorILD"],
    "TrackerBarrelDetectorNames": ["TPC"],
    "TrackerEndcapDetectorNames": ["FTD"],
    "UseDD4hepField": ["false"],
    "UseOldTrackStateCalculation": ["0", "1"],
    "V0VertexCollections": ["V0Vertices"],
    "VertexBarrelDetectorName": ["VXD"],
    "YokeBarrelNormalVector": ["0", "1", "0"],
}

PandoraPFASequence = [MyDDMarlinPandora]
