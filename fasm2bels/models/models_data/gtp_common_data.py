params = {
    "PLL0_CFG": {
        "type": "BIN",
        "digits": 27
    },
    "PLL0_REFCLK_DIV": {
        "type": "INT",
        "values": [1, 2],
        "encoding": [16, 0],
        "digits": 5
    },
    "PLL0_FBDIV_45": {
        "type": "INT",
        "values": [4, 5],
        "encoding": [0, 1],
        "digits": 1
    },
    "PLL0_FBDIV": {
        "type": "INT",
        "values": [1, 2, 3, 4, 5],
        "encoding": [16, 0, 1, 2, 3],
        "digits": 6
    },
    "PLL0_LOCK_CFG": {
        "type": "BIN",
        "digits": 9
    },
    "PLL0_INIT_CFG": {
        "type": "BIN",
        "digits": 24
    },
    "RSVD_ATTR0": {
        "type": "BIN",
        "digits": 16
    },
    "PLL1_DMON_CFG": {
        "type": "BIN",
        "digits": 1
    },
    "PLL0_DMON_CFG": {
        "type": "BIN",
        "digits": 1
    },
    "COMMON_CFG": {
        "type": "BIN",
        "digits": 32
    },
    "PLL_CLKOUT_CFG": {
        "type": "BIN",
        "digits": 8
    },
    "BIAS_CFG": {
        "type": "BIN",
        "digits": 64
    },
    "RSVD_ATTR1": {
        "type": "BIN",
        "digits": 16
    },
    "PLL1_INIT_CFG": {
        "type": "BIN",
        "digits": 24
    },
    "PLL1_LOCK_CFG": {
        "type": "BIN",
        "digits": 9
    },
    "PLL1_REFCLK_DIV": {
        "type": "INT",
        "values": [1, 2],
        "encoding": [16, 0],
        "digits": 5
    },
    "PLL1_FBDIV_45": {
        "type": "INT",
        "values": [4, 5],
        "encoding": [0, 1],
        "digits": 1
    },
    "PLL1_FBDIV": {
        "type": "INT",
        "values": [1, 2, 3, 4, 5],
        "encoding": [16, 0, 1, 2, 3],
        "digits": 6
    },
    "PLL1_CFG": {
        "type": "BIN",
        "digits": 27
    }
}

ports = {
    "inputs": [
        ("BGBYPASSB", 1),
        ("BGMONITORENB", 1),
        ("BGPDB", 1),
        ("BGRCALOVRDENB", 1),
        ("DRPCLK", 1),
        ("DRPEN", 1),
        ("DRPWE", 1),
        ("PLL0LOCKDETCLK", 1),
        ("PLL0LOCKEN", 1),
        ("PLL0PD", 1),
        ("PLL0RESET", 1),
        ("PLL1LOCKDETCLK", 1),
        ("PLL1LOCKEN", 1),
        ("PLL1PD", 1),
        ("PLL1RESET", 1),
        ("RCALENB", 1),
        ("DRPDI", 16),
        ("PLLRSVD1", 16),
        ("PLL0REFCLKSEL", 3),
        ("PLL1REFCLKSEL", 3),
        ("BGRCALOVRD", 5),
        ("PLLRSVD2", 5),
        ("DRPADDR", 8),
        ("PMARSVD", 8),
    ],
    "outputs": [
        ("DRPRDY", 1),
        ("PLL0FBCLKLOST", 1),
        ("PLL0LOCK", 1),
        ("PLL0REFCLKLOST", 1),
        ("PLL1FBCLKLOST", 1),
        ("PLL1LOCK", 1),
        ("PLL1REFCLKLOST", 1),
        ("REFCLKOUTMONITOR0", 1),
        ("REFCLKOUTMONITOR1", 1),
        ("DRPDO", 16),
        ("PMARSVDOUT", 16),
        ("DMONITOROUT", 8),
    ],
}

