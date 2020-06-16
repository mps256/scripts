#!/usr/bin/env python3


# map of information pertinent to running automated builds
# map keys are distro short names (see distributions.py)

envvars = {
    "GITHUB_TOKEN": "",
    "GITHUB_USER": "Galaxy-MSM8916",
    "GITHUB_REPO": "releases",
}

jobs = {
    "lineage": {
        "17.1": {
            "devices": ["gprimelte", "j7ltespr"],
            "picks": [],
            "picks_lineage": [],
            "build_variants": ["eng"],
            "targets": ["otapackage", "recoveryimage"],
        },
    },

    "lineage-go": {
        "17.1": {
            "devices": [],
            "picks": ["android-go"],
            "picks_lineage": [],
            "build_variants": ["eng"],
            "targets": ["otapackage"],
        },
    },

    "rr": {
        "ten": {
            "devices": [],
            "picks": [],
            "picks_lineage": [],
            "build_variants": ["eng"],
            "targets": ["otapackage"],
        },
    },
}
