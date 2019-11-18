WAV_FORMATS = {
    0: "UNKNOWN",  # Microsoft Corporation
    1: "PCM",  # Microsoft Corporation
    2: "ADPCM",  # Microsoft Corporation
    3: "IEEE_FLOAT",  # Microsoft Corporation
    4: "VSELP",  # Compaq Computer Corp.
    5: "IBM_CVSD",  # IBM Corporation
    6: "ALAW",  # Microsoft Corporation
    7: "MULAW",  # Microsoft Corporation
    8: "DTS",  # Microsoft Corporation
    9: "DRM",  # Microsoft Corporation
    16: "OKI_ADPCM",  # OKI
    17: "DVI_ADPCM",  # Intel Corporation
    18: "MEDIASPACE_ADPCM",  # Videologic
    19: "SIERRA_ADPCM",  # Sierra Semiconductor Corp
    20: "G723_ADPCM",  # Antex Electronics Corporation
    21: "DIGISTD",  # DSP Solutions, Inc.
    22: "DIGIFIX",  # DSP Solutions, Inc.
    23: "DIALOGIC_OKI_ADPCM",  # Dialogic Corporation
    24: "MEDIAVISION_ADPCM",  # Media Vision, Inc.
    25: "CU_CODEC",  # Hewlett-Packard Company
    32: "YAMAHA_ADPCM",  # Yamaha Corporation of America
    33: "SONARC",  # Speech Compression
    34: "DSPGROUP_TRUESPEECH",  # DSP Group, Inc
    35: "ECHOSC1",  # Echo Speech Corporation
    36: "AUDIOFILE_AF36",  # Virtual Music, Inc.
    37: "APTX",  # Audio Processing Technology
    38: "AUDIOFILE_AF10",  # Virtual Music, Inc.
    39: "PROSODY_1612",  # Aculab plc
    40: "LRC",  # Merging Technologies S.A.
    48: "DOLBY_AC2",  # Dolby Laboratories
    49: "GSM610",  # Microsoft Corporation
    50: "MSNAUDIO",  # Microsoft Corporation
    51: "ANTEX_ADPCME",  # Antex Electronics Corporation
    52: "CONTROL_RES_VQLPC",  # Control Resources Limited
    53: "DIGIREAL",  # DSP Solutions, Inc.
    54: "DIGIADPCM",  # DSP Solutions, Inc.
    55: "CONTROL_RES_CR10",  # Control Resources Limited
    56: "NMS_VBXADPCM",  # Natural MicroSystems
    57: "CS_IMAADPCM",  # Crystal Semiconductor IMA ADPCM
    58: "ECHOSC3",  # Echo Speech Corporation
    59: "ROCKWELL_ADPCM",  # Rockwell International
    60: "ROCKWELL_DIGITALK",  # Rockwell International
    61: "XEBEC",  # Xebec Multimedia Solutions Limited
    64: "G721_ADPCM",  # Antex Electronics Corporation
    65: "G728_CELP",  # Antex Electronics Corporation
    66: "MSG723",  # Microsoft Corporation
    80: "MPEG",  # Microsoft Corporation
    82: "RT24",  # InSoft, Inc.
    83: "PAC",  # InSoft, Inc.
    85: "MPEGLAYER3",  # ISO/MPEG Layer3 Format Tag
    89: "LUCENT_G723",  # Lucent Technologies
    96: "CIRRUS",  # Cirrus Logic
    97: "ESPCM",  # ESS Technology
    98: "VOXWARE",  # Voxware Inc
    99: "CANOPUS_ATRAC",  # Canopus, co., Ltd.
    100: "G726_ADPCM",  # APICOM
    101: "G722_ADPCM",  # APICOM
    103: "DSAT_DISPLAY",  # Microsoft Corporation
    105: "VOXWARE_BYTE_ALIGNED",  # Voxware Inc
    112: "VOXWARE_AC8",  # Voxware Inc
    113: "VOXWARE_AC10",  # Voxware Inc
    114: "VOXWARE_AC16",  # Voxware Inc
    115: "VOXWARE_AC20",  # Voxware Inc
    116: "VOXWARE_RT24",  # Voxware Inc
    117: "VOXWARE_RT29",  # Voxware Inc
    118: "VOXWARE_RT29HW",  # Voxware Inc
    119: "VOXWARE_VR12",  # Voxware Inc
    120: "VOXWARE_VR18",  # Voxware Inc
    121: "VOXWARE_TQ40",  # Voxware Inc
    128: "SOFTSOUND",  # Softsound, Ltd.
    129: "VOXWARE_TQ60",  # Voxware Inc
    130: "MSRT24",  # Microsoft Corporation
    131: "G729A",  # AT&amp;T Labs, Inc.
    132: "MVI_MVI2",  # Motion Pixels
    133: "DF_G726",  # DataFusion Systems (Pty) (Ltd)
    134: "DF_GSM610",  # DataFusion Systems (Pty) (Ltd)
    136: "ISIAUDIO",  # Iterated Systems, Inc.
    137: "ONLIVE",  # OnLive! Technologies, Inc.
    145: "SBC24",  # Siemens Business Communications Sys
    146: "DOLBY_AC3_SPDIF",  # Sonic Foundry
    147: "MEDIASONIC_G723",  # MediaSonic
    148: "PROSODY_8KBPS",  # Aculab plc
    151: "ZYXEL_ADPCM",  # ZyXEL Communications, Inc.
    152: "PHILIPS_LPCBB",  # Philips Speech Processing
    153: "PACKED",  # Studer Professional Audio AG
    160: "MALDEN_PHONYTALK",  # Malden Electronics Ltd.
    256: "RHETOREX_ADPCM",  # Rhetorex Inc.
    257: "IRAT",  # BeCubed Software Inc.
    273: "VIVO_G723",  # Vivo Software
    274: "VIVO_SIREN",  # Vivo Software
    291: "DIGITAL_G723",  # Digital Equipment Corporation
    293: "SANYO_LD_ADPCM",  # Sanyo Electric Co., Ltd.
    304: "SIPROLAB_ACEPLNET",  # Sipro Lab Telecom Inc.
    305: "SIPROLAB_ACELP4800",  # Sipro Lab Telecom Inc.
    306: "SIPROLAB_ACELP8V3",  # Sipro Lab Telecom Inc.
    307: "SIPROLAB_G729",  # Sipro Lab Telecom Inc.
    308: "SIPROLAB_G729A",  # Sipro Lab Telecom Inc.
    309: "SIPROLAB_KELVIN",  # Sipro Lab Telecom Inc.
    320: "G726ADPCM",  # Dictaphone Corporation
    336: "QUALCOMM_PUREVOICE",  # Qualcomm, Inc.
    337: "QUALCOMM_HALFRATE",  # Qualcomm, Inc.
    341: "TUBGSM",  # Ring Zero Systems, Inc.
    352: "MSAUDIO1",  # Microsoft Corporation
    368: "UNISYS_NAP_ADPCM",  # Unisys Corp.
    369: "UNISYS_NAP_ULAW",  # Unisys Corp.
    370: "UNISYS_NAP_ALAW",  # Unisys Corp.
    371: "UNISYS_NAP_16K",  # Unisys Corp.
    512: "CREATIVE_ADPCM",  # Creative Labs, Inc
    514: "CREATIVE_FASTSPEECH8",  # Creative Labs, Inc
    515: "CREATIVE_FASTSPEECH10",  # Creative Labs, Inc
    528: "UHER_ADPCM",  # UHER informatic GmbH
    544: "QUARTERDECK",  # Quarterdeck Corporation
    560: "ILINK_VC",  # I-link Worldwide
    576: "RAW_SPORT",  # Aureal Semiconductor
    577: "ESST_AC3",  # ESS Technology, Inc.
    592: "IPI_HSX",  # Interactive Products, Inc.
    593: "IPI_RPELP",  # Interactive Products, Inc.
    608: "CS2",  # Consistent Software
    624: "SONY_SCX",  # Sony Corp.
    768: "FM_TOWNS_SND",  # Fujitsu Corp.
    1024: "BTV_DIGITAL",  # Brooktree Corporation
    1104: "QDESIGN_MUSIC",  # QDesign Corporation
    1664: "VME_VMPCM",  # AT&amp;T Labs, Inc.
    1665: "TPC",  # AT&amp;T Labs, Inc.
    4096: "OLIGSM",  # Ing C. Olivetti &amp; C., S.p.A.
    4097: "OLIADPCM",  # Ing C. Olivetti &amp; C., S.p.A.
    4098: "OLICELP",  # Ing C. Olivetti &amp; C., S.p.A.
    4099: "OLISBC",  # Ing C. Olivetti &amp; C., S.p.A.
    4100: "OLIOPR",  # Ing C. Olivetti &amp; C., S.p.A.
    4352: "LH_CODEC",  # Lernout &amp; Hauspie
    5120: "NORRIS",  # Norris Communications, Inc.
    5376: "SOUNDSPACE_MUSICOMPRESS",  # AT&amp;T Labs, Inc.
    8192: "DVM"  # FAST Multimedia AG
}


def get_AudioFormat(AudioFormat):
    if AudioFormat in WAV_FORMATS:
        return WAV_FORMATS[AudioFormat]
    return "UNKNOWN"
